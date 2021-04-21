
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `facerecognition`
--

CREATE TABLE `Student` (
  `ID` VARCHAR(10) NOT NULL,
  `name` VARCHAR(40) NOT NULL,
  `email` VARCHAR(50) NOT NULL,
  `log_in_time` TIMESTAMP,
  `log_out_time` TIMESTAMP,
  `duration` INT AS (TIMESTAMPDIFF(SECOND, log_in_time, log_out_time)),
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `FullTime` (
  `ID` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `PartTime` (
  `ID` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Course` (
  `Course_ID` VARCHAR(8) NOT NULL,
  `name` VARCHAR(60) NOT NULL,
  `info` VARCHAR(300) NOT NULL,
  `teachers_message` VARCHAR(100) NOT NULL,
  `path_to_materials` VARCHAR(100),
  PRIMARY KEY (`Course_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Takes` (
  `ID` VARCHAR(10) NOT NULL,
  `Course_ID` VARCHAR(8) NOT NULL,
  PRIMARY KEY (`ID`, `Course_ID`),
  FOREIGN KEY (`ID`) REFERENCES `Student` (`ID`),
  FOREIGN KEY (`Course_ID`) REFERENCES `Course` (`Course_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Faculty` (
  `Faculty_ID` VARCHAR(10) NOT NULL,
  `name` VARCHAR(40) NOT NULL, 
  `email` VARCHAR(50) NOT NULL,
  `office_address` VARCHAR(6) NOT NULL,
  PRIMARY KEY (`Faculty_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Teaches` (
  `Course_ID` VARCHAR(8) NOT NULL,
  `Faculty_ID` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`Course_ID`, `Faculty_ID`),
  FOREIGN KEY (`Faculty_ID`) REFERENCES `Faculty` (`Faculty_ID`),
  FOREIGN KEY (`Course_ID`) REFERENCES `Course` (`Course_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Classes` (
  `Course_ID` VARCHAR(8) NOT NULL,
  `ClassID` VARCHAR(2) NOT NULL,
  PRIMARY KEY (`Course_ID`, `ClassID`),
  FOREIGN KEY (`Course_ID`) REFERENCES `Course` (`Course_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Lecture` (
  `Course_ID` VARCHAR(8) NOT NULL,
  `ClassID` VARCHAR(2) NOT NULL,
  `Zoom` VARCHAR(128) NOT NULL,
  PRIMARY KEY (`Course_ID`, `ClassID`),
  FOREIGN KEY (`Course_ID`) REFERENCES `Course` (`Course_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `LectTime` (
  `Course_ID` VARCHAR(8) NOT NULL,
  `ClassID` VARCHAR(2) NOT NULL,
  `LectTime_HH` INT NOT NULL,
  `LectTime_Duration` INT NOT NULL,
  `Weekday` INT NOT NULL,
  PRIMARY KEY (`Course_ID`, `ClassID`, `Weekday`),
  FOREIGN KEY (`Course_ID`) REFERENCES `Course` (`Course_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Tutorial` (
  `Course_ID` VARCHAR(8) NOT NULL,
  `ClassID` VARCHAR(2) NOT NULL,
  `TutTime_HH` INT NOT NULL,
  `Weekday` INT NOT NULL,
  `Zoom` VARCHAR(128),
  PRIMARY KEY (`Course_ID`, `ClassID`),
  FOREIGN KEY (`Course_ID`) REFERENCES `Course` (`Course_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Student` WRITE;
/*!40000 ALTER TABLE `Student` DISABLE KEYS */;
INSERT INTO `Student` (`ID`, `name`, `email`, `log_in_time`, `log_out_time`) VALUES
('3035445364','Saalim Mohamed Abdulla','mistermiyagi15973@gmail.com','2021-03-08 09:01:00','2021-03-08 09:05:00'),
('3035445974','Malik Muhammad Junaid Zubair','sicparvismagna15973@gmail.com','2021-03-10 10:10:00','2021-03-10 10:24:00'),
('3035602821','Ahmed Mahnoor','opamuk15973@gmail.com','2021-03-12 13:09:00','2021-03-12 13:49:00'),
('3035492989','Mohiuddin Saad','jmcroissant15973@gmail.com','2021-03-12 17:25:00','2021-03-12 18:05:00'),
('3035436399','Vanessa Leung Jia Min','historia15973@gmail.com','2021-03-13 11:52:00','2021-03-13 12:05:00');
/*!40000 ALTER TABLE `Student` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `FullTime` WRITE;
/*!40000 ALTER TABLE `FullTime` DISABLE KEYS */;
INSERT INTO `FullTime` (`ID`) VALUES
('3035445974'),
('3035602821'),
('3035492989'),
('3035436399');
/*!40000 ALTER TABLE `FullTime` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `PartTime` WRITE;
/*!40000 ALTER TABLE `PartTime` DISABLE KEYS */;
INSERT INTO `PartTime` (`ID`) VALUES
('3035445364');
/*!40000 ALTER TABLE `PartTime` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `Course` WRITE;
/*!40000 ALTER TABLE `Course` DISABLE KEYS */;
INSERT INTO `Course` (`Course_ID`, `path_to_materials`, `name`, `info`, `teachers_message`) VALUES
('STAT4609','/notes/STAT4609','Big Data Analytics','In the past decade, huge volume of data with highly complicated structure has appeared in every aspect, such as social web logs, photographs, tweets and others. This course focuses on the practical knowledge and skills of advanced analytics and statistical modeling for solving big data problems.','Consuming food or beverages of any kind is strictly prohibited during class times.'),
('STAT4710','/notes/STAT4710','Capstone experience for statistics undergraduates','This project-based course aims to provide students with capstone experience to formulate and investigate real life problems in multiple areas of research by integrating and applying the statistical theories and quantitative techniques learnt in their junior university years.','Upcoming meeting on 1st April. Feel free to send an email if you have any queries.'),
('COMP3314','/notes/COMP3314','Machine Learning','An introduction to algorithms and applications of machine learning. Topics include: decision theory; parametric models; supervised learning (classification and regression); unsupervised learning (clustering, mixture models, principal component analysis); Bayesian methods.','No class next week'),
('COMP3278','/notes/COMP3278','Introduction to database management systems','This course studies the principles, design, administration, and implementation of database management systems. Topics include: entity-relationship model, relational model, relational algebra, database design and normalization, database query languages, integrity and concurrency control.','SQL Challenge updated. Please check moodle post.'),
('MATH4602','/notes/MATH4602','Scietific Computing','This course covers some basic theoretical and computational techniques for solving scientific computing problems.','Assignment deadline on 3rd of April.'),
('COMP2396','/notes/COMP2396','OOP with Java','Introduction to object-oriented programming; abstract data types and classes; inheritance and polymorphism; object-oriented program design; Java language and its program development environment; user interfaces and GUI programming; collection class and iteration protocol; program documentation.','Assignment 2 posted on Moodle.'),
('CCHU9074','/notes/CCHU9074','Beyond Fake News','Common core.','Case study due on 5th May.'),
('STAT3621','/notes/STAT3621','Statistical data analysis','Building on prior coursework in statistical methods and modeling, students will get a deeper understanding of the entire process of data analysis. Students will learn how to explore the data, to build reliable models, and to communicate the results of data analysis to a variety of audiences.','Midterm project due on 17 March'),
('STAT3622','/notes/STAT3622','Data visualization','This course will focus on how to work with statistical graphics, graphics that display statistical data, to communicate and analyze data. Students will learn a set of tools such as R to create these graphics and critically evaluate them.','Assignment 2 due on 21 March'),
('AMER2056','/notes/AMER2056','American capitalism ','This course explores the dynamics and development of American capitalism, from the era of slavery to the financial crisis of 2007. This course explores the ever-shifting dynamics of capitalism over four centuries, and students will explore the cultures of capitalism from a number of perspectives.','Lecture recording has been posted'),
('CCCH9005','/notes/CCCH9005','Chinese Cultural Revolution','This course explores the causes, processes, and impact of the Cultural Revolution (CR). It introduces students to key intellectual ideas and methodologies from multi-disciplines and critically assess sources and statements to discover how history is continuously constructed and contested.','Tutorial 5 will be held from March 18-24 for each weekday group respectively '),
('PHYS3450','/notes/PHYS3450','Electromagnetism','This course is to introduce the physical concepts required for an understanding of electricity and magnetism. A foundation course for students majoring in physics.','Problem sets will be assigned on Friday and are due on the following Sunday.'),
('PHYS2155','/notes/PHYS2155','Methods in Physics','This is one of the second level courses that introduces problem solving, mathematical and computational skill sets at university-level physics. We focus on training students how to think and work as physicists through tackling simple physics problems by both analytical and numerical means.','Please visit the course webpage in Science Faculty.');
/*!40000 ALTER TABLE `Course` ENABLE KEYS */;
UNLOCK TABLES;
 
 
LOCK TABLES `Takes` WRITE;
/*!40000 ALTER TABLE `Takes` DISABLE KEYS */;
INSERT INTO `Takes` (`ID`, `Course_ID`) VALUES
('3035445364','STAT4609'),
('3035445364','STAT4710'),
('3035445364','COMP3314'),
('3035445364','COMP3278'),
('3035602821','STAT4609'),
('3035602821','STAT3621'),
('3035602821','STAT3622'),
('3035602821','COMP3278'),
('3035602821','AMER2056'),
('3035445974','COMP3278'),
('3035445974','MATH4602'),
('3035445974','CCHU9074'),
('3035445974','COMP2396'),
('3035492989','COMP3278'),
('3035492989','CCCH9005'),
('3035492989','PHYS3450'),
('3035492989','PHYS2155');
/*!40000 ALTER TABLE `Takes` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `Faculty` WRITE;
/*!40000 ALTER TABLE `Faculty` DISABLE KEYS */;
INSERT INTO `Faculty` (`Faculty_ID`, `name`, `email`, `office_address`) VALUES
('001','Luo P.','pluo@cs.hku.hk','CB326'),
('002','Yu Y.Z.','yzyu@cs.hku.hk','CB325'),
('003','Chim T.W.','twchim@cs.hku.hk','HW519'),
('004','Kajimoto M.','kajimoto@hku.hk','EH121'),
('005','Zhang D.Y.','doraz@hku.hk','RR304'),
('006','Yin G.','gyin@hku.hk','RR233'),
('007','Ali L.','historia15973@gmail.com','RR501'),
('008','Wang A.','awang@hku.hk','CRT963'),
('009','Cui X.D.','xdcui@hku.hk','CYM209'),
('010','Lee D.','leedav@hku.hk','RR120'),
('011','Lee K.M.','kmlee@lily.physics.hku.hk','CYM415'),
('012','Ching W.K.','wching@hku.hk','RR414'),
('013','Zhang M.','mzhang18@hku.hk','RR224');
/*!40000 ALTER TABLE `Faculty` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `Teaches` WRITE;
/*!40000 ALTER TABLE `Teaches` DISABLE KEYS */;
INSERT INTO `Teaches` (`Course_ID`, `Faculty_ID`) VALUES
('COMP3278','001'),
('COMP3314','002'),
('COMP2396','003'),
('CCHU9074','004'),
('STAT3621','005'),
('STAT3622','006'),
('AMER2056','007'),
('CCCH9005','008'),
('PHYS3450','009'),
('STAT4710','010'),
('PHYS2155','011'),
('MATH4602','012'),
('STAT4609','013');
/*!40000 ALTER TABLE `Teaches` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `Classes` WRITE;
/*!40000 ALTER TABLE `Classes` DISABLE KEYS */;
INSERT INTO `Classes` (`Course_ID`, `ClassID`) VALUES
('COMP3278','L'),
('COMP3314','L'),
('COMP2396','L'),
('CCHU9074','L'),
('STAT3621','L'),
('STAT3622','L'),
('AMER2056','L'),
('CCCH9005','L'),
('PHYS3450','L'),
('STAT4710','L'),
('PHYS2155','L'),
('MATH4602','L'),
('STAT4609','L'),
('PHYS2155','T'),
('MATH4602','T'),
('STAT4609','T'),
('COMP3278','T'),
('CCHU9074','T'),
('COMP2396','T'),
('CCCH9005','T');
/*!40000 ALTER TABLE `Classes` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `Lecture` WRITE;
/*!40000 ALTER TABLE `Lecture` DISABLE KEYS */;
INSERT INTO `Lecture` (`Course_ID`, `ClassID`, `Zoom`) VALUES
('STAT4609','L','https://hku.zoom.us/j/95828831639'),
('COMP3314','L','https://hku.zoom.us/j/92125651881?pwd=Q0t2WTdrc1ZTMnVOTVAyak82bmpGdz09'),
('COMP3278','L','https://hku.zoom.us/j/97686555806?pwd=NWxSNVRKTlNDU0NjYTgremxaQ3pldz09'),
('MATH4602','L','https://hku.zoom.us/j/99227888994?pwd=eXZLQkRDM2l6bXU4R2VJZDBNQlNhQT09'),
('CCHU9074','L','https://hku.zoom.us/j/91517172449?pwd=RXppbW5ldVdZZ2JvWjlJV1FhM2pDQT09'),
('COMP2396','L','https://hku.zoom.us/j/97902227890?pwd=QnlWWHdudGY0K21GeHhTa3JDQ3Urdz09'),
('CCCH9005','L','https://hku.zoom.us/j/3531454530?pwd=VUpWMUhmck1yMjE5TUhuU0pGWHBmUT09'),
('PHYS3450','L','https://zoom.us/j/8237642261#success'),
('PHYS2155','L','https://zoom.us/j/4782746197#success');
/*!40000 ALTER TABLE `Lecture` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `LectTime` WRITE;
/*!40000 ALTER TABLE `LectTime` DISABLE KEYS */;
INSERT INTO `LectTime` (`Course_ID`, `ClassID`, `LectTime_HH`, `LectTime_Duration`, `Weekday`) VALUES
('STAT4609','L',13,3,4),
('COMP3314','L',14,3,1),
('COMP3278','L',9,2,2),
('MATH4602','L',9,2,1),
('MATH4602','L',9,1,4),
('CCHU9074','L',16,2,3),
('COMP2396','L',12,2,5),
('CCCH9005','L',14,2,3),
('PHYS3450','L',3,1,2),
('PHYS3450','L',3,2,5),
('PHYS2155','L',12,1,2),
('PHYS2155','L',12,2,5);
/*!40000 ALTER TABLE `LectTime` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `Tutorial` WRITE;
/*!40000 ALTER TABLE `Tutorial` DISABLE KEYS */;
INSERT INTO `Tutorial` (`Course_ID`, `ClassID`, `TutTime_HH`, `Weekday`, `Zoom`) VALUES
('STAT4609','T',17,2,'https://hku.zoom.us/j/93095224906'),
('COMP3278','T',9,5,'https://hku.zoom.com.cn/j/2640918958?pwd=UmFpek1YMkUzNTFoL0ljRW84M1VLUT09'),
('MATH4602','T',14,5,'https://hku.zoom.us/j/99227888994?pwd=eXZLQkRDM2l6bXU4R2VJZDBNQlNhQT09'),
('CCHU9074','T',18,3,'https://hku.zoom.us/j/91517172449?pwd=RXppbW5ldVdZZ2JvWjlJV1FhM2pDQT09'),
('COMP2396','T',12,2,'https://hku.zoom.us/j/97902227890?pwd=QnlWWHdudGY0K21GeHhTa3JDQ3Urdz09'),
('CCCH9005','T',10,3,'https://hku.zoom.us/j/3531454530?pwd=VUpWMUhmck1yMjE5TUhuU0pGWHBmUT09');
/*!40000 ALTER TABLE `Tutorial` ENABLE KEYS */;
UNLOCK TABLES;



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;