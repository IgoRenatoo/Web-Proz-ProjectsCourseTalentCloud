# 📜 Desenvolvimento 01 

## 🎯 Descrição do Projeto 

Desenvolva um banco de dados e relacione tabelas através de chaves estrangeiras ou nomes de colunas iguais. Siga as instruções:
- Crie uma base de dados com tabelas;
- Cada tabela, adicione atributos e dados;
- Utilize os comandos Joins para realizar consultas nas tabelas. 

## 🛠️ Resolução

```sql
DROP DATABASE proz_db2_desen1;
CREATE DATABASE proz_db2_desen1;
USE proz_db2_desen1;

CREATE TABLE vehicle (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL
);

INSERT INTO vehicle (name) VALUES
	('Motorcycle'),
  ('Car')
;

CREATE TABLE user (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	age INT NOT NULL,
    vehicle_id INT NOT NULL,
    FOREIGN KEY (vehicle_id) REFERENCES vehicle(id)
);

INSERT INTO user (name, age, vehicle_id) VALUES('Teste1', 28, 1);
INSERT INTO user (name, age, vehicle_id) VALUES('Teste2', 32, 2);
INSERT INTO user (name, age, vehicle_id) VALUES('Teste3', 54, 1);

SELECT user.*, vehicle.name AS vehicle_name FROM user 
	INNER JOIN vehicle ON user.vehicle_id = vehicle.id
		ORDER BY user.id;
```

