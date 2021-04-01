import urllib
import numpy as np
import mysql.connector
import cv2
import pyttsx3
import pickle
from datetime import datetime
import sys
import PySimpleGUI as sg
from update_login_logout import update_login_time, update_logout_time
from timetable import draw_timetable_window
from mainWindowGUI import draw_course_window


# 1 Create database connection
myconn = mysql.connector.connect(host="localhost", user="root", passwd="Mysql7-4", database="facerecognition")
date = datetime.utcnow()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
cursor = myconn.cursor()


#2 Load recognize and read label from model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("train.yml")

labels = {"person_name": 1}
with open("labels.pickle", "rb") as f:
    labels = pickle.load(f)
    labels = {v: k for k, v in labels.items()}

# create text to speech
engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", 175)

# Define camera and detect face
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)


# 3 Define pysimplegui setting
layout =  [
    [sg.Text('Setting', size=(18,1), font=('Any',18),text_color='#1c86ee' ,justification='left')],
    [sg.Text('Confidence'), sg.Slider(range=(0,100),orientation='h', resolution=1, default_value=60, size=(15,15), key='confidence')],
    [sg.OK(), sg.Cancel()]
      ]
win = sg.Window('Attendance System',
        default_element_size=(21,1),
        text_justification='right',
        auto_size_text=False).Layout(layout)
event, values = win.Read()
if event is None or event =='Cancel':
    exit()
args = values
gui_confidence = args["confidence"]
win_started = False

# 4 Open the camera and start face recognition
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        print(x, w, y, h)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        # predict the id and confidence for faces
        id_, conf = recognizer.predict(roi_gray)

        # If the face is recognized
        if conf >= gui_confidence:
            # print(id_)
            # print(labels[id_])
            font = cv2.QT_FONT_NORMAL
            #id = 0
            #id += 1
            #name = labels[id_]
            id=labels[id_]
            current_id = id
            color = (255, 0, 0)
            stroke = 2
            cv2.putText(frame, id, (x, y), font, 1, color, stroke, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))

            # Find the student information in the database.
            #select = "SELECT ID, name, DAY(login_date), MONTH(login_date), YEAR(login_date) FROM Student WHERE name='%s'" % (name)
            select = "SELECT ID, name FROM student WHERE ID='%s'" % (id)
            name = cursor.execute(select)
            result = cursor.fetchall()
            # print(result)
            data = "error"

            for x in result:
                data = x

            # If the student's information is not found in the database
            if data == "error":
                # the student's data is not in the database
                print("The ID", current_id, "is NOT FOUND in the database.")

            # If the student's information is found in the database
            else:
                """
                Implement useful functions here.
                Check the course and classroom for the student.
                    If the student has class room within one hour, the corresponding course materials
                        will be presented in the GUI.
                """
                update_login_time(current_id) #If this is the case, then we need to keep only the latest login details in DB
                #print(data)

                # Need to call another MySQL query that gives the email_id as well in addition to what is contained in variable data
                #user = {"id" : , "email" : , "name": }
                transition_layout=[[sg.Text("You have logged in successfully, " + data[1])], [sg.Button("Continue")], [sg.Button("Logout")]]
                transition_window = sg.Window("Transition", transition_layout, size=(400, 300))
                cv2.destroyAllWindows() # Try to close once we open the next one for smoother transition
                while True:
                    t_event,t_values=transition_window.read()
                    if t_event == sg.WIN_CLOSED or t_event=="Logout":
                        update_logout_time(current_id)
                        break

                    if t_event =="Continue":
                        # all_classes = sql query by Van
                        # has_class = mahnoor_function(all_classes)
                        # if has_class[0]:
                        #   course = get_full_course_details(has_class[1])
                        #   draw_course_window(course, user, login_time, transition_window)
                        # else:
                        #   draw_timetable_window(all_classes, user, login_time, transition_window)
                        #
                        # logout_time = date.now()
                        update_logout_time(current_id)
                        break


                """
                    if the student does not have class at the moment, the GUI presents a personal class
                        timetable for the student.

                """

                #update =  "UPDATE Login SET log_in_time=%s WHERE ID=%s"
                #val = (str(now), current_id)
                #cursor.execute(update, val)
                #update = "UPDATE Student SET login_time=%s WHERE name=%s"
                #val = (current_time, current_name)
                #cursor.execute(update, val)
                #myconn.commit()

                #hello = ("Hello "+ current_id+ ". You logged in")
                #print(hello)
                #engine.say(hello)


        # If the face is unrecognized
        else:
            color = (255, 0, 0)
            stroke = 2
            font = cv2.QT_FONT_NORMAL
            cv2.putText(frame, "UNKNOWN", (x, y), font, 1, color, stroke, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))
            hello = ("Your face is not recognized")
            print(hello)
            engine.say(hello)
            # engine.runAndWait()

    # GUI
    imgbytes = cv2.imencode('.png', frame)[1].tobytes()
    if not win_started:
        win_started = True
        layout = [
            [sg.Text('Attendance System Interface', size=(30,1))],
            [sg.Image(data=imgbytes, key='_IMAGE_')],
            [sg.Text('Confidence'),
                sg.Slider(range=(0, 100), orientation='h', resolution=1, default_value=60, size=(15, 15), key='confidence')],
            [sg.Exit()]
        ]
        win = sg.Window('Attendance System',
                default_element_size=(14, 1),
                text_justification='right',
                auto_size_text=False).Layout(layout).Finalize()
        image_elem = win.FindElement('_IMAGE_')
    else:
        image_elem.Update(data=imgbytes)

    event, values = win.Read(timeout=20)
    if event is None or event == 'Exit':
        break
    gui_confidence = values['confidence']


win.Close()
cap.release()
