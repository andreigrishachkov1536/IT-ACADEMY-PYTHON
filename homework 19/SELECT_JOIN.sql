SELECT
	users.name,
	orders.total
FROM users JOIN orders ON users.id = orders.user_id;

SELECT
users.name,
orders.total
FROM users
LEFT JOIN orders
ON users.id = orders.user_id;


SELECT COUNT(*)
FROM users;

SELECT SUM(total)
FROM orders;

SELECT AVG(total)
FROM orders;