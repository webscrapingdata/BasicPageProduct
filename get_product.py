from bs4 import BeautifulSoup
import csv

def get_product(data:str) -> list:
    """Get the product name from the data string.

    Args:
        data (str): The HTML string.

    Returns:
        str: The product name in CSV format.
    """
    soup = BeautifulSoup(data, features="html.parser")
    prduct_name = list(map(lambda x: x.text, soup.find_all('h3', class_='name')))
    price_list = list(map(lambda x: x.text, soup.find_all('p', class_='price')))
    description = list(map(lambda x: x.text, soup.find_all('p', class_='description')))

    return zip(
        prduct_name,
        price_list,
        description
    )
    

def save_product(product: list) -> None:
    """Save the product name to the CSV file.

    Args:
        product (str): The product name in CSV format.
    """
    with open('h1_tag.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # writer.writerow(header)
        for i in product:
            writer.writerow(i)

# Open the file and read the HTML string
with open('html/product1.html', 'r') as f:
    data = f.read()
    # Get the product name in CSV format
    product_csv=get_product(data) 
    # Save the product name to the CSV file
    save_product(product_csv) 
