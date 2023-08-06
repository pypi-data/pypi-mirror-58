# Copyright 2016, Yahoo Inc.
# Licensed under the terms of the Apache License, Version 2.0. See the LICENSE file associated with the project for terms.

import dill
import pytest

from graphtik import NO_RESULT, compose, operation, optional, sideffect, vararg, varargs
from graphtik.network import yield_ops
from graphtik.op import (
    Operation,
    FunctionalOperation,
    as_renames,
    reparse_operation_data,
)


@pytest.fixture(params=[None, ["some"]])
def opname(request):
    return request.param


@pytest.fixture(params=[None, ["some"]])
def opneeds(request):
    return request.param


@pytest.fixture(params=[None, ["some"]])
def opprovides(request):
    return request.param


def test_repr_smoke(opname, opneeds, opprovides):
    # Simply check __repr__() does not crash on partial attributes.
    kw = locals().copy()
    kw = {name[2:]: arg for name, arg in kw.items()}

    op = operation(**kw)
    str(op)


def test_repr_returns_dict():
    assert (
        str(operation(lambda: None, returns_dict=True)())
        == "FunctionalOperation(name='None', needs=[], provides=[], fn{}='<lambda>')"
    )


@pytest.mark.parametrize(
    "opargs, exp",
    [
        ((None, None, None), (None, (), ())),
        ## Check name
        (("_", "a", ("A",)), ("_", ("a",), ("A",))),
        (((), ("a",), None), ((), ("a",), ())),
        ((("a",), "a", "b"), (("a",), ("a",), ("b",))),
        ((("a",), None, None), (("a",), (), ())),
        ## Check needs
        (((), (), None), ((), (), ())),
        (((), [], None), ((), [], ())),
        (("", object(), None), ValueError("Cannot tuple-ize needs")),
        (("", [None], None), ValueError("All `needs` must be str")),
        (("", [()], None), ValueError("All `needs` must be str")),
        ## Check provides
        (((), "a", ()), ((), ("a",), ())),
        (((), "a", []), ((), ("a",), [])),
        (("", "a", object()), ValueError("Cannot tuple-ize provides")),
        (("", "a", (None,)), ValueError("All `provides` must be str")),
        (("", "a", [()]), ValueError("All `provides` must be str")),
    ],
)
def test_validation(opargs, exp):
    if isinstance(exp, Exception):
        with pytest.raises(type(exp), match=str(exp)):
            reparse_operation_data(*opargs)
    else:
        assert reparse_operation_data(*opargs) == exp


def test_returns_dict():
    result = {"a": 1}

    op = operation(lambda: result, provides="a", returns_dict=True)()
    assert op.compute({}) == result

    op = operation(lambda: 1, provides="a", returns_dict=False)()
    assert op.compute({}) == result


@pytest.fixture(params=[None, ["a", "b"]])
def asked_outputs(request):
    return request.param


@pytest.mark.parametrize(
    "result", [None, 3.14, (), "", "foobar", ["b", "c", "e"], {"f"}]
)
def test_results_validation_iterable_BAD(result, asked_outputs):
    op = operation(lambda: result, provides=["a", "b"], returns_dict=False)()
    with pytest.raises(ValueError, match="Expected x2 ITERABLE results"):
        op.compute({}, outputs=asked_outputs)


@pytest.mark.parametrize("result", [None, 3.14, [], "foo", ["b", "c", "e"], {"a", "b"}])
def test_dict_results_validation_BAD(result, asked_outputs):
    op = operation(lambda: result, provides=["a", "b"], returns_dict=True)()
    with pytest.raises(ValueError, match="Expected dict-results"):
        op.compute({}, outputs=asked_outputs)


@pytest.mark.parametrize("result", [{"a": 1}, {"a": 1, "b": 2, "c": 3}])
def test_dict_results_validation_MISMATCH(result, asked_outputs):
    op = operation(lambda: result, provides=["a", "b"], returns_dict=True)()
    with pytest.raises(ValueError, match="mismatched provides"):
        op.compute({}, outputs=asked_outputs)


def test_varargs():
    def sumall(a, *args, b=0, **kwargs):
        return a + sum(args) + b + sum(kwargs.values())

    op = operation(
        sumall,
        name="t",
        needs=[
            "a",
            vararg("arg1"),
            vararg("arg2"),
            varargs("args"),
            optional("b"),
            optional("c"),
        ],
        provides="sum",
    )()

    exp = sum(range(8))
    assert op.compute(dict(a=1, arg1=2, arg2=3, args=[4, 5], b=6, c=7))["sum"] == exp
    assert op.compute(dict(a=1, arg1=2, arg2=3, args=[4, 5], c=7))["sum"] == exp - 6
    assert op.compute(dict(a=1, arg1=2, arg2=3, args=[4, 5], b=6))["sum"] == exp - 7
    assert op.compute(dict(a=1, arg2=3, args=[4, 5], b=6, c=7))["sum"] == exp - 2
    assert op.compute(dict(a=1, arg1=2, arg2=3, b=6, c=7))["sum"] == exp - 4 - 5
    with pytest.raises(ValueError, match="Missing compulsory needs.+'a'"):
        assert op.compute(dict(arg1=2, arg2=3, b=6, c=7))


def test_op_node_props_bad():
    op_factory = operation(lambda: None, name="a", node_props="SHOULD BE DICT")
    with pytest.raises(ValueError, match="`node_props` must be"):
        op_factory()


def test_op_node_props():
    op_factory = operation(lambda: None, name="a", node_props=())
    assert op_factory.node_props == ()
    assert op_factory().node_props == {}

    np = {"a": 1}
    op = operation(lambda: None, name="a", node_props=np)()
    assert op.node_props == np


def _collect_op_props(netop):
    return {
        k.name: v
        for k, v in netop.net.graph.nodes(data=True)
        if isinstance(k, Operation)
    }


def test_netop_node_props():
    op1 = operation(lambda: None, name="a", node_props={"a": 11, "b": 0, "bb": 2})()
    op2 = operation(lambda: None, name="b", node_props={"a": 3, "c": 4})()
    netop = compose("n", op1, op2, node_props={"bb": 22, "c": 44})

    exp = {"a": {"a": 11, "b": 0, "bb": 22, "c": 44}, "b": {"a": 3, "bb": 22, "c": 44}}
    node_props = _collect_op_props(netop)
    assert node_props == exp

    # Check node-prop sideffects are not modified
    #
    assert op1.node_props == {"a": 11, "b": 0, "bb": 2}
    assert op2.node_props == {"a": 3, "c": 4}


def test_netop_merge_node_props():
    op1 = operation(lambda: None, name="a", node_props={"a": 1})()
    netop1 = compose("n1", op1)
    op2 = operation(lambda: None, name="a", node_props={"a": 11, "b": 0, "bb": 2})()
    op3 = operation(lambda: None, name="b", node_props={"a": 3, "c": 4})()
    netop2 = compose("n2", op2, op3)

    netop = compose("n", netop1, netop2, node_props={"bb": 22, "c": 44}, merge=False)
    exp = {
        "n1.a": {"a": 1, "bb": 22, "c": 44},
        "n2.a": {"a": 11, "b": 0, "bb": 22, "c": 44},
        "n2.b": {"a": 3, "bb": 22, "c": 44},
    }
    node_props = _collect_op_props(netop)
    assert node_props == exp

    netop = compose("n", netop1, netop2, node_props={"bb": 22, "c": 44}, merge=True)
    exp = {"a": {"a": 1, "bb": 22, "c": 44}, "b": {"a": 3, "bb": 22, "c": 44}}
    node_props = _collect_op_props(netop)
    assert node_props == exp


@pytest.mark.parametrize(
    "inp, exp",
    [
        ({"a": "b"}, {"a": "b"}.items()),
        ((1, 2), [(1, 2)]),
        ([(1, 2)], [(1, 2)]),
        ([], []),
        ((), []),
        (("ab", "ad"), [("a", "b"), ("a", "d")]),
    ],
)
def test_as_renames(inp, exp):
    as_renames((1, 2), "talias")


@pytest.mark.parametrize(
    "opbuilder, ex",
    [
        (
            operation(str, aliases={"a": 1}),
            r"Operation `aliases` contain sources not found in real `provides`: \['a'\]",
        ),
        (
            operation(str, name="t", provides="a", aliases={"a": 1, "b": 2}),
            r"Operation `aliases` contain sources not found in real `provides`: \['b'\]",
        ),
        (
            operation(
                str, name="t", provides=sideffect("a"), aliases={sideffect("a"): 1}
            ),
            r"must not contain `sideffects`",
        ),
        (
            operation(str, name="t", provides="a", aliases={"a": sideffect("AA")}),
            r"must not contain `sideffects`",
        ),
    ],
)
def test_provides_aliases_BAD(opbuilder, ex):
    with pytest.raises(ValueError, match=ex):
        opbuilder()


def test_provides_aliases():
    op = operation(str, name="t", needs="s", provides="a", aliases={"a": "aa"})()
    assert op.provides == {"a", "aa"}
    assert op.compute({"s": "k"}) == {"a": "k", "aa": "k"}


def test_reschedule_unknown_dict_outs():
    op = operation(
        lambda: {"b": "B"}, name="t", provides=["a"], reschedule=1, returns_dict=1
    )()
    with pytest.raises(ValueError, match=r"contained unkown provides\['b'\]"):
        op.compute({})

    op = operation(
        lambda: {"BAD": "B"}, name="t", provides=["a"], reschedule=1, returns_dict=1
    )()
    with pytest.raises(ValueError, match=r"contained unkown provides\['BAD'\]"):
        op.compute({})


def test_rescheduled_op_repr():
    op = operation(str, name="t", provides=["a"], reschedule=True)
    assert str(op) == "operation(name='t', needs=[], provides=['a']?, fn='str')"
    assert (
        str(op())
        == "FunctionalOperation(name='t', needs=[], provides=['a']?, fn='str')"
    )


def test_endured_op_repr():
    op = operation(str, name="t", provides=["a"], endured=True)
    assert str(op) == "operation!(name='t', needs=[], provides=['a'], fn='str')"
    assert (
        str(op())
        == "FunctionalOperation!(name='t', needs=[], provides=['a'], fn='str')"
    )


def test_endured_rescheduled_op_repr():
    op = operation(str, name="t", reschedule=1, endured=1)
    assert str(op) == "operation!(name='t', needs=[], provides=[]?, fn='str')"
    assert (
        str(op()) == "FunctionalOperation!(name='t', needs=[], provides=[]?, fn='str')"
    )


def test_reschedule_outputs():
    op = operation(
        lambda: ["A", "B"], name="t", provides=["a", "b", "c"], reschedule=True
    )()
    assert op.compute({}) == {"a": "A", "b": "B"}

    # NOTE that for a single return item, it must be a collection.
    op = operation(lambda: ["AA"], name="t", provides=["a", "b"], reschedule=True)()
    assert op.compute({}) == {"a": "AA"}

    op = operation(lambda: NO_RESULT, name="t", provides=["a", "b"], reschedule=True)()
    assert op.compute({}) == {}

    op = operation(
        lambda: {"b": "B"}, name="t", provides=["a", "b"], reschedule=1, returns_dict=1
    )()
    assert op.compute({}) == {"b": "B"}

    op = operation(
        lambda: {"b": "B"},
        name="t",
        provides=["a", "b"],
        aliases={"a": "aa", "b": "bb"},
        reschedule=1,
        returns_dict=1,
    )()
    assert op.compute({}) == {"b": "B", "bb": "B"}


@pytest.mark.parametrize("attr, value", [("outputs", [1]), ("predicate", lambda: None)])
def test_netop_narrow_attributes(attr, value):
    netop = compose("1", operation(str, name="op1")())
    assert getattr(netop.narrowed(**{attr: value}), attr) == value


@pytest.mark.parametrize(
    "attr, value",
    [
        ("reschedule", None),
        ("reschedule", 1),
        ("reschedule", False),
        ("endured", None),
        ("endured", True),
        ("endured", 0),
    ],
)
def test_netop_conveys_attr(attr, value):
    def _opsattrs(ops, attr, value):
        vals = [getattr(op, attr) for op in ops if isinstance(op, Operation)]
        assert all(v == value for v in vals)

    kw = {attr: value}
    _opsattrs(compose("1", operation(str)(), **kw).net.graph, attr, value)
    _opsattrs(
        compose(
            "2", operation(str, name=1)(), operation(str, name=2)(), **kw
        ).net.graph,
        attr,
        value,
    )


@pytest.mark.parametrize(
    "op", [Operation, FunctionalOperation,
    operation(str)(), operation(lambda: None)()]
)
def test_dill_ops(op):
    dill.loads(dill.dumps(op))
