DROP TABLE IF EXISTS 'shop';
DROP INDEX IF EXISTS 'sqlite_autoindex_shop_1';
DROP TABLE IF EXISTS 'product';
DROP INDEX IF EXISTS 'sqlite_autoindex_product_1';
DROP TABLE IF EXISTS 'warehouse';
DROP INDEX IF EXISTS 'sqlite_autoindex_warehouse_1';
DROP TABLE IF EXISTS 'worker';
CREATE TABLE shop (
id INTEGER PRIMARY KEY,
name VARCHAR(255) UNIQUE,
balance FLOAT NOT NULL);
INSERT INTO 'shop' VALUES(1,'пятерочка',31);
INSERT INTO 'shop' VALUES(2,'перекресток',133);
null;
CREATE TABLE product (
id INTEGER PRIMARY KEY,
name VARCHAR(255) UNIQUE,
price FLOAT NOT NULL);
INSERT INTO 'product' VALUES(1,'молоко',100);
INSERT INTO 'product' VALUES(2,'хлеб',25);
INSERT INTO 'product' VALUES(3,'сыр',30);
null;
CREATE TABLE warehouse (
shop_id INTEGER REFERENCES shop (id),
product_id INTEGER REFERENCES product (id),
quantity INTEGER NOT NULL,
PRIMARY KEY (shop_id, product_id));
INSERT INTO 'warehouse' VALUES(1,1,20);
INSERT INTO 'warehouse' VALUES(1,2,10);
INSERT INTO 'warehouse' VALUES(2,1,30);
null;
CREATE TABLE worker (
worker_id INTEGER PRIMARY KEY,
shop_id INTEGER REFERENCES product (id),
name VARCHAR(255),
salary INTEGER NOT NULL,
position VARCHAR(255));
INSERT INTO 'worker' VALUES(1,1,'Дима',15000,'Кассир');
INSERT INTO 'worker' VALUES(2,1,'Женя',30000,'Менеджер');
INSERT INTO 'worker' VALUES(3,1,'Катя',40000,'Администратор');
INSERT INTO 'worker' VALUES(4,2,'Антон',17000,'Кассир');
INSERT INTO 'worker' VALUES(5,2,'Варя',29000,'Менеджер');
INSERT INTO 'worker' VALUES(6,2,'Андрей',42000,'Администратор');
INSERT INTO 'worker' VALUES(7,2,'Павел',12000,'Уборщик');
