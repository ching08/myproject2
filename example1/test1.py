import pytest
from gold_train.goldengate_tests.Lib import putil

# apply tc_logger fixture to all functions


@pytest.mark.usefixture("tc_logger")
def test_tc1():
    '''
    demo without muti_assert, tc1 abrot on the 1st False assert
    '''
    putil.myassert(False, "step 1 is False")
    putil.myassert(True, "Step2 is True")
    putil.myassert(False, "Step3 is False")


def test_tc2(multi_assert):
    '''
    demo with muti_assert, tc3 does NOT abrot on the 1st False assert
    '''
    putil.myassert(False, "step 1 is False")
    putil.myassert(True, "Step2 is True")
    putil.myassert(False, "Step3 is False")


@pytest.mark.parametrize("input1,input2", [(1, "x1"), (2, "x3"), (3, "x3")])
def test_tc3(input1, input2):
    '''
    demo loop testcase with parameter
    '''
    putil.myassert(input1 == 2, "expecting parameter input1 %s == 2 " % input1)
