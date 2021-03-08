INSERT INTO Student (ID, name, welcome_message) VALUES 
(1, 'Saalim Mohamed Abdulla', 'Welcome back! Check out your courses and keep up with your timetable!');

INSERT INTO LogIn (ID, log_in_time, log_out_time) VALUES
(1, '2021-03-08 09:01:00', '2021-03-08 09:05:00');

INSERT INTO Course (Course_ID, name, info, teachers_message) VALUES
('STAT4609', 'Big Data Analytics', 'In the past decade, huge volume of data with highly complicated structure has appeared in every aspect, such as social web logs, e-mails, video, speech recordings, photographs, tweets and others. The efficient extraction of valuable information from these data sources becomes a challenging task. This course focuses on the practical knowledge and skills of some advanced analytics and statistical modeling for solving big data problems.',
 'Consuming food or beverages of any kind is strictly prohibited during class times. Messes with my flow. Thank you for your understanding.'
 );
 
INSERT INTO Takes (ID, Course_ID) VALUES
(1, 'STAT4609');

INSERT INTO ClassTimeZoom (Course_ID, ClassTime, Zoom) VALUES
('STAT4609', '09:47', 'https://hku.zoom.us/j/95828831639');

/*
INSERT INTO ClassLectNotes (Course_ID, LectNotePath, mimetype) VALUES
('STAT4609',);

INSERT INTO ClassLectNotes (Course_ID, TutNotePath, mimetype) VALUES
('STAT4609',);
*/

/*
INSERT INTO FaceImages (ID, filename, mimetype) VALUES
();
*/