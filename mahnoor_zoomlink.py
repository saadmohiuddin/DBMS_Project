import PySimpleGUI as sg
import os
import mysql.connector

query_zoom_lecture #Sql query here
query_zoom_tutorial #SQL query here

myconn = mysql.connector.connect(host="localhost",
        user="root", passwd="Mysql7-4",
        database="facerecognition")


def select_lecture(conn):
    conn.database = "facerecognition"
    mycursor = conn.cursor()
    mycursor.execute(query_zoom_lecture)
    return mycursor.fetchone()[0]

def select_tutorial(conn):
    conn.database = "facerecognition"
    mycursor = conn.cursor()
    mycursor.execute(query_zoom_tutorial)
    return mycursor.fetchone()[0]


zoom_link_lecture= select_lecture(myconn)


zoom_lecture_layout = [
            [sg.Listbox(
            values=[zoom_link_lecture], enable_events=True, size=(40, 20), key="zoomlink"
            )]
]

zoom_lecture_window = sg.Window("Zoom Lecture Link", zoom_lecture_layout) #incorporate this into overall window

while True:
    event,values = zoom_lecture_window.read()
    if event == "zoomlink":

        os.startfile(values[event][0])

    if event == sg.WIN_CLOSED:
        break

zoom_link_tutorial= select_tutorial(myconn)

zoom_tutorial_layout = [
            [sg.Listbox(
            values=[zoom_link_tutorial], enable_events=True, size=(40, 20), key="zoomlink"
            )]
]

zoom_tutorial_window = sg.Window("Zoom Tutorial Link", zoom_tutorial_layout) #incorporate this into overall window

while True:
    event,values = zoom_tutorial_window.read()
    if event == "zoomlink":

        os.startfile(values[event][0])

    if event == sg.WIN_CLOSED:
        break
