-- I want to find out the top 3 car manufacturers that customers bought by sales 
-- (quantity) and the sales number for it in the current month.

SELECT car.Manufacturer as Manufacturer, Count(car.Manufacturer) as Sales_Count, Sum(car.Price) as Sales
FROM dealership.Transaction transaction
INNER JOIN dealership.Car as car ON Car.Id = transaction.CarId
WHERE EXTRACT(YEAR FROM transaction.Date) = 2022 AND
EXTRACT(MONTH FROM transaction.Date) = 1
GROUP BY car.Manufacturer
ORDER BY Count(car.Manufacturer) DESC
FETCH FIRST 3 ROWS ONLY

-- NOTE: we can replace EXTRACT(MONTH FROM transaction.Date) = 1 by 
-- EXTRACT(MONTH FROM transaction.Date) = EXTRACT(MONTH FROM CURRENT_DATE)
-- and EXTRACT(YEAR FROM transaction.Date) = 2022 by
-- EXTRACT(YEAR FROM transaction.Date) = EXTRACT(YEAR FROM CURRENT_DATE)
-- to set to the current month. But since this can be run in the future, there
-- will be a case where nothing is fetched since transactions are not within this month