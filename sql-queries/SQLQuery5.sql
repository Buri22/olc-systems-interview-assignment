CREATE PROCEDURE sp_InsertFilm
    @title nvarchar(255),
    @description nvarchar(max),
    @release_year int,
    @language_id smallint,
    @rental_duration smallint,
    @rental_rate decimal(4,2),
    @length smallint,
    @replacement_cost decimal(5,2),
    @rating nvarchar(5),
    @category_ids varchar(max),
    @actor_ids varchar(max),
    @store_ids varchar(max)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Insert film record
    DECLARE @film_id int;
    INSERT INTO film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, last_update)
    VALUES (@title, @description, @release_year, @language_id, @rental_duration, @rental_rate, @length, @replacement_cost, @rating, GETDATE());
    SET @film_id = SCOPE_IDENTITY();

    -- Insert film_category records
    DECLARE @category_id smallint;
    DECLARE @category_ids_table TABLE (category_id smallint);
    INSERT INTO @category_ids_table (category_id)
    SELECT value FROM string_split(@category_ids, ',');

    INSERT INTO film_category (film_id, category_id, last_update)
    SELECT @film_id, category_id, GETDATE() FROM @category_ids_table;

    -- Insert film_actor records
    DECLARE @actor_id smallint;
    DECLARE @actor_ids_table TABLE (actor_id smallint);
    INSERT INTO @actor_ids_table (actor_id)
    SELECT value FROM string_split(@actor_ids, ',');

    INSERT INTO film_actor (film_id, actor_id, last_update)
    SELECT @film_id, actor_id, GETDATE() FROM @actor_ids_table;

    -- Insert inventory records
    DECLARE @store_id smallint;
    DECLARE @store_ids_table TABLE (store_id smallint);
    INSERT INTO @store_ids_table (store_id)
    SELECT value FROM string_split(@store_ids, ',');

    INSERT INTO inventory (film_id, store_id, last_update)
    SELECT @film_id, store_id, GETDATE() FROM @store_ids_table;
END
GO