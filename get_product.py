from bs4 import BeautifulSoup

def get_product(data:str) -> str:
    """Get the product name from the data string.

    Args:
        data (str): The HTML string.

    Returns:
        str: The product name in CSV format.
    return "Product Name,Product Price,Product Description\n"+("\n".join([f'{element.h3.text}, {element.p.text}, {element.find(class_="description").text}' for element in BeautifulSoup(data, features="html.parser").find_all(class_="product")]))


def save_product(product:str) -> None:
    """Save the product name to the CSV file.

    Args:
        product (str): The product name in CSV format.
    """
    with open('product.csv', "w") as f: f.write(product)
    return True


# Open the file and read the HTML string
with open('html/product1.html', 'r') as f:
    data = f.read()
    # Get the product name in CSV format
    product_csv=get_product(data)
    # Save the product name to the CSV file
    save_product(product_csv) 
