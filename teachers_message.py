import PySimpleGUI as sg
import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="Mysql7-4", database="dbms")

mycursor = myconn.cursor()

mycursor.execute("SELECT Course_ID, teachers_message FROM Course")

myresult = mycursor.fetchall()

layout = [[sg.Text('Please input your course code:'), sg.Text(size=(15, 1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]
          ]

window = sg.Window("Teacher's Message", layout)

while True:  # Event Loop
    event, values = window.read()
    # print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        for x in myresult:
            if values['-IN-'].upper() == x[0]:
                # Update the "output" text element to be the teachers message
                window['-OUTPUT-'].update(x[1])
                break
        else:
            window['-OUTPUT-'].update('Course not found')

window.close()