import pytest 
import bloomdata as bd

def test_increment_int():
    assert bd.increment(3) == 4
    assert bd.increment(-2) == -1

def test_increment_float():
    assert bd.increment(4.5) == 5.5

def test_increment_int_return_type():
    assert isinstance(bd.increment(3), int)
    assert isinstance(bd.increment(4.32), float)