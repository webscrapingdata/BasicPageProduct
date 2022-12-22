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
        product_csv+=f'{names[i].get_text()}, {prices[i].get_text()}, {descriptions[i].get_text()}\n'
    return product_csv
   

    # list of products
    products = ['Product Name,Product Price,Product Description']

    soup = BeautifulSoup(markup=data, features='html.parser')
    # get div tags
    product_tags = soup.find_all('div', class_='product')
    for div in product_tags:
        # get product name
        product_name = div.h3.text
        # get price
        price = div.find('p', class_='price').text
        # get description
        description = div.find('p', class_='description').text

        products.append(','.join([product_name, price, description]))
    
    # convert to str
    products_str = '\n'.join(products)
    return products_str


def save_product(product:str) -> None:
    """Save the product name to the CSV file.

    Args:
        product (str): The product name in CSV format.
    """

    with open('product_csv.csv','w') as f:
        f.write(product)
    

    with open('products.csv', 'w') as f:
        f.write(product)


# Open the file and read the HTML string
with open('html/product1.html', 'r') as f:
    data = f.read()

# Get the product name in CSV format
product_csv=get_product(data) 
# Save the product name to the CSV file
save_product(product_csv) 
