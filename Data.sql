INSERT INTO Student (ID, name, email, log_in_time, log_out_time) VALUES
('3035445364','Saalim Mohamed Abdulla','mistermiyagi15973@gmail.com','2021-03-08 09:01:00','2021-03-08 09:05:00'),
('3035602821','Ahmed Mahnoor','opamuk15973@gmail.com','2021-03-12 13:09:00','2021-03-12 13:49:00'),
('3035492989','Mohiuddin Saad','jmcroissant15973@gmail.com','2021-03-12 17:25:00','2021-03-12 18:05:00');

INSERT INTO FullTime (ID) VALUES
('3035445364'),
('3035492989');

INSERT INTO PartTime (ID) VALUES
('3035602821');

INSERT INTO Course (Course_ID, path_to_materials, name, info, teachers_message) VALUES
('STAT4609','/notes/STAT4609','Big Data Analytics','In the past decade, huge volume of data with highly complicated structure has appeared in every aspect, such as social web logs, photographs, tweets and others. This course focuses on the practical knowledge and skills of advanced analytics and statistical modeling for solving big data problems.','Consuming food or beverages of any kind is strictly prohibited during class times.'),
('STAT4710','/notes/STAT4710','Capstone experience for statistics undergraduates','This project-based course aims to provide students with capstone experience to formulate and investigate real life problems in multiple areas of research by integrating and applying the statistical theories and quantitative techniques learnt in their junior university years.','Upcoming meeting on 1st April. Feel free to send an email if you have any queries.'),
('COMP3314','/notes/COMP3314','Machine Learning','An introduction to algorithms and applications of machine learning. Topics include: decision theory; parametric models; supervised learning (classification and regression); unsupervised learning (clustering, mixture models, principal component analysis); Bayesian methods.','No class next week'),
('COMP3278','/notes/COMP3278','Introduction to database management systems','This course studies the principles, design, administration, and implementation of database management systems. Topics include: entity-relationship model, relational model, relational algebra, database design and normalization, database query languages, integrity and concurrency control.','SQL Challenge updated. Please check moodle post.'),
('MATH4602','/notes/MATH4602','Scietific Computing','This course covers some basic theoretical and computational techniques for solving scientific computing problems.','Assignment deadline on 3rd of April.'),
('CCCH9005','/notes/CCCH9005','Chinese Cultural Revolution','This course explores the causes, processes, and impact of the Cultural Revolution (CR). It introduces students to key intellectual ideas and methodologies from multi-disciplines and critically assess sources and statements to discover how history is continuously constructed and contested.','Tutorial 5 will be held from March 18-24 for each weekday group respectively '),
('PHYS3450','/notes/PHYS3450','Electromagnetism','This course is to introduce the physical concepts required for an understanding of electricity and magnetism. A foundation course for students majoring in physics.','Problem sets will be assigned on Friday and are due on the following Sunday.'),
('PHYS2155','/notes/PHYS2155','Methods in Physics','This is one of the second level courses that introduces problem solving, mathematical and computational skill sets at university-level physics. We focus on training students how to think and work as physicists through tackling simple physics problems by both analytical and numerical means.','Please visit the course webpage in Science Faculty.');
 
INSERT INTO Takes (ID, Course_ID) VALUES
('3035445364','STAT4609'),
('3035445364','CCCH9005'),
('3035445364','COMP3278'),
('3035602821','COMP3278'),
('3035602821','PHYS3450'),
('3035492989','COMP3278'),
('3035492989','CCCH9005'),
('3035492989','PHYS3450'),
('3035492989','PHYS2155');

INSERT INTO Faculty (Faculty_ID, name, email, office_address) VALUES
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

INSERT INTO Teaches (Course_ID, Faculty_ID) VALUES
('COMP3278','001'),
('CCCH9005','008'),
('PHYS3450','009'),
('PHYS2155','011'),
('MATH4602','012'),
('STAT4609','013');

INSERT INTO Classes (Course_ID, ClassID) VALUES
('COMP3278','L'),
('CCCH9005','L'),
('PHYS3450','L'),
('PHYS3450','T'),
('PHYS2155','L'),
('PHYS2155','T'),
('MATH4602','L'),
('MATH4602','T'),
('STAT4609','L'),
('STAT4609','T'),
('COMP3278','T'),
('CCCH9005','T');

INSERT INTO Lecture (Course_ID, ClassID, Zoom) VALUES
('STAT4609','L','https://hku.zoom.us/j/95828831639'),
('COMP3278','L','https://hku.zoom.us/j/97686555806?pwd=NWxSNVRKTlNDU0NjYTgremxaQ3pldz09'),
('MATH4602','L','https://hku.zoom.us/j/99227888994?pwd=eXZLQkRDM2l6bXU4R2VJZDBNQlNhQT09'),
('MATH4602','L','https://hku.zoom.us/j/99227888994?pwd=eXZLQkRDM2l6bXU4R2VJZDBNQlNhQT09'),
('CCCH9005','L','https://hku.zoom.us/j/3531454530?pwd=VUpWMUhmck1yMjE5TUhuU0pGWHBmUT09'),
('PHYS3450','L','https://zoom.us/j/8237642261#success'),
('PHYS3450','L','https://zoom.us/j/8237642261#success'),
('PHYS2155','L','https://zoom.us/j/4782746197#success'),
('PHYS2155','L','https://zoom.us/j/4782746197#success');

INSERT INTO LectTime (Course_ID, ClassID, LectTime_HH, LectTime_Duration, Weekday) VALUES
('STAT4609','L',13,3,4),
('COMP3278','L',9,2,2),
('MATH4602','L',9,2,1),
('MATH4602','L',9,1,4),
('CCCH9005','L',14,2,3),
('PHYS3450','L',3,1,2),
('PHYS3450','L',3,2,5),
('PHYS2155','L',12,1,2),
('PHYS2155','L',12,2,5);

INSERT INTO Tutorial (Course_ID, ClassID, TutTime_HH, Weekday, Zoom) VALUES
('STAT4609','T',17,2,'https://hku.zoom.us/j/93095224906'),
('COMP3278','T',9,5,'https://hku.zoom.com.cn/j/2640918958?pwd=UmFpek1YMkUzNTFoL0ljRW84M1VLUT09'),
('MATH4602','T',14,5,'https://hku.zoom.us/j/99227888994?pwd=eXZLQkRDM2l6bXU4R2VJZDBNQlNhQT09'),
('CCHU9074','T',18,3,'https://hku.zoom.us/j/91517172449?pwd=RXppbW5ldVdZZ2JvWjlJV1FhM2pDQT09'),
('COMP2396','T',12,2,'https://hku.zoom.us/j/97902227890?pwd=QnlWWHdudGY0K21GeHhTa3JDQ3Urdz09'),
('CCCH9005','T',10,3,'https://hku.zoom.us/j/3531454530?pwd=VUpWMUhmck1yMjE5TUhuU0pGWHBmUT09');
