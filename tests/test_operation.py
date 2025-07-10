## Imprt both addition ands subtraction functions from math_operations module
from src.math_operations import add, sub

## Now we'll run the test cases
def test_add():
    assert add(2, 3) == 5
    assert add(-1,1) == 0
    assert add(0, 0) == 0   

def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 0) == 0
    assert sub(-1, -1) == 0
    assert sub(10, 5) == 5