import urllib
import numpy as np
import mysql.connector
import cv2
import pyttsx3
import pickle
from datetime import datetime
import sys
import PySimpleGUI as sg
myconn = mysql.connector.connect(host="localhost", user="root", passwd="Mysql7-4", database="facerecognition")
cursor = myconn.cursor()


def update_login_time(current_id):
    time = datetime.now()
    update =  "UPDATE student SET log_in_time=%s WHERE ID=%s"
    val = (str(time), current_id)
    cursor.execute(update, val)
    myconn.commit()

    return


def update_logout_time(current_id):
    time = datetime.now()
    update =  "UPDATE student SET log_out_time=%s WHERE ID=%s"
    val = (str(time), current_id)
    cursor.execute(update, val)
    myconn.commit()

    return
