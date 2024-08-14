SELECT category.name, COUNT(film.film_id) as film_amount
FROM film_category
INNER JOIN film ON film.film_id = film_category.film_id
INNER JOIN category ON category.category_id = film_category.category_id
GROUP BY category.name