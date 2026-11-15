-- every sql function since I started 
CREATE TABLE IF NOT EXISTS Customer(
customer_id INTEGER,
cust_name TEXT PRIMARY KEY,
city TEXT,
grade INTEGER,
Salesman_id INTEGER);
INSERT INTO Customer(customer_id,cust_name,city,grade,Salesman_id)
VALUES
("3002","nick rimando","new york","100","5001"),
("3007","brad davis","new york","200","5001"),
("3005","graham zusi","california","200","5002"),
("3008","julian green","london","300","5002"),
("3004","fabian johnson","paris","300","5006"),
("3009","geoff cameron","berlin","100","5003"),
("3003","jozy altidor","moscow","200","5007"), --lagos
("3001","brad guzan","london","","5005");

--SELECT * FROM Customer 
--WHERE grade > 100 AND IS NOT NULL;
SELECT * 
FROM Customer
WHERE grade > 100
AND grade IS NOT NULL;
SELECT * FROM Customer 
WHERE cust_name LIKE 'g%';
--SELECT * FROM Customer
--SET city TO "lagos";
UPDATE Customer 
SET city = "lagos"
WHERE cust_name = "jozy altidor";
SELECT * FROM Customer
ORDER BY customer_id ASC;
SELECT * FROM Customer LIMIT 1;
SELECT COUNT(customer_id) 
FROM Customer;
SELECT city,
COUNT (*) AS customer_count
FROM Customer
GROUP BY city;
INSERT INTO Customer(customer_id, cust_name, city, grade, Salesman_id)
VALUES
("3010", "joyce miller", "california", "300", "5008");
UPDATE Customer
SET grade = "100"
WHERE customer_id = "3001";
DELETE FROM Customer
WHERE customer_id = "3001";
SELECT SUM(grade) AS sum_of_grades
FROM Customer;
SELECT AVG(grade) AS sum_of_grades
FROM Customer;
SELECT COUNT(city) AS no_of_city
FROM Customer
WHERE city  = 'london';
