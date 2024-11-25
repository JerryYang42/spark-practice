from extract import expanded_customers, expanded_products, expanded_sales
from combine import combine_data
# explore the combined dataset

combined_data = combine_data()
# number of products brought from each category by each customer?


# Question: total sales by each customer
total_sales_by_each_customer = combined_data.groupby('CustomerID').apply(lambda x: (x['Quantity'] * x['PricePerUnit']).sum()).reset_index(name='total')
print(total_sales_by_each_customer.sort_values(by='total', ascending=False))

# Question: which category of products are most sold?
most_sold_category = combined_data.groupby('Category').apply(lambda x: (x['Quantity'] * x['PricePerUnit']).sum()).reset_index(name='total')
print(most_sold_category.sort_values(by='total', ascending=False))