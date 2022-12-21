from get_product import get_product

def test_get_product():
    with open('html/product1.html', 'r') as f:
        data = f.read()
        output = get_product(data)
        expect = ''
        assert output == expect, f'Wrong output'
        