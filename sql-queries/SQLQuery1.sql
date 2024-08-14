SELECT CONCAT(customer.first_name, ' ', customer.last_name) AS customer_name
, address.address
, address.postal_code
, city.city
, country.country
FROM customer
INNER JOIN address ON customer.address_id = address.address_id
INNER JOIN city ON address.city_id = city.city_id
INNER JOIN country ON city.country_id = country.country_id

WHERE customer.customer_id IN (
	SELECT rental.customer_id
	FROM rental
	WHERE YEAR(rental.rental_date) = (SELECT TOP(1) YEAR(rental_date) FROM rental ORDER BY rental_date DESC)
	GROUP BY rental.customer_id
)