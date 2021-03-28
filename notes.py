import PySimpleGUI as sg
import os
import mysql.connector

'''
query = "SELECT course_id FROM courses WHERE course_id = 'COMP3278' "
#query = "SELECT course_id FROM courses WHERE course_name ='Introduction to Database Management Systems' "

myconn = mysql.connector.connect(host="localhost", user="root", passwd="Mysql7-4", database="facerecognition")
def select_course(conn):
conn.database = "facerecognition"
mycursor = conn.cursor()
mycursor.execute(query)
return mycursor.fetchone()[0]

course_code= select_course(myconn)
'''

def notes(course_code):


    currentpath=os.getcwd()+"\\notes"

    pathdict = {"lecture":os.path.join(currentpath,course_code,"lecture"), "tutorial":os.path.join(currentpath,course_code,"tutorial"),
                "assignment":os.path.join(currentpath,course_code,"assignment")}

    notesdict={"lecture":os.listdir(pathdict["lecture"]), "tutorial":os.listdir(pathdict["tutorial"]),
                "assignment":os.listdir(pathdict["assignment"])}

    return notesdict,pathdict
    '''
    Lecturelist=os.listdir(path["lecture"]) #list of files from the chosen folder
    tutoriallist=os.listdir(path["tutorial"])
    assignmentlist=os.listdir(path["assignment"])
    '''


#trial run of function notes(course_code)
notesdict=notes("COMP3278")[0]
pathdict= notes("COMP3278")[1]

noteslayout =[

        [
            sg.Column(
                [
                        [sg.Text("Lecture Notes")],
                        [sg.Listbox(values=notesdict["lecture"], enable_events=True, size=(40, 20), key="lecture_notelist")]
                ]
            ),

            sg.Column(
                [
                    [sg.Text("Tutorial Notes")],
                    [sg.Listbox(values=notesdict["tutorial"], enable_events=True, size=(40, 20), key="tutorial_notelist")]
                ]
            ),

            sg.Column(
                [
                    [sg.Text("assignments")],
                    [sg.Listbox(values=notesdict["assignment"], enable_events=True, size=(40, 20), key="assignments")]
                ]
            )

        ]
]

noteswindow = sg.Window("Notes", noteslayout) #incorporate this into overall window

while True:
    event,values = noteswindow.read()

    if event == "lecture_notelist":
        os.system(os.path.join(pathdict["lecture"],values[event][0])) #opening pdf file

    if event == "tutorial_notelist":
        os.system(os.path.join(pathdict["tutorial"],values[event][0]))

    if event == "assignments":
        os.system(os.path.join(pathdict["assignment"],values[event][0]))


    if event == sg.WIN_CLOSED:
        break
