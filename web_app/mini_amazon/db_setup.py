"""
This file is used to populate the database that is created by Django.
"""


import db_utils

conn, cursor = db_utils.connect_db()

# clear all tables
query = f"""
    TRUNCATE  
    mini_amazon_orderproducttuple,
    mini_amazon_warehousestock, 
    mini_amazon_order, 
    mini_amazon_product
    CASCADE;

    DELETE FROM mini_amazon_warehouse;
"""
db_utils.execute_and_commit(query, conn, cursor)

# create some products
query = f"""
    INSERT INTO mini_amazon_product(name, description, price, seller)
    VALUES
    ('productA', 'A', 1.00, 'Alice'),
    ('productB', 'B', 2.00, 'Bob'),
    ('productC', 'C', 3.00, 'Cassie'),
    ('productD', 'D', 4.56, 'Drew');
"""
db_utils.execute_and_commit(query, conn, cursor)

# create some warehouses
query = f"""
    INSERT INTO mini_amazon_warehouse(location_x, location_y)
    VALUES
    (1, 1),
    (2, 2),
    (3, 3);
"""
db_utils.execute_and_commit(query, conn, cursor)

query = f"""
    SELECT 
        mini_amazon_warehouse.id AS warehouse_id, 
        mini_amazon_product.id AS product_id
    FROM mini_amazon_warehouse, mini_amazon_product
"""
cursor.execute(query)
rows = cursor.fetchall()
for warehouse_id, product_id in rows:
    query = f"""
        INSERT INTO mini_amazon_warehousestock(warehouse_id, product_id, num_product) 
        VALUES({warehouse_id}, {product_id}, 0);
    """
    db_utils.execute_and_commit(query, conn, cursor)


cursor.close()
