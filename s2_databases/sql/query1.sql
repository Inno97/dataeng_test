-- 1. I want to know the list of our customers and their spending.
SELECT customer.Name as Name, SUM(car.Price) AS SPENDING
FROM dealership.Customer customer
INNER JOIN dealership.Transaction transaction ON customer.Id = transaction.CustomerId
INNER JOIN dealership.Car car on Car.Id = transaction.CarId
GROUP BY customer.name