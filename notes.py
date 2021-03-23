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
path = {"lecture":os.path.join(currentpath,course_code,"lecture"), "tutorial":os.path.join(currentpath,course_code,"tutorial"),
            "assignment":os.path.join(currentpath,course_code,"assignment")}

Lecturelist=os.listdir(path["lecture"]) #list of files from the chosen folder
tutoriallist=os.listdir(path["tutorial"])
assignmentlist=os.listdir(path["assignment"])

noteslayout =[

        [
            sg.Column(
                [
                        [sg.Text("Lecture Notes")],
                        [sg.Listbox(values=Lecturelist, enable_events=True, size=(40, 20), key="lecture_notelist")]
                ]
            ),

            sg.Column(
                [
                    [sg.Text("Tutorial Notes")],
                    [sg.Listbox(values=tutoriallist, enable_events=True, size=(40, 20), key="tutorial_notelist")]
                ]
            ),

            sg.Column(
                [
                    [sg.Text("assignments")],
                    [sg.Listbox(values=assignmentlist, enable_events=True, size=(40, 20), key="assignments")]
                ]
            )

        ]
]

noteswindow = sg.Window("Notes", noteslayout) #incorporate this into overall window

while True:
    event,values = noteswindow.read()

    if event == "lecture_notelist":
        os.system(os.path.join(path["lecture"],values[event][0])) #opening pdf file

    if event == "tutorial_notelist":
        os.system(os.path.join(path["tutorial"],values[event][0]))

    if event == "assignments":
        os.system(os.path.join(path["assignment"],values[event][0]))


    if event == sg.WIN_CLOSED:
        break
