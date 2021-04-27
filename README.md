# Face Recognition

Face recognition using python and mysql.

*******

## Usage

### Environment

Create virtual environment using Anaconda.
```
conda create -n face python=3.x
conda activate face
pip install -r requirements.txt
```

### MySQL Install

[Mac](https://dev.mysql.com/doc/mysql-osx-excerpt/5.7/en/osx-installation-pkg.html)

[Ubuntu](https://dev.mysql.com/doc/mysql-linuxunix-excerpt/5.7/en/linux-installation.html)

[Windows](https://dev.mysql.com/downloads/installer/)

You'll obtain an account and password after installation, then you should modify `update_login_logout.py`, with the corresponding
`user` and `passwd`:
```
# create database connection
myconn = mysql.connector.connect(host="localhost", user="root", passwd="xxxxx", database="facerecognition")
```

*******

## Run

### 1. Face Recognition

#### 1.1 Collect Face Data
```
"Make these user_name changes within the file"
"""
user_name = "3033333333"   # UID
NUM_IMGS = 400       # the number of saved images
"""
python face_capture.py
```
The camera will be activated and the captured images will be stored in `data/3033333333` folder.      
**Note:** Only one person’s images can be captured at a time.

#### 1.2 Train a Face Recognition Model
```
python train.py
```
`train.yml` and `labels.pickle` will be created at the current folder.



### 2. Database Design

#### 2.1 Define Database
**You need to** add your information to `facerecognition.sql` to insert data into the tables Student and Takes. You can also add the relevant data for the courses you're taking into the relevant tables such as Courses etc.

Here is a sample code for `Student`.
```
INSERT INTO Student (ID, name, email, log_in_time, log_out_time) VALUES
('3033333333','Bob','bob@gmail.com','2021-03-08 09:01:00','2021-03-08 09:05:00');
```

#### 2.2 Import Database
Open mysql server and import the file `facerecognition.sql`.
```
# login the mysql command (or either login with MySQL Command Line Client)
mysql -u root -p

# create database.  'mysql>' indicates we are now in the mysql command line
mysql> CREATE DATABASE facerecognition;
mysql> USE facerecognition;

# import from sql file (try using the full name (including path) <fullpath>\facerecognition.sql, if this command does not work this way)
mysql> source facerecognition.sql
```
#### 2.3 Add course notes files
```
For adding notes of a new course:
1. Make a folder with the name corresponding to the Course_id
2. Make subfolders named "assignment", "lecture" and "tutorial"
3. Add pdf files corresponding to the subfolders

```

### 3. Login Interface

#### 3.1 PySimpleGUI GUI
```
python faces_gui.py
```
The camera will be activated and recognize your face using the pretrained model.
This will open up the python GUI for the student portal Moodle 2.0.
