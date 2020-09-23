/*-------------------------
Table Flight
--------------------------*/

CREATE TABLE flights (
	id SERIAL PRIMARY KEY,
	origin VARCHAR NOT NULL,
	destination VARCHAR NOT NULL,
	duration INTEGER NOT NULL
);

insert into flights(origin, destination, duration)
values ('Jujuy', 'Cordoba', 120);

insert into flights(origin, destination, duration)
values ('Salta', 'Cordoba', 90);

insert into flights(origin, destination, duration)
values ('Cordoba', 'Buenos Aires', 120);

insert into flights(origin, destination, duration)
values ('Cordoba', 'Mendoza', 100);

insert into flights(origin, destination, duration)
values ('Mendoza', 'Buenos Aires', 110);

/*-------------------------
Table Passengers
--------------------------*/

create table passengers (
	id SERIAL not null,
	"name" varchar not null,
	flight_id integer references flights not null
);

insert into passengers(name, flight_id)
values('Nacho', 1);

insert into passengers(name, flight_id)
values('Apu', 1);

insert into passengers(name, flight_id)
values('Juan', 1);

insert into passengers(name, flight_id)
values('Pato', 2);

insert into passengers(name, flight_id)
values('Francis', 3);

insert into passengers(name, flight_id)
values('Martin', 4);

insert into passengers(name, flight_id)
values('Mati', 5);

