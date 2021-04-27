import mysql.connector
from datetime import datetime
import PySimpleGUI as sg

myconn = mysql.connector.connect(
    host="localhost", user="root", passwd="MjzM1312!", database="facerecognition")
cursor=myconn.cursor()


def update_login_time(current_id):
    time = datetime.now()
    #time=datetime(2021,4,15,15,0,0) # for testing case:class in an hour
    update =  "UPDATE student SET log_in_time=%s WHERE ID=%s"
    val = (str(time), current_id)
    cursor.execute(update, val)
    myconn.commit()

    return time


def update_logout_time(current_id):
    time = datetime.now()
    update =  "UPDATE student SET log_out_time=%s WHERE ID=%s"
    val = (str(time), current_id)
    cursor.execute(update, val)
    myconn.commit()

    return time
