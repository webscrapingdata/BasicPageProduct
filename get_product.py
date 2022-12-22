from bs4 import BeautifulSoup
def get_product(data:str) -> str:
    """Get the product name from the data string.

    Args:
        data (str): The HTML string.

    Returns:
        str: The product name in CSV format.
    """
    f = open("html/product1.html").read()
    soup = BeautifulSoup(f,"html.parser")

    names =  soup.findAll(name="h3",attrs={"class":"name"})
    prices = soup.findAll(name="p",attrs={"class":"price"})
    des = soup.findAll(name="p",attrs={"class":"description"})

    st = "Product Name,Product Price,Product Description\n"
    for i in range(len(names)):
        st += f'{names[i].text},{prices[i].text},{des[i].text}\n'
    return st[:-1]


def save_product(product:str) -> None:
    """Save the product name to the CSV file.

    Args:
        product (str): The product name in CSV format.
    """
    with open("product.csv", 'w') as f:
        f.write(product)
# Open the file and read the HTML string
with open('html/product1.html', 'r') as f:
    data = f.read()
    # Get the product name in CSV format
    product_csv=get_product(data) 
    # Save the product name to the CSV file
    save_product(product_csv) 
