import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta


def execute_read_query(query):
    connection = mysql.connector.connect(host="localhost", user="root", passwd="Mysql7-4", database="dbms")
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def selectCourse():
    select_course = """
    SELECT Course_ID, name, info, teachers_message, GROUP_CONCAT(LectTime_Duration), GROUP_CONCAT(Lect_Weekday), GROUP_CONCAT(LectTime_HH), GROUP_CONCAT(LectTime_MM), Lect_Zoom, Tut_Weekday, TutTime_HH, TutTime_MM, Tut_Zoom
    FROM(SELECT DISTINCT C.*, L.LectTime_Duration, L.Weekday AS Lect_Weekday, L.LectTime_HH, L.LectTime_MM, L.Zoom AS Lect_Zoom, T.Weekday AS Tut_Weekday, T.TutTime_HH, T.TutTime_MM, T.Zoom AS Tut_Zoom
    FROM Course C, Lecture L, Tutorial T  
    WHERE C.Course_ID = L.Course_ID 
    AND C.Course_ID = T.Course_ID 
    AND L.Course_ID = T.Course_ID)query1
    GROUP BY Course_ID, name, info, teachers_message, Lect_Zoom, Tut_Weekday, TutTime_HH, TutTime_MM, Tut_Zoom
    """
    courses = execute_read_query(select_course)
    courseList = []
    for c in courses:
        course = {'code': c[0], "title": c[1], "lecture": [(c[4], (c[5], c[6], c[7]))],
                  "tutorial": (1, (c[9], c[10], c[11])), "zoom_link_lec": c[8], "zoom_link_tut": c[12],
                  "course_info": c[2], "teacher_msg": c[3]}
        courseList.append(course)

    print(courseList)


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


def checkClass():
    check_class = """
    SELECT ID, last_login, GROUP_CONCAT(Course_ID), GROUP_CONCAT(LectTime_HH), GROUP_CONCAT(LectTime_MM), 
    GROUP_CONCAT(Lect_Weekday), GROUP_CONCAT(TutTime_HH), GROUP_CONCAT(TutTime_MM), GROUP_CONCAT(Tut_Weekday)
    FROM(
    SELECT DISTINCT I.ID, MAX(I.log_in_time) as last_login, T.Course_ID, L.LectTime_HH, L.LectTime_MM, 
    L.Weekday as Lect_Weekday, Tut.TutTime_HH, Tut.TutTime_MM, Tut.Weekday as Tut_Weekday
    FROM LogIn I, Takes T, Lecture L, Tutorial Tut
    WHERE I.ID = T.ID
    AND T.Course_ID = L.Course_ID
    AND T.Course_ID = Tut.Course_ID
    AND L.Course_ID = Tut.Course_ID
    GROUP BY I.ID, T.Course_ID, L.LectTime_HH, L.LectTime_MM, L.Weekday, Tut.TutTime_HH, Tut.TutTime_MM, Tut.Weekday)query2
    GROUP BY ID, last_login
    """
    classes = execute_read_query(check_class)
    haveLec = []
    haveTut = []
    for c in classes:
        dayOfWeek = c[1].weekday()
        loginTime = c[1]
        course = c[2].split(",")
        lectHour = c[3].split(",")
        lectMin = c[4].split(",")
        lectDay = c[5].split(",")
        lectTime = []
        for i in range(len(lectHour)):
            lectTime.append(lectDay[i] + ',' + lectHour[i] + ',' + lectMin[i])
        for i in range(len(lectTime)):
            lect = lectTime[i].split(",")
            day = lect[0]
            if int(day) == dayOfWeek:
                time_str = lect[1] + lect[2]
                time = datetime.strptime(time_str, '%H%M').time()
                loginTimeEnd = loginTime + timedelta(hours=1)
                if time_in_range(loginTime.time(), loginTimeEnd.time(), time):
                    haveLec.append(course[i])

        TutHour = c[6].split(",")
        TutMin = c[7].split(",")
        TutDay = c[8].split(",")
        TutTime = []
        for i in range(len(TutHour)):
            TutTime.append(TutDay[i] + ',' + TutHour[i] + ',' + TutMin[i])
        for i in range(len(TutTime)):
            Tut = TutTime[i].split(",")
            day = Tut[0]
            if int(day) == dayOfWeek:
                time_str = Tut[1] + Tut[2]
                time = datetime.strptime(time_str, '%H%M').time()
                loginTimeEnd = loginTime + timedelta(hours=1)
                if time_in_range(loginTime.time(), loginTimeEnd.time(), time):
                    haveTut.append(course[i])
    print(haveLec)
    print(haveTut)


checkClass()
selectCourse()
