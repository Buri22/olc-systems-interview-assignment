SELECT
	CONCAT(staff.first_name, ' ', staff.last_name) AS staff_name,
    YEAR(rental.rental_date) AS rental_year,
    COUNT(rental.rental_id) AS rental_amount,
	store.store_id
FROM 
    staff
INNER JOIN
    rental ON staff.staff_id = rental.staff_id
INNER JOIN
    store ON store.store_id = staff.store_id
GROUP BY
	staff.first_name,
	staff.last_name,
    YEAR(rental.rental_date),
	store.store_id
ORDER BY 
    staff_name,
    rental_year;