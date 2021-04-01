import PySimpleGUI as sg
import os
import mysql.connector

def notes(course_code):


    currentpath=os.getcwd()+"\\notes"

    pathdict = {"lecture":os.path.join(currentpath,course_code,"lecture"), "tutorial":os.path.join(currentpath,course_code,"tutorial"),
                "assignment":os.path.join(currentpath,course_code,"assignment")}

    notesdict={"lectures":os.listdir(pathdict["lecture"]), "tutorials":os.listdir(pathdict["tutorial"]),
                "assignments":os.listdir(pathdict["assignment"])}

    return notesdict,pathdict

#trial run of function notes(course_code)
if __name__ == '__main__':
    notesdict = notes("COMP3278")[0]
    pathdict = notes("COMP3278")[1]

    noteslayout = [

        [
            sg.Column(
                [
                    [sg.Text("Lecture Notes")],
                    [sg.Listbox(values=notesdict["lectures"], enable_events=True, size=(
                        40, 20), key="lecture_notelist")]
                ]
            ),

            sg.Column(
                [
                    [sg.Text("Tutorial Notes")],
                    [sg.Listbox(values=notesdict["tutorials"], enable_events=True, size=(
                        40, 20), key="tutorial_notelist")]
                ]
            ),

            sg.Column(
                [
                    [sg.Text("assignments")],
                    [sg.Listbox(values=notesdict["assignments"], enable_events=True, size=(
                        40, 20), key="assignments")]
                ]
            )

        ]
    ]

    #incorporate this into overall window
    noteswindow = sg.Window("Notes", noteslayout)

    while True:
        event, values = noteswindow.read()

        if event == "lecture_notelist":
            #opening pdf file
            os.system(os.path.join(pathdict["lecture"], values[event][0]))

        if event == "tutorial_notelist":
            os.system(os.path.join(pathdict["tutorial"], values[event][0]))

        if event == "assignments":
            os.system(os.path.join(pathdict["assignment"], values[event][0]))

        if event == sg.WIN_CLOSED:
            break
