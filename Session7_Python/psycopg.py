import psycopg2

conn = psycopg2.connect("dbname=test2 user=odoo password=odoo host=127.0.0.1 port=5432")

cursor = conn.cursor()

cursor.execute("""
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
	       """)
	       

cursor.execute("""
		select customers.name,customers.email,coalesce(products.name,'-'),coalesce(orders.quantity,0) from customers
		left join orders on  customers.id = orders.customer_id
		left join products on products.id = orders.product_id
		""")
		

data = cursor.fetchall()

cursor.execute("""
            CREATE TABLE leftjoin(
                customer_name varchar(100),
                customer_email varchar(100),
                product_name varchar(100),
                orders_quantity int)
            """)

sql1 = 'INSERT INTO leftjoin(customer_name,customer_email,product_name,orders_quantity) values (%s,%s,%s,%s)'
for row in data:   
	print(row)         
	cursor.execute(sql1,row)
	   	
cursor.execute("""
		select products.name from orders
		right join products on products.id = orders.id
		where orders.id is null
		""")
		
data1 = cursor.fetchall()

cursor.execute("""
            CREATE TABLE rightjoin(
              product_name varchar(100))
            """)

sql1 = 'INSERT INTO rightjoin(product_name) values (%s)'
for row in data1:   
	print(row)         
	cursor.execute(sql1,row)

cursor.execute("""
		select customers.name,orders.product_id,products.price*orders.quantity from products
		inner join orders on  orders.product_id = products.id
		inner join customers on customers.id = products.id
		where products.price > 50""")
		
data2 = cursor.fetchall()

cursor.execute("""
            CREATE TABLE innerjoin(
              customer_name varchar(100),
              product_id int,
              total_price int)
            """)

sql1 = 'INSERT INTO innerjoin(customer_name,product_id,total_price) values (%s,%s,%s)'
for row in data2:   
	print(row)         
	cursor.execute(sql1,row)
      
conn.commit()
conn.close()
