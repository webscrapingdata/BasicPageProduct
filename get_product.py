def get_product(data:str) -> str:
    """Get the product name from the data string.

    Args:
        data (str): The HTML string.

    Returns:
        str: The product name in CSV format.
    """
    pass

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
