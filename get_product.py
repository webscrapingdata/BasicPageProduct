from bs4 import BeautifulSoup

def get_product(data:str) -> str:
    """Get the product name from the data string.

    Args:
        data (str): The HTML string.

    Returns:
        str: The product name in CSV format.
    """

    soup = BeautifulSoup(data, 'html.parser')

    names = soup.findAll(name='h3', attrs={'class':'name'})
    prices = soup.findAll(name='p',attrs={'class':'price'})
    descriptions = soup.findAll(name='p', attrs={'class':'description'})
    
    format_csv = "Product Name,Product Price,Product Description\n"

    for name, price, description in zip(names, prices, descriptions):
        format_csv += f"{name.get_text()},{price.get_text()},{description.get_text()}\n"

    return format_csv.strip()

def save_product(product:str) -> None:
    """Save the product name to the CSV file.

    Args:
        product (str): The product name in CSV format.
    """
    with open('product.csv', 'w') as f:
        f.write(product)

# Open the file and read the HTML string
with open('html/product1.html', 'r') as f:
    data = f.read()
    # Get the product name in CSV format
    product_csv=get_product(data) 
    # Save the product name to the CSV file
    save_product(product_csv)
# print(product_csv)