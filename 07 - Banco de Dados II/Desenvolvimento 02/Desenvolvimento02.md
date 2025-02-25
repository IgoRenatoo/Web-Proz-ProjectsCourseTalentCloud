# 📜 Desenvolvimento 02

## 🎯 Descrição do Projeto 

Crie um banco de dados, adicione tabelas e determine quais são os atributos de cada uma. 
- Execute um trigger que se relacione com algum comando, como insert, select, delete ou update.

## 🛠️ Resolução

```sql
DROP DATABASE proz_db2_desen2;
CREATE DATABASE proz_db2_desen2;
USE proz_db2_desen2;

CREATE TABLE vehicle (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL
);

INSERT INTO vehicle (name) VALUES('Motorcycle'), ('Car');

CREATE TABLE user (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	age INT NOT NULL,
    vehicle_id INT NOT NULL,
    FOREIGN KEY (vehicle_id) REFERENCES vehicle(id)
);

CREATE TABLE user_log (
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_user INT NOT NULL,
	action VARCHAR(30) NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (id_user) REFERENCES user(id)
);

DELIMITER $$
	CREATE TRIGGER after_insert_user									-- Cria ação de inserir dados na tabela user_log
		AFTER INSERT ON user
		FOR EACH ROW
		BEGIN
			INSERT INTO user_log (id_user, action) VALUES (NEW.id, 'INSERT');
		END $$
DELIMITER ;

DELIMITER $$
	CREATE TRIGGER before_update_user									-- Cria ação de inserir dados na tabela user_log
    BEFORE UPDATE ON user
    FOR EACH ROW
    BEGIN
		INSERT INTO user_log (id_user, action) VALUES (OLD.id, 'UPDATE');
	END $$
DELIMITER ;

INSERT INTO user (name, age, vehicle_id) VALUES('Teste1', 28, 1);
INSERT INTO user (name, age, vehicle_id) VALUES('Teste2', 32, 2);
INSERT INTO user (name, age, vehicle_id) VALUES('Teste3', 54, 1);

SELECT * FROM user;

CREATE VIEW user_and_vehicle AS 										-- Cria uma tabela de visualização.
	SELECT user.*, vehicle.name AS vehicle_name FROM user 
		INNER JOIN vehicle ON user.vehicle_id = vehicle.id				-- Exibi usuários com veículo registrados que contém na tabela de veículos.
			ORDER BY user.id;
        
SELECT * FROM user_and_vehicle;


SET GLOBAL event_scheduler = ON; 										-- Ativar o agendador de eventos

CREATE EVENT update_vehicle_after_5s									-- Cria evento de atualização após 5s rodar a query.
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 5 SECOND
DO
    UPDATE user SET vehicle_id = CASE WHEN vehicle_id = 1 THEN 2 ELSE 1 END WHERE id = 3;
    
SELECT * FROM user_log;
```
