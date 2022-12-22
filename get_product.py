from bs4 import BeautifulSoup




def get_product(data:str) -> str:
    """Get the product name from the data string.

    Args:
        data (str): The HTML string.

    Returns:
        str: The product name in CSV format.
    """
    soup=BeautifulSoup(open('html/product1.html'),'html.parser')

    names=soup.findAll(name='h3',attrs={'class':'name'})

    prices=soup.findAll(name='p',attrs={'class':'price'})

    descriptions=soup.findAll(name='p',attrs={'class':'description'})
    product_csv='Product Name,Product Price,Product Description\n'
    for i in range(len(names)):
        product_csv+=f'{names[i].get_text()} {prices[i].get_text()} {descriptions[i].get_text()} \n'
    return product_csv
   

def save_product(product:str) -> None:
    """Save the product name to the CSV file.

    Args:
        product (str): The product name in CSV format.
    """
    pass

# Open the file and read the HTML string
with open('html/product1.html', 'r') as f:
    data = f.read()
    # Get the product name in CSV format
    product_csv=get_product(data) 
    # Save the product name to the CSV file
    save_product(product_csv) 
