SHOW DATABASES;

create database sda_project;

set sql_safe_updates = 0;

use sda_project;

SHOW TABLES;

CREATE TABLE sda_project.categories
(
    cat_id smallint unsigned not null auto_increment,
    cat_name varchar(32) not null,
    cat_desc varchar(64) default 'Brak opisu kategorii',
    primary key (cat_id)
);

DESC sda_project.categories;

CREATE TABLE sda_project.customers 
(
    cus_id SMALLINT(5) UNSIGNED NOT NULL AUTO_INCREMENT,
    cus_name VARCHAR(64) NOT NULL,
    cus_surname VARCHAR(64) NOT NULL,
    cus_phone VARCHAR(9),
    cus_email VARCHAR(8),
    cus_email2 VARCHAR(8),
    PRIMARY KEY (cus_id)
);

ALTER TABLE customers DROP COLUMN cus_email2;
ALTER TABLE customers MODIFY COLUMN cus_email VARCHAR(32) NULL;

DESC sda_project.customers;

CREATE TABLE sda_project.books
(
	bk_id VARCHAR(5) NOT NULL,
	bk_cat_id SMALLINT(5) UNSIGNED NOT NULL,
	bk_name VARCHAR(64) NOT NULL,
	bk_author VARCHAR(64) NOT NULL,
	bk_release VARCHAR(4) NOT NULL,
	bk_publisher VARCHAR(32) NOT NULL,
	PRIMARY KEY (bk_id),
    FOREIGN KEY (bk_cat_id) REFERENCES sda_project.categories(cat_id)
);

DESC sda_project.books;

CREATE TABLE sda_project.rents
(
	rn_id SMALLINT(5) UNSIGNED NOT NULL AUTO_INCREMENT,
	rn_bk_id VARCHAR(5) NOT NULL,
	rn_cus_id SMALLINT(5) UNSIGNED NOT NULL,
	rn_rent_date date NOT NULL,
	PRIMARY KEY (rn_id),
	FOREIGN KEY (rn_bk_id) REFERENCES sda_project.books(bk_id),
	FOREIGN KEY (rn_cus_id) REFERENCES sda_project.customers(cus_id)
);

ALTER TABLE sda_project.rents ADD COLUMN rn_return_date date null;

DESC sda_project.rents;

INSERT INTO sda_project.customers(cus_id, cus_name, cus_surname, cus_phone, cus_email) VALUES (1, 'Adam', 'Nowak', '371980245', 'adam.nowak@email.pl');
INSERT INTO sda_project.customers(cus_id, cus_name, cus_surname, cus_phone, cus_email) VALUES 
(2, 'Ewelina', 'Oczytana', '244908121', NULL),
(3, 'Jakub', 'Mol', '322657100', 'jakub_mol@o3.pl');

DESC sda_project.customers;

INSERT INTO sda_project.categories(cat_id, cat_name, cat_desc) VALUES 
(1, 'Fantastyka', NULL);
INSERT INTO sda_project.categories(cat_id, cat_name, cat_desc) VALUES 
(2, 'Sensacyjne i Kryminały', NULL),
(3, 'Dla dzieci', NULL);

INSERT INTO sda_project.categories
VALUES (4, 'Fantastyka', 'Wielotomowe, epickie dzieła'),
    (5, 'Sensacyjne i Kryminały', 'Dział dla miłośników silnych emocji'),
    (6, 'Naukowe', NULL),
    (7, 'Dla dzieci', 'Coś dla naszych pociech');

INSERT INTO sda_project.books(bk_id, bk_cat_id, bk_name, bk_author, bk_release, bk_publisher) VALUES 
('JP101', 1, 'Inkwyzitor. Przeklęte Krainy', 'Jacek Piekara', '2019', 'Fabryka Słów'),
('SJM01', 1, 'Szklany Tron. Tom 5.5. Wieża świtu', 'Sarah J. Maas', '2018', 'Uroboros'),
('AS210', 1, 'Wiedźmin. Tom 1. Ostatnie życzenie', 'Andrzej Sapkowski', '2014', 'SuperNowa');

INSERT INTO sda_project.books(bk_id, bk_cat_id, bk_name, bk_author, bk_release, bk_publisher) VALUES 
('TF567', 2, 'Bad Mommy. Zła mama', 'Tarryn Fisher', '2017', 'Sine Qua Non'),
('AC989', 2, 'Pajęczyna', 'Agatha Christie', '2013', 'Dolnośląskie'),
('TL367', 2, 'Login', 'Tomasz Lipko', '2019', 'Literackie'),
('WC666', 2, 'Rana', 'Wojciech Chmielarz', '2019', 'Marginesy');

INSERT INTO sda_project.books(bk_id, bk_cat_id, bk_name, bk_author, bk_release, bk_publisher) VALUES 
('RG345', 3, 'Mikołajek. Jak to się zaczęło', 'Rene Goscinny', '2019', 'Znak');

insert into sda_project.rents(rn_id, rn_bk_id, rn_cus_id, rn_rent_date, rn_return_date) values
(null, 'JP101', 1, '2019-05-01', '2019-06-01'),
(null, 'TF567', 1, '2019-06-01', '2019-07-01'),
(null, 'RG345', 1, '2019-07-01', null),
(null, 'SJM01', 2, '2019-07-01', null),
(null, 'JP101', 2, '2019-07-01', '2019-09-01'),
(null, 'WC666', 2, '2019-08-01', '2019-09-01'),
(null, 'WC666', 3, '2019-02-01', '2019-05-01');

-- polecenie do domu z soboty na niedziele
CREATE TABLE sda_project.departments
(
    dep_id          SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    dep_name        VARCHAR(64) NOT NULL UNIQUE,
    dep_location    VARCHAR(128) NOT NULL,
    PRIMARY KEY (dep_id)
);

ALTER TABLE sda_project.departments ADD dep_city VARCHAR(64) NOT NULL;

CREATE TABLE sda_project.employees
(
    ep_id           SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    ep_man_id       SMALLINT UNSIGNED not null,
    ep_dep_id       SMALLINT UNSIGNED,
    ep_name         VARCHAR(64) NOT NULL,
    ep_surname      VARCHAR(64) NOT NULL,
    ep_hire_date    DATE NOT NULL,
    ep_salary       SMALLINT UNSIGNED NOT NULL,
    ep_phone        VARCHAR(9),
    ep_email        VARCHAR(32) NOT NULL UNIQUE,
    PRIMARY KEY (ep_id),
    FOREIGN KEY (ep_dep_id) REFERENCES sda_project.departments(dep_id),
    FOREIGN KEY (ep_man_id) REFERENCES sda_project.employees(ep_id)
);

ALTER TABLE sda_project.employees MODIFY COLUMN ep_man_id SMALLINT UNSIGNED;

INSERT INTO sda_project.departments(dep_id, dep_name, dep_city, dep_location)
VALUES (NULL, 'Alpha', 'Warszawa', 'Ostatnia 10/20'),
    (NULL, 'Beta', 'Warszawa', 'Cukierkowa 65'),
    (NULL, 'Gamma', 'Gdynia', 'Wojska Polskiego 1'),
    (NULL, 'Epsilon', 'Lodz', 'Wektorowa 1/70'),
    (NULL, 'Omega', 'Lodz', 'Zamkowa 23/20');

-- Usuwanie tabeli
Drop table sda_project.employees;

-- Department 1
INSERT INTO sda_project.employees
VALUES (NULL, NULL, 1, 'Jan', 'Boss', '2018-01-01', 15000, '154978100', 'jan_boss@alpha.pl');
-- Department 2
INSERT INTO sda_project.employees
VALUES (NULL, 1, 2, 'Ewelina', 'Wice', '2018-02-01', 12500, '345890112', 'ewelina_wice@beta.pl');
INSERT INTO sda_project.employees
VALUES (NULL, 1, 2, 'Agnieszka', 'Kowalik', '2018-04-01', 12500, '123567455', 'agnieszka_kowalik@beta.pl');
-- Department 3
INSERT INTO sda_project.employees
VALUES (NULL, 3, 3, 'Adam', 'Nowakowski', '2018-07-01', 3500, '234675112', 'adam_nowakowski@gamma.pl');
INSERT INTO sda_project.employees
VALUES (NULL, 3, 3, 'Jakub', 'Nazwisko', '2018-04-01', 3500, '900767433', 'jakub_nazwisko@gamma.pl');
-- Department 4
INSERT INTO sda_project.employees
VALUES (NULL, 2, 4, 'Karolina', 'Polka', '2019-01-01', 3500, '231564786', 'karolina_polka@epsilon.pl');
INSERT INTO sda_project.employees
VALUES (NULL, 5, 4, 'Jakub', 'Drugi', '2019-03-01', 4000, '111222333', 'jakub_drugi@epsilon.pl');
INSERT INTO sda_project.employees
VALUES (NULL, 5, 4, 'Karolina', 'Wierna', '2019-05-01', 5000, '123456980', 'karolina_wierna@epsilon.pl');

-- Ex05_Selects.sql
SELECT * FROM sda_project.customers;

SELECT * FROM sda_project.books LIMIT 3;

SELECT ep_dep_id FROM sda_project.employees;

SELECT DISTINCT ep_dep_id FROM sda_project.employees;

SELECT ep_name AS imie, ep_surname AS nazwisko FROM sda_project.employees;

-- Ex06_OrderBy.sql

SELECT * FROM sda_project.employees ORDER BY ep_surname ASC;

SELECT * FROM sda_project.books ORDER BY bk_release ASC;

SELECT cus_name AS imie, cus_surname AS nazwisko FROM sda_project.customers ORDER BY cus_id ASC;

SELECT * FROM sda_project.rents ORDER BY rn_bk_id ASC, rn_id DESC;

-- Ex07_TxtFunctions.sql

SELECT CONCAT(ep_name, ' ', ep_surname) AS PRACOWNIK FROM sda_project.employees;

SELECT length(dep_location) AS dlugosc FROM sda_project.departments;

SELECT substr(cus_phone, 1, 3) AS 3_pierwsze FROM sda_project.customers;

SELECT upper(bk_name) AS Tytuly FROM sda_project.books;

SELECT substr(dep_location,3, 4) AS wycięta_nazwa FROM sda_project.departments;

-- Ex08_TimeFunctions.sql

select month(rn_rent_date) from sda_project.rents;

select datediff(curdate(), date('1990-04-23')) AS roznica;

select CONCAT(curtime(), ' ', curdate()) AS teraz;

-- Ex09_GroupBy.sql

select MIN(ep_salary), MAX(ep_salary) from sda_project.employees;

select AVG(bk_release) from sda_project.books;

select ep_dep_id, count(*) from sda_project.employees group by ep_dep_id;

select rn_return_date, count(*), rn_bk_id from sda_project.rents group by rn_bk_id  having count(rn_return_date) > 1;

-- Ex10_Where.sql

select ep_name, ep_surname, ep_salary FRom sda_project.employees where ep_salary > 1000 ;

select bk_name FRom sda_project.books where bk_name != 'J%'; -- not like 'J%'

select bk_name FRom sda_project.books where bk_author = 'Andrzej Sapkowski' or  bk_publisher = 'Dolnośląskie';

select rn_bk_id FRom sda_project.rents where rn_rent_date != '2019-03-01';

select rn_bk_id FRom sda_project.rents where month(rn_rent_date) between 5 and 7 and year(rn_rent_date) = '2019';

-- 11

-- Ex12_SubQuery

select bk_name,	bk_release from sda_project.books bk1 where bk1.bk_release > (select avg(bk_release) from sda_project.books bk2);

select * from sda_project.employees e1 where e1.ep_salary > (select e2.ep_salary from sda_project.employees e2 where e2.ep_id = e1.ep_man_id);

select * from sda_project.employees;

update sda_project.employees
	set ep_hire_date = '2019-01-01'
where 1=1;

select * from sda_project.departments;

update sda_project.departments
	set dep_name = 'Gamma v2',
		dep_city = 'Pabianice'
where dep_id = 5;

select ep_id, ep_salary from sda_project.employees;

update sda_project.employees
	set ep_salary = ep_salary * 1.1
where 1=1;

-- Ex13_Updates

select * from sda_project.departments;

update sda_project.departments
	set dep_name = 'Ajin'
where dep_name = 'Alpha';

select * from sda_project.customers;

update sda_project.customers
	set cus_phone = '123456789'
where cus_id = '3';

select * from sda_project.employees;

update sda_project.employees
	set ep_salary = ep_salary * 1.1
where ep_man_id = '2' or ep_dep_id = '4';

select * from sda_project.rents;

update sda_project.rents
	set rn_rent_date = '2019-10-10'
where rn_rent_date is null;

-- Ex14_Indexes;

-- Zad 01: Załóż indeks pk_emp_idx na kolumnie ep_id w tabeli employees;

CREATE INDEX pk_emp_idx
ON sda_project.employees(ep_id);

-- Zad 02: Załóż indeks full_name_cust_idx na koumnach cus_name, cust_surname w tabeli customers.

CREATE INDEX full_name_cust_idx
ON sda_project.customers(cus_name, cus_surname); 

-- Zad 03: Załóż unikatowy indeks na rn_bk_id w tabeli rents (Jaki komunikat zwróciła baza danych?)

CREATE UNIQUE INDEX rn_bk_id
ON sda_project.rents(rn_bk_id);

-- Zad 04: Załóż indeks typu FULLTEXT na kolumnie bk_author w tabeli books.

CREATE fulltext index full_id
ON sda_project.books(bk_author); 

explain select*from sda_project.employees;

explain select*from sda_project.employees where ep_id = 3;

explain select*from sda_project.employees where lower(ep_id) = 3;

explain select*from sda_project.employees where ep_surname = 'Boss';

explain select e.ep_name, e.ep_surname, d.dep_name
	from sda_project.employees e
    join sda_project.departments d on d.dep_id = e.ep_dep_id
where e.ep_hire_date like '2019%';

create view emp_dep_2
as select * from sda_project.employees where ep_dep_id = 2;

select *
from emp_dep_2;

-- Ex15_Views

-- Zad 01: Utwórz widoku all_rents wyświetlając imię, nazwisko wypożyczającego oraz nazwę książki którą wypożyczył.

create view all_rents2 as
select cus_name, cus_surname, cus_id, rn_cus_id, bk_id from sda_project.rents r join sda_project.books bk join sda_project.customers c on c.cus_id = r.rn_cus_id;

-- Zad 02: Utwórz widok emp_man_2, który wyświetli pracowników, których menadżerem jest pracownik o ID = 2.

create view emp_man_2 as
select e.ep_name, e.ep_surname from sda_project.employees e where ep_man_id = 2;

-- Zad 03: Utwórz widok, który wyświetli książki o ID zaczynającym się na literę A lub kończacym się zerem.

create view book_id as
select * from sda_project.books bk where bk.bk_id LIKE 'A%' or '%0';

-- Ex16_Functions

-- Zad 01: Napisz funkcję, która zwróci podaną liczbę do potęgi 2.

create function potega (p1 int)
returns int deterministic
	return p1 * p1;
    
select potega (2)as potegaaa;

-- Zad 02: Napisz procedurę, która przyjmuje dwa ciągi znaków i zwraca ich konkatenację.

CREATE PROCEDURE procedura ( IN txt1 VARCHAR(64), in txt2 VARCHAR(64), out txt3 varchar(128))
SELECT COUNT (txt1,txt2) into txt3;

CALL procedura ('rgvsv', 'vwevrbeb');




































