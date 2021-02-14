CREATE DATABASE fly;
CREATE DATABASE hotel;
CREATE DATABASE account;

\c fly;

CREATE TABLE IF NOT EXISTS booking(
  id SERIAL PRIMARY KEY,
  client_name VARCHAR (50),
	fly_number VARCHAR (50),
	fly_from VARCHAR (50),
	fly_to VARCHAR (50),
	fly_date DATE
);

\c hotel;

CREATE TABLE IF NOT EXISTS booking(
  id SERIAL PRIMARY KEY,
  client_name VARCHAR (50),
	hotel_name VARCHAR (50),
	arrival DATE,
	departure DATE
);

\c account;
CREATE TABLE IF NOT EXISTS account(
  id SERIAL PRIMARY KEY,
  client_name VARCHAR (50),
	amount numeric CHECK(amount > 0)
);

INSERT INTO account (client_name, amount)
VALUES ('Nik', 1000);
