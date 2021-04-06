
from datetime import datetime
myconn = mysql.connector.connect(host="localhost", user="root",
        passwd="Mysql7-4", database="Tables")

#query_id for student ID

#query_log_in_time for log_in_time

#query_lecture_time for lecture times (HH:MM) of all lectures where ID of logged in
# student AND where weekday = log_in_time

#query_tutorial_time for tutorial times (HH:MM) of all tutorials where ID of logged in
# student AND where where weekday = log_in_time

def select_ID(conn):
    conn.database = "Tables"
    mycursor = conn.cursor()
    mycursor.execute(query_id)
    return mycursor.fetchall()

def select_log_in_time(conn):
    conn.database = "Tables"
    mycursor = conn.cursor()
    mycursor.execute(query_log_in_time)
    return mycursor.fetchall()

ID= select_ID(myconn)
log_in_time = select_log_in_time(myconn)


def check_class(ID, log_in_time):
    conn.database = "Tables"
    mycursor = conn.cursor()
    mycursor.execute(query_lecture_time)
    lecture_times = [i[0] for i in mycursor.fetchall()]
    mycursor.execute(query_tutorial_time)
    tutorial_times = [i[0] for i in mycursor.fetchall()]
    classes_time = lecture_times + tutorial_times
    classes_time.sort(key=lambda date: datetime.strptime(date, "%H:%M"))
    next_class_time = min(time for time in classes_time if time >= log_in_time)
    time_to_class = next_class_time - log_in_time #in hh:mm

    if time_to_class <= '01:00' :
        return (True, course_id) #and all information of that particular course.

    else:
        return (False, timetable)
