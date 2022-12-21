# Product Page

## Objective

 The objective of this assignment is to demonstrate the candidate's ability to use Beautiful Soup to parse and extract data from an HTML document.

## Problem

You are given an HTML document containing information about a set of products. Your task is to write a Python script that uses Beautiful Soup to parse the document and extract the following information for each product:

- Product name
- Product price
- Product description

The script should output the extracted information in a CSV file.

## Requirements

- Python 3.6 or higher
- Beautiful Soup 4
- Requests

## Instructions

1. Clone this repository.
2. Create a virtual environment and install the requirements.
3. Extract the product information from the HTML document.
4. Output the extracted information in a CSV file with the following format:

```csv
Product Name,Product Price,Product Description
```

5.Your script should be able to handle any HTML document that follows the same format as the one provided.

## Example

Input:

```html
<html>
  <body>
    <div class="product">
      <h3 class="name">Product 1</h3>
      <p class="price">$10.99</p>
      <p class="description">This is a description of product 1</p>
    </div>
    <div class="product">
      <h3 class="name">Product 2</h3>
      <p class="price">$20.00</p>
      <p class="description">This is a description of product 2</p>
    </div>
  </body>
</html>
```

Output:

```csv
Product Name,Product Price,Product Description
Product 1,$10.99,This is a description of product 1
Product 2,$20.00,This is a description of product 2
```
