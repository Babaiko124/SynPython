drop database if exists test2;
create database if not exists test2;
use test2;
create table if not exists markets
(
id int,
title varchar(100),
address varchar(100),
city varchar(100),
`working hours` varchar(100),
index (id,title)
);

insert into markets values
(0,'Пятёрочка','ул.Семёнова,47','Москва', '8:00-22:00'),
(1,'Перекрёсток','ул.Семёнова,48','Москва', 'Круглосуточно'),
(2,'Пятёрочка','ул.Вовы,32','Санкт-Петербург', '8:30-22:30'),
(3,'Перекрёсток','ул.Татьяны Б.,1','Ижевск', '9:00-21:00');

select * from markets;

update markets set title='Пятёрочка 2' where title='Пятёрочка';
update markets set address='пр-т Орлова, 33' where city='Ижевск';
update markets set address='Рядом с домом',title='Всегда открыто' where `working hours`='Круглосуточно';
delete from markets where id=2;
select * from markets;