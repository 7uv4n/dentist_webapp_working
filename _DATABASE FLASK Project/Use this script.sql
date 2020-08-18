create database dentalproject;
use dentalproj;

create table dental
(
p_id int NOT NULL PRIMARY KEY auto_increment,
pname varchar(50) NOT NULL,
birthdate varchar(15) NOT NULL,
age varchar(3) NOT NULL,
gender varchar(3) NOT NULL,
occupation varchar(50)NOT NULL,
mobile varchar(11) NOT NULL,
raddress varchar(100) NOT NULL,
e_name varchar(50) NOT NULL,
e_mobile int(11) NOT NULL,
relation varchar(50) NOT NULL,
care varchar(100),
drugs varchar(100),
surgery varchar(100),
chest varchar(100),
bleed varchar(100),
bldis varchar(100),
odrugs varchar(100),
smoke varchar(10),
ocondn varchar(200),
pregnant varchar(30),
period varchar(20),
pills varchar(20)
);
