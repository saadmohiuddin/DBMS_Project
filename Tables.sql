CREATE TABLE Student (
  ID VARCHAR(10) NOT NULL,
  name VARCHAR(200) NOT NULL,
  email VARCHAR(50) NOT NULL,
  password VARCHAR(30) NOT NULL,
  PRIMARY KEY (ID)
);

CREATE TABLE LogIn (
  ID VARCHAR(10) NOT NULL,
  log_in_time TIMESTAMP NOT NULL,
  log_out_time TIMESTAMP NOT NULL,
  duration INT AS (TIMESTAMPDIFF(SECOND, log_in_time, log_out_time)),
  FOREIGN KEY (ID) REFERENCES Student (ID)
);

CREATE TABLE Course (
  Course_ID VARCHAR(8) NOT NULL,
  name VARCHAR(200) NOT NULL,
  info VARCHAR(2000) NOT NULL,
  teachers_message VARCHAR(2000) NOT NULL,
  path_to_materials VARCHAR(200),
  PRIMARY KEY (Course_ID)
);

CREATE TABLE Takes (
  ID VARCHAR(10) NOT NULL,
  Course_ID VARCHAR(8) NOT NULL,
  FOREIGN KEY (ID) REFERENCES Student (ID),
  FOREIGN KEY (Course_ID) REFERENCES Course (Course_ID)
);

CREATE TABLE Faculty (
  Faculty_ID VARCHAR(10) NOT NULL,
  name VARCHAR(200) NOT NULL, 
  lecturer BOOLEAN NOT NULL,
  email VARCHAR(50) NOT NULL,
  PRIMARY KEY (Faculty_ID)
);

CREATE TABLE Teaches (
  Course_ID VARCHAR(8) NOT NULL,
  Faculty_ID VARCHAR(10) NOT NULL,
  FOREIGN KEY (Faculty_ID) REFERENCES Faculty (Faculty_ID),
  FOREIGN KEY (Course_ID) REFERENCES Course (Course_ID)
);

CREATE TABLE Lecture (
  Course_ID VARCHAR(8) NOT NULL,
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
