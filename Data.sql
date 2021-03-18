INSERT INTO Student (ID, name, welcome_message) VALUES
('3035445364','Saalim Mohamed Abdulla', 'Welcome back! Check out your courses and keep up with your timetable!'),
('3035445974','Malik Muhammad Junaid Zubair', 'Welcome back! Check out your courses and keep up with your timetable!'),
('3035602821','Ahmed Mahnoor', 'Welcome back! Check out your courses and keep up with your timetable!'),
('3035492989','Mohiuddin Saad', 'Welcome back! Check out your courses and keep up with your timetable!');

INSERT INTO LogIn (ID, log_in_time, log_out_time) VALUES
('3035492989', '2021-03-08 09:01:00', '2021-03-08 09:05:00'),
('3035602821', '2021-03-10 10:10:00', '2021-03-10 10:24:00'),
('3035445364', '2021-03-12 13:09:00', '2021-03-12 13:49:00'),
('3035445974', '2021-03-12 17:25:00', '2021-03-12 18:05:00'),
('3035445364', '2021-03-13 11:52:00', '2021-03-13 12:05:00');

INSERT INTO Course (Course_ID, name, info, teachers_message) VALUES
('STAT4609','Big Data Analytics','In the past decade, huge volume of data with highly complicated structure has appeared in every aspect, such as social web logs, e-mails, video, speech recordings, photographs, tweets and others. The efficient extraction of valuable information from these data sources becomes a challenging task. This course focuses on the practical knowledge and skills of some advanced analytics and statistical modeling for solving big data problems.','Consuming food or beverages of any kind is strictly prohibited during class times. Messes with my flow. Thank you for your understanding.'),
('STAT4710','Capstone experience for statistics undergraduates','This project-based course aims to provide students with capstone experience to formulate and investigate real life problems in the area of statistics, risk management, finance, climate, social science, medicine and scientific research by integrating and applying the statistical theories and quantitative techniques learnt in their junior university years.','Upcoming meeting on 1st April. Feel free to send an email if you have any queries.'),
('COMP3314','Machine Learning','An introduction to algorithms and applications of machine learning. Topics include: decision theory; parametric models; supervised learning (classification and regression); unsupervised learning (clustering, mixture models, principal component analysis); Bayesian methods.','No class next week'),
('COMP3278','Introduction to database management systems','This course studies the principles, design, administration, and implementation of database management systems. Topics include: entity-relationship model, relational model, relational algebra, database design and normalization, database query languages, indexing schemes, integrity and concurrency control.','SQL Challenge updated. Please check moodle post.'),
('MATH4602','Scietific Computing','This course covers some basic theoretical and computational techniques for solving scientific computing problems.','Assignment deadline on 3rd of April.'),
('COMP2396','OOP with Java','Introduction to object-oriented programming; abstract data types and classes; inheritance and polymorphism; object-oriented program design; Java language and its program development environment; user interfaces and GUI programming; collection class and iteration protocol; program documentation.','Assignment 2 posted on Moodle.'),
('CCHU9074','Beyond Fake News','Common core.','Case study due on 5th May.'),
('STAT3621','Statistical data analysis','Building on prior coursework in statistical methods and modeling, students will get a deeper understanding of the entire process of data analysis. The course aims to develop skills of model selection and hypotheses formulation so that questions of interest can be properly formulated and answered. An important element deals with model review and improvement, when ones first attempt does not adequately fit the data. Students will learn how to explore the data, to build reliable models, and to communicate the results of data analysis to a variety of audiences.','Midterm project due on 17 March'),
('STAT3622','Data visualization','This course will focus on how to work with statistical graphics, graphics that display statistical data, to communicate and analyze data. Students will learn a set of tools such as R to create these graphics and critically evaluate them.','Assignment 2 due on 21 March'),
('AMER2056','American capitalism ','This course explores the dynamics and development of American capitalism, from the era of slavery to the financial crisis of 2007. In this period the United States emerged as the dominant financial and industrial power of the global order. The development of American capitalism produced unprecedented material wealth but also growing inequality and class- and race-based social divisions. This course explores the ever-shifting dynamics of capitalism over four centuries, and will allow students to explore the cultures of capitalism from a number of perspectives.','Lecture recording has been posted'),
('CCCH9005','Chinese Cultural Revolution','The Cultural Revolution (1966-1976) was a defining episode in modern China. In ten years, it dismantled the state, party, and economy with widespread social upheaval and violence, followed by unrelenting oppressive campaigns. It dramatically exploded the inherent contradictions of the Communist State. It has exerted a major impact on the direction of Chinese politics, economic reforms, and public protests. This course explores the causes, processes, and impact of the Cultural Revolution (CR), asking why millions of people participated in the CR, who were the agents responsible for the CR, what determined the CR’s multifaceted courses, and what legacy the CR left for the following reform era and the coming future. It introduces students to key intellectual ideas and methodologies from multi-disciplines – history, political and social science, literature, and film. Students will learn to critically assess sources and statements, through which to discover how history is continuously constructed and contested.','Tutorial 5 will be held on Mar. 18 (Thursday groups), Mar. 19 (Friday groups), Mar. 20 (Saturday group), Mar. 22 (Monday groups), Mar. 23 (Tuesday groups) and Mar. 24 (Wednesday groups). '),
('PHYS3450','Electromagnetism','This course is to introduce the physical concepts required for an understanding of electricity and magnetism. A foundation course for students majoring in physics.','There will be 6 or 7 assignments. Problem sets will be assigned on Friday. Completed problem sets are due on the following Sunday. No problem sets will be accepted after the solutions have been posted.'),
('PHYS2155','Methods in Physics','This is one of the second level courses in our series of courses that introduces problem solving, mathematical and computational skill sets that are commonly used in the study of university-level physics. Instead of the cookbook approach, we focus on training students how to think and work as physicists through tackling simple physics problems by both analytical and numerical means. After completion, interested students may take the other second level courses in this series PHYS2150 and/or PHYS2160 or the third level course in this series PHYS3150.','Please also visit the course webpage in Science Faculty. Backup of email announcements is in "News Announcement" above.');
 
INSERT INTO Takes (ID, Course_ID) VALUES
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

INSERT INTO Lecture (Course_ID, LectNo, LectTime_HH, LectTime_MM, LectTime_Duration, Weekday, Zoom) VALUES
('STAT4609',1,13,30,3,4,'https://hku.zoom.us/j/95828831639'),
('COMP3314',1,14,30,3,1,'https://hku.zoom.us/j/92125651881?pwd=Q0t2WTdrc1ZTMnVOTVAyak82bmpGdz09'),
('COMP3278',1,9,30,2,2,'https://hku.zoom.us/j/97686555806?pwd=NWxSNVRKTlNDU0NjYTgremxaQ3pldz09'),
('MATH4602',1,9,30,2,1,'https://hku.zoom.us/j/99227888994?pwd=eXZLQkRDM2l6bXU4R2VJZDBNQlNhQT09'),
('MATH4602',2,9,30,1,4,'https://hku.zoom.us/j/99227888994?pwd=eXZLQkRDM2l6bXU4R2VJZDBNQlNhQT09'),
('CCHU9074',1,16,30,2,3,'https://hku.zoom.us/j/91517172449?pwd=RXppbW5ldVdZZ2JvWjlJV1FhM2pDQT09'),
('COMP2396',1,12,30,2,5,'https://hku.zoom.us/j/97902227890?pwd=QnlWWHdudGY0K21GeHhTa3JDQ3Urdz09'),
('CCCH9005',1,14,30,2,3,'https://hku.zoom.us/j/3531454530?pwd=VUpWMUhmck1yMjE5TUhuU0pGWHBmUT09'),
('PHYS3450',1,3,30,1,2,'https://zoom.us/j/8237642261#success'),
('PHYS3450',2,3,30,2,5,'https://zoom.us/j/8237642261#success'),
('PHYS2155',1,12,30,1,2,'https://zoom.us/j/4782746197#success'),
('PHYS2155',2,12,30,2,5,'https://zoom.us/j/4782746197#success');

INSERT INTO Tutorial (Course_ID, TutTime_HH, TutTime_MM, Weekday, Zoom) VALUES
('STAT4609',17,30,2,'https://hku.zoom.us/j/93095224906'),
('COMP3278',9,30,5,'https://hku.zoom.com.cn/j/2640918958?pwd=UmFpek1YMkUzNTFoL0ljRW84M1VLUT09'),
('MATH4602',14,30,5,'https://hku.zoom.us/j/99227888994?pwd=eXZLQkRDM2l6bXU4R2VJZDBNQlNhQT09'),
('CCHU9074',18,30,3,'https://hku.zoom.us/j/91517172449?pwd=RXppbW5ldVdZZ2JvWjlJV1FhM2pDQT09'),
('COMP2396',12,30,2,'https://hku.zoom.us/j/97902227890?pwd=QnlWWHdudGY0K21GeHhTa3JDQ3Urdz09'),
('CCCH9005',10,30,3,'https://hku.zoom.us/j/3531454530?pwd=VUpWMUhmck1yMjE5TUhuU0pGWHBmUT09');



/*
INSERT INTO ClassTimeZoom (Course_ID, ClassTime, Zoom) VALUES
('STAT4609', '10:30', 'https://hku.zoom.us/j/95828831639');
*/


/*
INSERT INTO FaceImages (ID, filename, mimetype) VALUES
();
*/