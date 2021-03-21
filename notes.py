import PySimpleGUI as sg
import os
import mysql.connector

query = "SELECT course_id FROM courses WHERE course_id = 'COMP3278' "
#query = "SELECT course_id FROM courses WHERE course_name ='Introduction to Database Management Systems' "

myconn = mysql.connector.connect(host="localhost", user="root", passwd="Mysql7-4", database="facerecognition")
def select_course(conn):
    conn.database = "facerecognition"
    mycursor = conn.cursor()
    mycursor.execute(query)
    return mycursor.fetchone()[0]

course_code= select_course(myconn)

currentpath=os.getcwd()+"\\notes"
path = os.path.join(currentpath,course_code)

Lecturelist=os.listdir(path) #list of files from the chosen folder

noteslayout = [
            [sg.Listbox(
            values=Lecturelist, enable_events=True, size=(40, 20), key="lecture_notelist"
            )],
            [sg.Listbox(
            values=Lecturelist, enable_events=True, size=(40, 20), key="tutorial_notelist"
            )],
            [sg.Listbox(
            values=Lecturelist, enable_events=True, size=(40, 20), key="assignments"
            )]
]

noteswindow = sg.Window("Notes", noteslayout) #incorporate this into overall window

while True:
    event,values = noteswindow.read()

    if event == "lecture_notelist":

        os.system(os.path.join(path,values[event][0])) #opening pdf file

    if event == sg.WIN_CLOSED:
        break
