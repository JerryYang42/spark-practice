from extract import expanded_customers, expanded_products, expanded_sales

def clean_sales():
    sales = expanded_sales()
    # data types
    print(sales.describe())
    # missing values / nulls
    print(sales.isnull().sum())
    # duplicates
    print(sales.duplicated().sum())
    # sales['SaleDate'] = pd.to_datetime(sales['SaleDate'])
    # return sales

def clean_customers():
    customers = expanded_customers()
    # data types
    print(customers.describe())
    # missing values / nulls
    print(customers.isnull().sum())
    # duplicates
    print(customers.duplicated().sum())
    # return customers

def clean_products():
    products = expanded_products()
    # data types
    print(products.describe())
    # missing values / nulls
    print(products.isnull().sum())
    # duplicates
    print(products.duplicated().sum())
    # return products

if __name__ == "__main__":
    clean_sales()
    clean_customers()
    clean_products()