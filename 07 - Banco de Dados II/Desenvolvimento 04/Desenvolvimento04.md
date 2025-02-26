# 📜 Desenvolvimento 04

## 🎯 Descrição do Projeto 

Uma loja tem um banco de dados que contém todo o controle de vendas de produtos e de cadastro de clientes. 

- Crie uma função para somar todos os clientes que foram cadastrados na loja durante um dia.

## 🛠️ Resolução

```sql
DROP DATABASE proz_db2_desen4;
CREATE DATABASE proz_db2_desen4;
USE proz_db2_desen4;

CREATE TABLE users (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	age INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO users (name, age)
	VALUES
		('João Marquês', 54),
		('Maria Rosário', 38),
        ('Igor Oliver', 27);
;


DELIMITER $$
	CREATE FUNCTION sum_register_users()
		RETURNS INT
		DETERMINISTIC
		BEGIN
			DECLARE quantity_registers INT;
            SELECT COUNT(*) INTO quantity_registers FROM users;
            RETURN quantity_registers;
		END $$
DELIMITER ;


SELECT sum_register_users();
```
