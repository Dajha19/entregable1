import pandas as pd
import numpy as np
import random
from faker import Faker

# Inicializar Faker para generar datos falsos
fake = Faker()

# Parámetros para los datos
num_users = 1000
num_products = 100
num_sales = 5000

# Generar datos de usuarios
user_ids = [i for i in range(1, num_users + 1)]
user_names = [fake.name() for _ in range(num_users)]
user_emails = [fake.email() for _ in range(num_users)]

users_df = pd.DataFrame({
    'user_id': user_ids,
    'user_name': user_names,
    'user_email': user_emails
})

# Guardar archivo CSV de usuarios
users_df.to_csv('users.csv', index=False)

# Generar datos de productos
product_ids = [i for i in range(1, num_products + 1)]
product_names = [fake.word() for _ in range(num_products)]
product_prices = [round(random.uniform(5.0, 500.0), 2) for _ in range(num_products)]

products_df = pd.DataFrame({
    'product_id': product_ids,
    'product_name': product_names,
    'product_price': product_prices
})

# Guardar archivo CSV de productos
products_df.to_csv('products.csv', index=False)

# Generar datos de ventas
sales = []
for _ in range(num_sales):
    sale_id = _ + 1
    user_id = random.choice(user_ids)
    product_id = random.choice(product_ids)
    quantity = random.randint(1, 5)
    total_price = quantity * products_df.loc[products_df['product_id'] == product_id, 'product_price'].values[0]
    sales.append([sale_id, user_id, product_id, quantity, round(total_price, 2)])

sales_df = pd.DataFrame(sales, columns=['sale_id', 'user_id', 'product_id', 'quantity', 'total_price'])

# Guardar archivo CSV de ventas
sales_df.to_csv('sales.csv', index=False)

print("Archivos CSV generados exitosamente.")

