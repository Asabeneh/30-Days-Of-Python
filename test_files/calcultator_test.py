def plus(a, b):
    return a + b


def test_plus():
    assert plus(10, 10) == 20


if __name__ == '__main__':
    test_plus()