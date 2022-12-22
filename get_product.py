from bs4 import BeautifulSoup
import csv

def get_product(data:str) -> str:
    """Get the product name from the data string.

    Args:
        data (str): The HTML string.

    Returns:
        str: The product name in CSV format.
    """
    soup = BeautifulSoup(data, 'html.parser')
    dev_tags = soup.find_all('div', class_='product')
    product = []
    for i in dev_tags:
        # product.append([i.h3.text])
        p1_tag = i.find_all('p', class_='price')
        p2_tag = i.find_all('p', class_='description')
        product.append([i.h3.text,p1_tag[0].text,p2_tag[0].text])
    # print(product)
    return product

def save_product(product:str) -> None:
    """Save the product name to the CSV file.

    Args:
        product (str): The product name in CSV format.
    """
    header = ['Product Name', 'Product Price', 'Product Description']

    with open('product.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(product)

# Open the file and read the HTML string
with open('html/product1.html', 'r') as f:
    data = f.read()
    # Get the product name in CSV format
    product_csv=get_product(data) 
    # Save the product name to the CSV file
    save_product(product_csv) 
