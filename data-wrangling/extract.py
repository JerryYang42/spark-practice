# extract data from Sales_Data.csv
# example data
# SalesID,CustomerID,ProductID,Quantity,PricePerUnit,SaleDate
# 1,40,14,5,167.84,2024-01-01
# 2,32,11,5,345.3,2024-01-02

import pandas as pd
def expanded_sales():
    return pd.read_csv('./resources/Expanded_Sales_Data.csv')

def expanded_customers():
    return pd.read_csv('./resources/Expanded_Customers_Data.csv')

def expanded_products():
    return pd.read_csv('./resources/Expanded_Products_Data.csv')

if __name__ == "__main__":
    print(expanded_sales().head())
    print(expanded_customers().head())
    print(expanded_products().head())
