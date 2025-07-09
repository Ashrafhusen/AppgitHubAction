from src.math_opreration import add, sub

def test_add():
    assert add(2,4) == 6
    assert add(-1, 9) == 8

def test_sub():
    assert sub(10, 5) == 5
    assert sub(0, 0) == 0
    assert sub(3, 7) == -4