DECLARE @rental_id INT = 15813
DECLARE @max_rental_days INT = 14
DECLARE @after_deadline_days INT

SELECT @after_deadline_days =
	CASE WHEN rental.return_date IS NULL
		THEN DATEDIFF(y, rental.rental_date, GETDATE())
		ELSE DATEDIFF(y, rental.rental_date, return_date)
	END - @max_rental_days
FROM rental
WHERE rental.rental_id = @rental_id

SELECT
	CASE WHEN @after_deadline_days > 0
		THEN @after_deadline_days * payment.amount / 100
		ELSE 0
	END as rental_fine
FROM rental
INNER JOIN payment ON payment.rental_id = rental.rental_id
WHERE rental.rental_id = @rental_id