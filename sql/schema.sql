CREATE TABLE Customers(
	customer_id INT PRIMARY KEY,
	country VARCHAR(30)
);

CREATE TABLE Products(
	stockcode VARCHAR(20) PRIMARY KEY,
	description TEXT
);

CREATE TABLE Transactions(
    transaction_id SERIAL PRIMARY KEY,
	invoice VARCHAR(20),
	customer_id INT REFERENCES Customers(customer_id),
	stockcode VARCHAR(20) REFERENCES Products(stockcode),
	quantity INT,
	price DECIMAL(10, 2),
	invoiceDate TIMESTAMP
);