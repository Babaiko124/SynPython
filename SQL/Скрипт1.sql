drop database if exists test;
create database if not exists test;
use test;
create table if not exists USERS_TEST
(
id int,
username varchar(30),
lastname varchar(30),
date varchar(20),
index (id,username)
);

insert into USERS_TEST values
(1,'One','One', '09.09.2009'),
(2,'Two','Two', '15.09.2009'),
(3,'Three','Three', '17.09.2009'),
(4,'Four','Four', '01.09.2009'),
(5,'Five','Five', '25.09.2009');

create table if not exists SERIALS
(
id int,
title varchar(30),
index (id,title)
);

insert into SERIALS values
(1,'Остаться в живых'),
(2,'Бригада'),
(3,'Сваты'),
(4,'Очень странные дела'),
(5,'Шерлок');

create table if not exists REVIEWS
(
id int,
review varchar(300),
rating int,
index(id)
);

insert into REVIEWS values
(1,'Страшно интересно что будет дальше',5),
(2,'Хорошо',3),
(3,'Скучно',1);

insert into REVIEWS(id, rating) values
(6,10),
(12,7);

create table if not exists GENRES
(
id int,
genre varchar(30),
index(id,genre)
);

insert into GENRES values
(1,'Комедия'),
(2,'Триллер'),
(3,'Мистика');

insert into GENRES(genre) values
('Детектив'),
('Драма');

select * from USERS_TEST;
select * from SERIALS;
select * from GENRES;
select * from REVIEWS;

update USERS_TEST set username='пользователь';
update USERS_TEST set lastname='Сенаторов' where date='09.09.2009';
select * from USERS_TEST;

delete from GENRES where id=1;
-- delete from GENRES where genre='Мистика';
select * from GENRES;