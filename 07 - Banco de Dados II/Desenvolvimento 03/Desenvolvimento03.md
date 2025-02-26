# 📜 Desenvolvimento 03 

## 🎯 Descrição do Projeto 

Uma empresa de vendas tem um banco de dados com informações sobre os seus produtos.

Ela precisa criar um relatório que faça um levantamento diário da quantidade de produtos comprados por dia. 

- Crie um procedure para agilizar esse processo.

## 🛠️ Resolução

```sql
DROP DATABASE proz_db2_desen3;
CREATE DATABASE proz_db2_desen3;
USE proz_db2_desen3;

CREATE TABLE users (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
	create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO users (name, age)
	VALUES	('Igor', 22),
			('Emily', 21),
			('TchanTchanTchan', 19)
;


CREATE TABLE products (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(6,2) NOT NULL DEFAULT 0,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO products (name, price)
	VALUES	('Placa de Vídeo', 4500.00),
			('Placa Mãe', 569.00),
            ('Monitor', 899.00),
            ('Teclado', 68.00),
            ('Mouse', 27.99)
;


CREATE TABLE purchase_orders (
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_user INT NOT NULL,    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_user) REFERENCES users(id) ON DELETE CASCADE
);


CREATE TABLE purchase_order_items (
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_order INT NOT NULL,
	id_product INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (id_order) REFERENCES purchase_orders(id) ON DELETE CASCADE,
    FOREIGN KEY (id_product) REFERENCES products(id) ON DELETE CASCADE
);


INSERT INTO purchase_orders (id_user) VALUES(3);
SET @LAST_ID = LAST_INSERT_ID();

INSERT INTO purchase_order_items (id_order, id_product, quantity) 
	VALUES	(@LAST_ID, 3, 1),
			(@LAST_ID, 1, 1),
            (@LAST_ID, 5, 2)
;


INSERT INTO purchase_orders (id_user) VALUES(1);
SET @LAST_ID = LAST_INSERT_ID();

INSERT INTO purchase_order_items (id_order, id_product, quantity) 
	VALUES	(@LAST_ID, 1, 4),
			(@LAST_ID, 2, 3),
            (@LAST_ID, 3, 1)
;

-- Exibir informações referente as ordens de compra.
SELECT purchase_orders.id as number_order, users.id as user_id, users.name as user_name, purchase_order_items.id_product, products.name, purchase_order_items.quantity
	FROM purchase_orders
    JOIN users ON purchase_orders.id_user = users.id
    JOIN purchase_order_items ON purchase_order_items.id_order = purchase_orders.id
    JOIN products ON purchase_order_items.id_product = products.id ORDER BY number_order ASC
;

-- Procedure para exibir todas as compras realizadas no dia.
DELIMITER $$
	CREATE PROCEDURE getTotalItemsSoldOnDay(IN sale_date DATE)
		BEGIN
			SELECT DATE(purchase_orders.created_at) as date_purchase, SUM(purchase_order_items.quantity) as quantity_products
				FROM purchase_order_items
				JOIN purchase_orders ON purchase_orders.id = purchase_order_items.id_order
					WHERE DATE(purchase_orders.created_at) = CURDATE()
					GROUP BY purchase_orders.created_at
			;
		END $$
DELIMITER ;


CALL getTotalItemsSoldOnDay(CURDATE());


SELECT * FROM users;
SELECT * FROM purchase_orders;
SELECT * FROM purchase_order_items;
SELECT * FROM products ORDER BY price DESC;
```
