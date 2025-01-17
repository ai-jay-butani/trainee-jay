import psycopg2

conn = psycopg2.connect("dbname=test2 user=odoo password=odoo host=127.0.0.1 port=5432")

print(conn)

cursor = conn.cursor()

'''cursor.execute("""
            CREATE TABLE customers (
                id serial PRIMARY KEY,
                name varchar(100),
                email varchar(100))
            """)
            
cursor.execute("""
            CREATE TABLE products (
                id serial PRIMARY KEY,
                name varchar(100),
                price int)
            """)
            
cursor.execute("""
            CREATE TABLE orders (
                id serial PRIMARY KEY,
                customer_id int,
                product_id int,
                quantity int,
                order_date Date,
            	foreign key (customer_id) references customers(id),
            	foreign key (product_id) references products(id))
            """)
            
cursor.execute("""
		INSERT INTO customers(name,email) values ('Alice','alice@email.com'),('Bob','bob@email.com'),('Charlie','charlie@email.com')
	       """)
	     

cursor.execute("""
		INSERT INTO products(name,price) values ('Mobile',30),('Laptop',70),('TV',90)
	       """)  
	       
cursor.execute("""
		INSERT INTO orders(customer_id,product_id,quantity,order_date) values (1,2,1,'2025-01-01'),(2,1,3,'2025-01-02')
	       """)'''
	       

cursor.execute("""
		select customers.name,customers.email,coalesce(orders.quantity,0) from customers 
		left join products on customers.id = products.id
		left join orders on  customers.id = orders.customer_id
		""")

data = cursor.fetchall()

for r in data:
	print(r)
	

cursor.execute("""
		select products.name from orders
		right join products on products.id = orders.id
		where orders.id is null
		""")
		
data1 = cursor.fetchall()
print(data1)

cursor.execute("""
		select customers.name,orders.id,products.price*orders.quantity from products
		inner join orders on  orders.product_id = products.id
		inner join customers on customers.id = products.id
		where products.price > 50""")
		
data2 = cursor.fetchall()
print(data2)
      
conn.commit()
conn.close()
