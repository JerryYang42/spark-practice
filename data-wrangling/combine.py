from extract import expanded_customers, expanded_products, expanded_sales

def combine_data():
    sales = expanded_sales()
    customers = expanded_customers()
    products = expanded_products()
    # merge sales and customers
    sales_customers = sales.merge(customers, how='left', left_on='CustomerID', right_on='CustomerID')
    # merge sales_customers and products
    sales_customers_products = sales_customers.merge(products, how='left', left_on='ProductID', right_on='ProductID')
    return sales_customers_products

def clean_combined_data():
    data = combine_data()
    # data types
    print(data.describe())
    # missing values / nulls
    print(data.isnull().sum())
    # duplicates
    print(data.duplicated().sum())
    # return data

if __name__ == "__main__":
    print(combine_data().head())
    print(combine_data().shape)
    clean_combined_data()