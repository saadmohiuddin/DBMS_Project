CREATE TABLE Student (
  ID VARCHAR(10) NOT NULL,
  name VARCHAR(40) NOT NULL,
  email VARCHAR(50) NOT NULL,
  log_in_time TIMESTAMP,
  log_out_time TIMESTAMP,
  duration INT AS (TIMESTAMPDIFF(SECOND, log_in_time, log_out_time)),
  PRIMARY KEY (ID)
);

CREATE TABLE StudentType (
  ID VARCHAR(10) NOT NULL,
  StudentType VARCHAR(10) NOT NULL,
  PRIMARY KEY (ID)
);

CREATE TABLE Course (
  Course_ID VARCHAR(8) NOT NULL,
  name VARCHAR(60) NOT NULL,
  info VARCHAR(300) NOT NULL,
  teachers_message VARCHAR(100) NOT NULL,
  path_to_materials VARCHAR(100),
  PRIMARY KEY (Course_ID)
);

CREATE TABLE Takes (
  ID VARCHAR(10) NOT NULL,
  Course_ID VARCHAR(8) NOT NULL,
  PRIMARY KEY (ID, Course_ID),
  FOREIGN KEY (ID) REFERENCES Student (ID),
  FOREIGN KEY (Course_ID) REFERENCES Course (Course_ID)
);

CREATE TABLE Faculty (
  Faculty_ID VARCHAR(10) NOT NULL,
  name VARCHAR(40) NOT NULL, 
  email VARCHAR(50) NOT NULL,
  office_address VARCHAR(6) NOT NULL,
  PRIMARY KEY (Faculty_ID)
);

CREATE TABLE Teaches (
  Course_ID VARCHAR(8) NOT NULL,
  Faculty_ID VARCHAR(10) NOT NULL,
  PRIMARY KEY (Course_ID, Faculty_ID),
  FOREIGN KEY (Faculty_ID) REFERENCES Faculty (Faculty_ID),
  FOREIGN KEY (Course_ID) REFERENCES Course (Course_ID)
);

CREATE TABLE Classes (
  Course_ID VARCHAR(8) NOT NULL,
  ClassID VARCHAR(2) NOT NULL,
  PRIMARY KEY (Course_ID, ClassID),
  FOREIGN KEY (Course_ID) REFERENCES Course (Course_ID)
);

CREATE TABLE Lecture (
  Course_ID VARCHAR(8) NOT NULL,
  ClassID VARCHAR(2) NOT NULL,
  Zoom VARCHAR(128) NOT NULL,
  PRIMARY KEY (Course_ID, ClassID),
  FOREIGN KEY (Course_ID) REFERENCES Course (Course_ID)
);

CREATE TABLE LectTime (
  Course_ID VARCHAR(8) NOT NULL,
  ClassID VARCHAR(2) NOT NULL,
  LectTime_HH INT NOT NULL,
  LectTime_Duration INT NOT NULL,
  Weekday INT NOT NULL,
  PRIMARY KEY (Course_ID, ClassID),
  FOREIGN KEY (Course_ID) REFERENCES Course (Course_ID)
);

CREATE TABLE Tutorial (
  Course_ID VARCHAR(8) NOT NULL,
  ClassID VARCHAR(2) NOT NULL,
  TutTime_HH INT NOT NULL,
  Weekday INT NOT NULL,
  Zoom VARCHAR(128),
  PRIMARY KEY (Course_ID, ClassID),
  FOREIGN KEY (Course_ID) REFERENCES Course (Course_ID)
);
