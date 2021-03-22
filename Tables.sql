CREATE TABLE Student (
  ID VARCHAR(10) NOT NULL,
  name VARCHAR(200) NOT NULL,
  welcome_message VARCHAR(2000) NOT NULL,
  PRIMARY KEY (ID)
);

CREATE TABLE LogIn (
  ID VARCHAR(10) NOT NULL,
  log_in_time TIMESTAMP NOT NULL,
  log_out_time TIMESTAMP NOT NULL,
  duration INT AS (TIMESTAMPDIFF(SECOND, log_in_time, log_out_time)),
  FOREIGN KEY (ID) REFERENCES Student (ID)
);

CREATE TABLE FaceImages (
  ID VARCHAR(10) NOT NULL,
  filename VARCHAR(128) NOT NULL,
  mimetype VARCHAR(64) NOT NULL,
  FOREIGN KEY (ID) REFERENCES Student (ID)
);

CREATE TABLE Course (
  Course_ID VARCHAR(8) NOT NULL,
  name VARCHAR(200) NOT NULL,
  info VARCHAR(2000) NOT NULL,
  teachers_message VARCHAR(2000) NOT NULL,
  PRIMARY KEY (Course_ID)
);

CREATE TABLE Takes (
  ID VARCHAR(10) NOT NULL,
  Course_ID VARCHAR(8) NOT NULL,
  FOREIGN KEY (ID) REFERENCES Student (ID),
  FOREIGN KEY (Course_ID) REFERENCES Course (Course_ID)
);

CREATE TABLE Lecture (
  Course_ID VARCHAR(8) NOT NULL,
  LectNo INT NOT NULL,
  LectTime_HH INT NOT NULL,
  LectTime_MM INT NOT NULL,
  LectTime_Duration INT NOT NULL,
  Weekday INT NOT NULL,
  Zoom VARCHAR(128) NOT NULL,
  FOREIGN KEY (Course_ID) REFERENCES Course (Course_ID)
);

CREATE TABLE Tutorial (
  Course_ID VARCHAR(8) NOT NULL,
  TutTime_HH INT,
  TutTime_MM INT,
  Weekday INT NOT NULL,
  Zoom VARCHAR(128),
  FOREIGN KEY (Course_ID) REFERENCES Course (Course_ID)
);

CREATE TABLE LectNotes (
  Course_ID VARCHAR(8) NOT NULL,
  LectNotePath VARCHAR(255) NOT NULL,  
  mimetype VARCHAR(64) NOT NULL,
  FOREIGN KEY (Course_ID) REFERENCES Course (Course_ID)
);

CREATE TABLE TutNotes (
  Course_ID VARCHAR(8) NOT NULL,
  TutNotePath VARCHAR(255) NOT NULL,  
  mimetype VARCHAR(64) NOT NULL,
  FOREIGN KEY (Course_ID) REFERENCES Course (Course_ID)
);

/*

### This wouldn't work if there were more than one file and 
### if there was lecture notes but no tutorial notes and vice versa.
### So I split it into two

CREATE TABLE ClassMaterials (
  Course_ID VARCHAR(8) NOT NULL,
  LectNotePath VARCHAR(128),
  TutNotePath VARCHAR(128),
  mimetype VARCHAR(64) NOT NULL,
  FOREIGN KEY (Course_ID) REFERENCES Course (Course_ID)
);
*/