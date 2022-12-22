from get_product import get_product

def test_get_product():
    with open('html/product1.html', 'r') as f:
        data = f.read()
        output = get_product(data)
        expect = 'Product Name,Product Price,Product Description\nProduct 1,$10.99,This is a description of product 1\nProduct 2,$20.00,This is a description of product 2'
        assert output == expect, f'Wrong output'
        