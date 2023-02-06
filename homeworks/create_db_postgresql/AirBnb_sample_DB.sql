CREATE DATABASE  AirBnb_sample;

CREATE TABLE Hosts(
	host_id 	serial PRIMARY KEY,
	host_name	TEXT 		NOT NULL,
	host_email 	VARCHAR(30)	NOT NULL,
	host_phone	VARCHAR(20),
	host_url	VARCHAR(50)	NOT NULL,
	host_location TEXT		NOT NULL
);

CREATE TABLE Rooms(
	room_id		serial PRIMARY KEY,
	home_type 	VARCHAR(20)	NOT NULL,
	room_type	VARCHAR(20)	NOT NULL,
	total_accomodates	INT	NOT NULL,
	total_bedrooms		INT	NOT NULL,
	total_beds			INT	NOT NULL,
	total_bathrooms		INT NOT NULL,
	amenities	TEXT		NOT NULL,
	price		DECIMAL(10,2) NOT NULL,
	address		VARCHAR(50)	NOT NULL,
	host_id		serial		references Hosts(host_id)
);

CREATE TABLE Guests(
	guest_id	serial 	PRIMARY KEY,
	guest_name	TEXT	NOT NULL,
	guest_email	VARCHAR(30) NOT NULL
);

CREATE TABLE Reservations(
	reservation_id	serial PRIMARY KEY,
	guest_id 	serial 	references Rooms(room_id),
	room_id		serial	references Guests(guest_id),
	start_date 	TIMESTAMP		NOT NULL,
	end_date	TIMESTAMP		NOT NULL,
	price_full	DECIMAL(10, 2)	NOT NULL,
	created_at	TIMESTAMP		NOT NULL
);

CREATE TABLE Room_reserved (
	room_reserved_id serial PRIMARY KEY,
	reservation_id	serial 	references Reservations(reservation_id),
	room_id			serial	references Rooms(room_id),
	price	DECIMAL(10, 2)	NOT NULL
);

CREATE TABLE Invoice_guest(
	invoice_id 	serial PRIMARY KEY,
	guest_id 	serial references Guests(guest_id),
	reservation_id 	serial references Reservations(reservation_id),
	invoice_amount 	DECIMAL(10,2)	NOT NULL,
	created_at 		TIMESTAMP 		NOT NULL,
	paid_at 		TIMESTAMP,
	canceled_at 	TIMESTAMP
);

CREATE TABLE Reviews(
	review_id	serial 	PRIMARY KEY,
	rating		INT 	NOT NULL,
	review_text	TEXT,
	guest_id	serial	references Guests(guest_id)
);

CREATE TABLE Review_room(
	review_room_id	serial 	PRIMARY KEY,
	review_id 		serial 	references Reviews (review_id),
	room_id	serial UNIQUE	references Rooms (room_id)
);

CREATE TABLE Review_host(
	review_host_id	serial 	PRIMARY KEY,
	review_id 	serial 		references Reviews (review_id),
	host_id		serial UNIQUE references Hosts (host_id)
);

INSERT INTO Hosts (host_name, host_email, host_phone, host_url, host_location)
VALUES
	('Sash', 'sash@gmail.com', '4158245056', 'http:\\sash.airbnb.com', 'Varsawa, Centre'),
	('Alex', 'alex@gmail.com', '5874569516', 'http:\\alex.airbnb.com', 'Praha, Old Centre'),
	('Mark', 'mark@gmail.com', '0887564488', 'http:\\mark.airbnb.com', 'Vienna, Aspern')
;

SELECT * FROM Hosts;

INSERT INTO Rooms(home_type, room_type, total_accomodates, total_bedrooms, total_beds, total_bathrooms, amenities, price, address)
VALUES
	('House', 'apt', 3, 1, 1, 1, 'Waterfront, EV charger, HDTV, Backyard, Dedicated workspace, Kitchen', 56.0, 'Mila, Warszawa, Poland'),
	('House', 'apt', 3, 1, 2, 1, 'TV, Kitchen, WiFi, Washing machine', 40.0, 'Prague 1, Hlavní město Praha, Czech Republic'),
	('House', 'apt', 4, 1, 2, 1, 'Kitchen, Free parking, Washing machine, TV, WiFi', 50.0, 'Hohenbergstraße, Wien, Austria')
;

SELECT * FROM Rooms;

INSERT INTO Guests(guest_name, guest_email)
VALUES
	('Martin', 'martin@te.com'),
	('David', 'david@gut.com'),
	('Mary', 'mary@mar.com')
;

SELECT * FROM Guests;

INSERT INTO Reviews(rating, review_text, guest_id)
VALUES
	(5, 'Quite out the way of the city but transport is right on your doorstep making it easily accessible', 3),
	(4, 'Washing machine located at basement which is quite trouble and it is a bit dirty', 1),
	(5, 'Very good location, nice neighborhood and public transportation is nearby', 2)
;

INSERT INTO Room_reserved(room_id, reservation_id, price)
VALUES
	(1, 1, 56),
	(2, 2, 40),
	(2, 3, 40)
;

INSERT INTO Reservations(room_id, guest_id, start_date, end_date, price_full, created_at)
VALUES
	(1, 1, '2022-12-05 12:00:00', '2022-12-10 12:00:00', 280, '2022-10-27 21:15:47'),
	(2, 3, '2023-01-24 10:00:00', '2023-01-30 09:00:00', 240, '2022-12-15 23:05:21'),
	(2, 2, '2022-12-18 15:00:00', '2022-12-21 10:00:00', 120, '2022-12-15 10:47:28')
;

INSERT INTO Invoice_guest(reservation_id, invoice_amount, created_at, paid_at)
VALUES
	(1, 280, '2022-10-27 21:43:12', '2022-10-27 22:01:16'),
	(2, 240, '2022-12-15 23:12:41', '2022-12-16 08:42:15'),
	(3, 120, '2022-12-15 10:54:32', '2022-12-15 11:02:47')
;

-- Find a user who had biggest amount of reservation.
-- Return user name and user_id
SELECT t1.guest_id, t2.guest_name
FROM 
	(SELECT guest_id, sum(price_full) amount_reservation
	 FROM Reservations
	 GROUP BY guest_id) AS t1
JOIN Guests AS t2 
ON (t1.guest_id = t2.guest_id)
ORDER BY t1.amount_reservation DESC
LIMIT 1;

-- Find a host who earned biggest amount of money for the last month.
-- Return host name and host_id
SELECT t2.host_name, t1.host_id
FROM (SELECT Rooms.host_id, sum(Reservations.price_full) amount_host_revenue
	  FROM Rooms
	  JOIN Room_reserved
	  	ON (Room_reserved.room_id = Rooms.room_id)
	  JOIN Reservations
	  	ON (Room_reserved.reservation_id = Reservations.reservation_id)
	  GROUP BY Rooms.host_id
	  ORDER BY amount_host_revenue DESC
	  LIMIT 1) AS t1
JOIN Hosts AS t2
ON (t1.host_id = t2.host_id)
;

-- OR 
WITH host_revenue AS (
	SELECT Rooms.host_id, sum(Reservations.price_full) amount_host_revenue
	  FROM Rooms
	  JOIN Room_reserved
	  	ON (Room_reserved.room_id = Rooms.room_id)
	  JOIN Reservations
	  	ON (Room_reserved.reservation_id = Reservations.reservation_id)
	  GROUP BY Rooms.host_id
	  ORDER BY amount_host_revenue DESC)
SELECT hosts.host_name, host_revenue.host_id 
FROM host_revenue
JOIN Hosts
ON (Hosts.host_id = host_revenue.host_id)
LIMIT 1
;


-- Oportunity to check available date for reservation in particular room
WITH vars AS (
	SELECT 
		'2022-12-09'::date AS startdate, 	-- enter start date
		'2022-12-11'::date as enddate		-- enter end date 
),
calendar AS ( 	-- create calendar for period you want to check
	SELECT
		vars.startdate AS startdate,
		vars.enddate AS enddate,
    	DENSE_RANK() OVER (ORDER BY t1.date) as rank,
    	t1.date 
	FROM
    	vars,
		generate_series(vars.startdate, vars.enddate, '1 day') AS t1
)
SELECT
	Rooms.room_id, 
	calendar.date
FROM vars, calendar
	CROSS JOIN Rooms 
	LEFT JOIN Room_reserved ON Rooms.room_id = Room_reserved.room_id
	LEFT JOIN Reservations ON Room_reserved.reservation_id = Reservations.reservation_id
		AND calendar.date BETWEEN Reservations.start_date AND Reservations.end_date
WHERE Reservations.reservation_id IS NULL
GROUP BY Rooms.room_id, calendar.date
ORDER BY room_id, date
;