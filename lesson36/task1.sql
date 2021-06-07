CREATE TABLE university.CUSTOMER(
   ID   INT              NOT NULL,
   NAME VARCHAR (20)     NOT NULL,
   AGE  INT              NOT NULL,
   ADDRESS  CHAR (25) ,
   SALARY   DECIMAL (18, 2),
   PRIMARY KEY (ID)
);

ALTER TABLE university.CUSTOMER
RENAME TO university.CUSTOMERS;

ALTER TABLE university.CUSTOMERS
ADD Email varchar(255);

INSERT INTO university.CUSTOMERS
	(ID, Name, AGE, Address, SALARY, Email)
VALUES
	(1, 'Cardinal', 30, 'Skagen 21', 20000, 'asd@asd.com'),
    (2, 'John', 40, 'Skagen 21', 40000, 'asd2@asd.com'),
    (3, 'Cat', 34, 'Stockholm', 20000, 'asd3@asd.com');

UPDATE university.CUSTOMERS
SET SALARY = 50000, Address= 'Frankfurt'
WHERE ID = 3;

DELETE FROM university.CUSTOMERS WHERE ID=2;