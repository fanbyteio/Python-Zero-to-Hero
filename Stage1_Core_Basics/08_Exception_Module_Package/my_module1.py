__all__ = ['test_a']

def test(a, b):
    print(a + b)

def test_a():
    print('test_A')

def test_b():
    print('test_b')

if __name__ == '__main__':
    test(1,2)
    test_a()
    test_b()