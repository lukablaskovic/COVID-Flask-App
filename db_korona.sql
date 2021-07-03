DROP DATABASE IF EXISTS db_korona;
CREATE DATABASE db_korona;
USE db_korona;
DROP TABLE IF EXISTS test;
CREATE TABLE test(
	test_id SERIAL AUTO_INCREMENT,
    datum_testiranja DATE NOT NULL,
    zarazen BOOLEAN,
    CONSTRAINT test_pk PRIMARY KEY (test_id)
);

DROP TABLE IF EXISTS osoba;
CREATE TABLE osoba(
osoba_id SERIAL AUTO_INCREMENT,
ime VARCHAR(30) NOT NULL,
prezime VARCHAR(40) NOT NULL,
OIB CHAR(11) NOT NULL UNIQUE,
grad VARCHAR(25) NOT NULL,
test_id INTEGER NOT NULL REFERENCES test(test_id),
CONSTRAINT osoba_pk PRIMARY KEY (osoba_id)
);

INSERT INTO test (test_id,datum_testiranja, zarazen) VALUES
	(1,str_to_date('14.5.2020','%d.%m.%Y'),1),
	(2,str_to_date('20.8.2021','%d.%m.%Y'),0),
	(3,str_to_date('30.1.2021','%d.%m.%Y'),1),
	(4,str_to_date('18.4.2021','%d.%m.%Y'),1),
	(5,str_to_date('2.2.2021','%d.%m.%Y'),0);

INSERT INTO osoba (osoba_id,ime,prezime,OIB,grad,test_id) VALUES
	(11,'Petar','Perić',15284750804,'Pula',1),
    (12,'Ivan','Ivić',85476932154,'Karlovac',2),
    (13,'Sanja','Sanjić',62958415263,'Vinkuran',3),
    (14,'Saša','Radolović',02154823561,'Pula',4),
    (15,'Slavko','Slavan',00581479652,'Rijeka',5);
    
DROP VIEW IF EXISTS podaci;
CREATE VIEW podaci AS
	(SELECT test_id,ime,prezime,OIB,grad,datum_testiranja,zarazen FROM osoba
	NATURAL JOIN test);
    
SELECT * FROM podaci;