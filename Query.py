import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta
from update_login_logout import myconn



def execute_read_query(query):
    connection = myconn #mysql.connector.connect(
        #host="localhost", user="root", passwd="MjzM1312!", database="facerecognition")
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def getUser(userid):
    select_user = "SELECT name, email FROM Student WHERE ID='%s'" % userid
    user = execute_read_query(select_user)
    if user:
        person = {
             'name': user[0][0], 'email': user[0][1]
        }
        return person
    else:
        return


"""
>>> getUser(3035445364)
{'userID': '3035445364', 'name': 'Saalim Mohamed Abdulla', 'email': 'mistermiyagi15973@gmail.com'}
"""


def selectCourse(course):
    select_course = """
    SELECT Course_ID, name, info, teachers_message, GROUP_CONCAT(LectTime_Duration), GROUP_CONCAT(Lect_Weekday),
    GROUP_CONCAT(LectTime_HH), Lect_Zoom, Tut_Weekday, TutTime_HH, Tut_Zoom, lecturer, office_address, email
    FROM(SELECT DISTINCT C.*, L.LectTime_Duration, L.Weekday AS Lect_Weekday, L.LectTime_HH,
    Lec.Zoom AS Lect_Zoom, T.Weekday AS Tut_Weekday, T.TutTime_HH, T.Zoom AS Tut_Zoom, F.name AS lecturer,
    F.office_address, F.email
    FROM Course C, LectTime L, Tutorial T, Lecture Lec, Faculty F, Teaches Tea
    WHERE C.Course_ID = L.Course_ID
    AND C.Course_ID = T.Course_ID
    AND C.Course_ID = Lec.Course_ID
    AND C.Course_ID = Tea.Course_ID
    AND F.Faculty_ID = Tea.Faculty_ID)query1
    WHERE Course_ID ='%s'
    GROUP BY Course_ID, name, info, teachers_message, Lect_Zoom, Tut_Weekday, TutTime_HH, Tut_Zoom, lecturer,
    office_address, email
    """ % course

    c = execute_read_query(select_course)
    lectDuration = c[0][4].split(",")
    lectDay = c[0][5].split(",")
    lectHour = c[0][6].split(",")
    lectTime = []
    for i in range(len(lectHour)):
        time = lectDuration[i] + ',(' + lectDay[i] + ',' + lectHour[i] + ',' + '30' + ')'
        lectTime.append(time)
    res = list(map(eval, lectTime))
    course = {'code': c[0][0], "title": c[0][1], "lecture": res,
              "tutorial": (1, (c[0][8], c[0][9], 30)), "zoom_link_lec": c[0][7], "zoom_link_tut": c[0][10],
              "course_info": c[0][2], "teacher_msg": c[0][3], 'lecturer': (c[0][11], c[0][12], c[0][13])}

    return course


"""
>>> selectCourse('STAT4609')
{'code': 'STAT4609',
'title': 'Big Data Analytics',
'lecture': [(3, (4, 13, 30))],
'tutorial': (1, (2, 17, 30)),
'zoom_link_lec': 'https://hku.zoom.us/j/95828831639',
'zoom_link_tut': 'https://hku.zoom.us/j/93095224906',
'course_info': 'In the past decade, huge volume of data with highly complicated structure has appeared in every aspect,
such as social web logs, e-mails, video, speech recordings, photographs, tweets and others. The efficient extraction of
valuable information from these data sources becomes a challenging task. This course focuses on the practical knowledge
and skills of some advanced analytics and statistical modeling for solving big data problems.',
'teacher_msg': 'Consuming food or beverages of any kind is strictly prohibited during class times. Messes with my flow.
Thank you for your understanding.',
'lecturer': ('Zanila Zhao', 'hku', 'historia15973@gmail.com')}
"""


def selectAllCourses(userid):
    select_courses = """
    SELECT Course_ID, name, GROUP_CONCAT(LectTime_Duration), GROUP_CONCAT(Lect_Weekday),
    GROUP_CONCAT(LectTime_HH), Tut_Weekday, TutTime_HH
    FROM(SELECT DISTINCT C.*, L.LectTime_Duration, L.Weekday AS Lect_Weekday, L.LectTime_HH,
    T.Weekday AS Tut_Weekday, T.TutTime_HH
    FROM Course C, LectTime L, Tutorial T, Takes Ta
    WHERE C.Course_ID = L.Course_ID
    AND C.Course_ID = T.Course_ID
    AND C.Course_ID = Ta.Course_ID
    AND Ta.ID = '%s')query1
    GROUP BY Course_ID, name, Tut_Weekday, TutTime_HH
    """ % userid
    courses = execute_read_query(select_courses)
    courseList = {}
    for c in courses:
        lectDuration = c[2].split(",")
        lectDay = c[3].split(",")
        lectHour = c[4].split(",")
        lectTime = []
        for i in range(len(lectHour)):
            time = lectDuration[i] + ',(' + lectDay[i] + ',' + lectHour[i] + ',' + '30' + ')'
            lectTime.append(time)
        res = list(map(eval, lectTime))

        course = {'code': c[0], "title": c[1], "lecture": res,
                  "tutorial": (1, (c[5], c[6], 30))}
        courseList[course['code']]=course

    return courseList


"""
Output:
[{'code': 'CCCH9005', 'title': 'Chinese Cultural Revolution', 'lecture': [(2, (3, 14, 30))], 'tutorial': (1, (3, 10, 30))},
{'code': 'CCHU9074', 'title': 'Beyond Fake News', 'lecture': [(2, (3, 16, 30))], 'tutorial': (1, (3, 18, 30))},
{'code': 'COMP2396', 'title': 'OOP with Java', 'lecture': [(2, (5, 12, 30))], 'tutorial': (1, (2, 12, 30))},
{'code': 'COMP3278', 'title': 'Introduction to database management systems', 'lecture': [(2, (2, 9, 30))], 'tutorial': (1, (5, 9, 30))},
{'code': 'MATH4602', 'title': 'Scietific Computing', 'lecture': [(2, (1, 9, 30)), (1, (4, 9, 30))], 'tutorial': (1, (5, 14, 30))},
{'code': 'STAT4609', 'title': 'Big Data Analytics', 'lecture': [(3, (4, 13, 30))], 'tutorial': (1, (2, 17, 30))}]
"""


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


def checkClass(userid):
    check_class = """
    SELECT last_login, GROUP_CONCAT(Course_ID), GROUP_CONCAT(LectTime_HH), GROUP_CONCAT(Lect_Weekday),
    GROUP_CONCAT(TutTime_HH), GROUP_CONCAT(Tut_Weekday)
    FROM(
    SELECT DISTINCT S.log_in_time as last_login, T.Course_ID, L.LectTime_HH,
    L.Weekday as Lect_Weekday, Tut.TutTime_HH, Tut.Weekday as Tut_Weekday
    FROM Student S, Takes T, LectTime L, Tutorial Tut
    WHERE S.ID = T.ID
    AND S.ID = '%s'
    AND T.Course_ID = L.Course_ID
    AND T.Course_ID = Tut.Course_ID)query2
    GROUP BY last_login
    """ % userid
    classes = execute_read_query(check_class)
    #print(classes,"\n\n\n")
    haveClass = []
    for c in classes:
        dayOfWeek = c[0].weekday()+1
        loginTime = c[0]
        course = c[1].split(",")
        #print("course=", course)
        lectHour = c[2].split(",")
        lectDay = c[3].split(",")
        tutHour = c[4].split(",")
        tutDay = c[5].split(",")
        classTime = []
        for i in range(len(lectHour)):
            classTime.append(lectDay[i] + ',' + lectHour[i] + ',' + '30')
        for i in range(len(tutHour)):
            classTime.append(tutDay[i] + ',' + tutHour[i] + ',' + '30')
            #workaround to include entries for course for each tuthour
            course.append(c[1].split(",")[i])
        #print("\n updated course=",course)
        for i in range(len(classTime)):
            class_time = classTime[i].split(",")
            #print("classtime[%s]="%i,class_time, course[i])
            day = class_time[0]
            if int(day) == dayOfWeek:
                time_str = class_time[1] + class_time[2]
                time = datetime.strptime(time_str, '%H%M').time()
                #print("\n",time)
                loginTimeEnd = loginTime + timedelta(hours=1)
                if time_in_range(loginTime.time(), loginTimeEnd.time(), time):
                    haveClass.append(course[i])

    return haveClass



"""
>>> checkClass(3035445364)
Returns list of course_id of courses with lectures or tutorials within 1 hr for user with userid = 3035445364
e.g. ['STAT4609']
"""
