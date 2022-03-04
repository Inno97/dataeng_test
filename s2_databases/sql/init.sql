-- Setups the table with some data
CREATE SCHEMA dealership;

CREATE SEQUENCE dealership.customer_sequence
    START WITH 1
    INCREMENT BY 1
    MINVALUE 0
    MAXVALUE 10000
    CYCLE
    CACHE 1;

CREATE SEQUENCE dealership.salesperson_sequence
    START WITH 1
    INCREMENT BY 1
    MINVALUE 0
    MAXVALUE 10000
    CYCLE
    CACHE 1;

CREATE SEQUENCE dealership.car_sequence
    START WITH 1
    INCREMENT BY 1
    MINVALUE 0
    MAXVALUE 10000
    CYCLE
    CACHE 1;
    
CREATE SEQUENCE dealership.transaction_sequence
    START WITH 1
    INCREMENT BY 1
    MINVALUE 0
    MAXVALUE 10000
    CYCLE
    CACHE 1;

CREATE TABLE dealership.Customer (
    Id int NOT NULL,
    Name text,
    CONSTRAINT PK_Customer PRIMARY KEY (Id)
);

CREATE TABLE dealership.Salesperson (
    Id int NOT NULL,
    Name text,
    CONSTRAINT PK_Salesperson PRIMARY KEY (Id)
);

CREATE TABLE dealership.Car (
    Id int NOT NULL,
    ModelName text,
    Manufacturer text,
    SerialNumber text,
    Weight numeric,
    Price numeric,
    CONSTRAINT PK_Car PRIMARY KEY (Id)
);

CREATE TABLE dealership.Transaction (
    Id int NOT NULL,
    CarId int,
    CustomerId int,
    SalespersonId int,
    CustomerPhoneNumber text,
    Date timestamp
);


ALTER TABLE dealership.Transaction ADD CONSTRAINT PK_Customer FOREIGN KEY (CustomerId)
REFERENCES dealership.Customer (Id) MATCH FULL;

ALTER TABLE dealership.Transaction ADD CONSTRAINT PK_Salesperson FOREIGN KEY (SalespersonId)
REFERENCES dealership.Salesperson (Id) MATCH FULL;

ALTER TABLE dealership.Transaction ADD CONSTRAINT PK_Car FOREIGN KEY (CarId)
REFERENCES dealership.Car (Id) MATCH FULL;

-- Add some sample data
INSERT INTO dealership.Customer(Id, Name) 
VALUES
(1, 'Daniel'),
(2, 'Tom'),
(3, 'Harry'),
(4, 'Jill');

INSERT INTO dealership.Salesperson(Id, Name) 
VALUES
(1, 'Bobby'),
(2, 'Tim'),
(3, 'Max'),
(4, 'Xiao Ming');

INSERT INTO dealership.Car(Id, ModelName, Manufacturer, SerialNumber, Weight, Price)
VALUES
(1, 'WRX STI', 'Subaru', 'S000001', 900, 100000),
(2, 'Quattro', 'Audi', 'S000002', 800, 110000),
(3, '911', 'Porsche', 'S000003', 1000, 120000),
(4, 'Impreza', 'Subaru', 'S000004', 1100, 130000),
(5, 'Fulvia', 'Lancia', 'S000005', 800, 60000),
(6, 'Stratos', 'Lancia', 'S000006', 800, 100000),
(7, 'Delta Integrale', 'Lancia', 'S000007', 600, 100000);

INSERT INTO dealership.Transaction(Id, CarId, CustomerId, SalespersonId, CustomerPhoneNumber, Date)
VALUES
(1, 1, 1, 1, '88115566', '2022-01-07 12:05:00'),
(2, 2, 2, 2, '88115566', '2022-01-08 13:06:00'),
(3, 3, 3, 3, '88115566', '2022-01-09 14:07:00'),
(4, 4, 4, 4, '88115566', '2022-01-10 15:08:00'),
(5, 5, 1, 4, '88115566', '2022-02-07 16:09:00'),
(6, 6, 2, 4, '88115566', '2022-02-08 17:10:00'),
(7, 6, 3, 3, '88115566', '2022-02-09 17:10:00');
