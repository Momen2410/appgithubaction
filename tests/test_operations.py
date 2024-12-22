from src.math_operations import add, sub

def test_add():
    assert add(2, 3) == 5
    assert add(-1, -2) == -3
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0
    
def test_sub():
    assert sub(5, 3) == 2
    assert sub(-1, -2) == 1
    assert sub(0, 0) == 0
    assert sub(2.5, 1.5) == 1.0
    