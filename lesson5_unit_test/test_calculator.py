from calculator import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-1) == 1
    assert square(-2) == 4

def test_zero():
    assert square(0) == 0

if __name__ == "__main__":
    main()
