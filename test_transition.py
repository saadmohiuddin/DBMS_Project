import PySimpleGUI as sg

from timetable import draw_timetable_window
from mainWindowGUI import draw_course_window

sg.theme('DarkBlue6')

courses = {
    "COMP3278": {
        "code": "COMP3278",
        "title": "Introduction to database management systems",
        "lecture": [(2, (5, 9, 30))],
        "tutorial": (1, (2, 9, 30))
    },
    "MATH2012": {
        "code": "MATH2012",
        "title": "Fundamental concepts",
        "lecture": [(2, (4, 12, 30)), (1, (1, 12, 30))],
        "tutorial": (1, (1, 4, 30))
    }
}

course = {
    "code": "COMP3278",
    "title": "Capstone experience for statistics undergraduates",
    "course_info": "This course studies the principles, design, administration, and implementation of database management systems. Topics include: entity-relationship model, relational model, relational algebra, database design and normalization, database query languages, indexing schemes, integrity and concurrency control.",
    # there can be more than one lecture (duration, (day_number, starting_hour, starting_min))
    "lecture": [(2, (5, 9, 30)), (1, (3, 9, 30))],
    "tutorial": (1, (2, 9, 30)), #there can only be one tutorial
    "zoom_link_lec": "https://hku.zoom.us/j/97686555806?pwd=NWxSNVRKTlNDU0NjYTgremxaQ3pldz09",
    "zoom_link_tut": "https://hku.zoom.com.cn/j/2640918958?pwd=UmFpek1YMkUzNTFoL0ljRW84M1VLUT09",
    "teacher_msg": "There will be 6 or 7 assignments. Problem sets will be assigned on Friday. Completed problem sets are due on the following Sunday. No problem sets will be accepted after the solutions have been posted.",
    #(name, office_address, email_id)
    "lecturer": ("Dr. Ping Luo", "CB326", "pluo@cs.hku.hk")
}

person = {
    "name": "Junaid Malik",
    "email": "junaidzm@connect.hku.hk",
}


name = "Junaid Malik"

from datetime import datetime
date = datetime.now().strftime("at %H:%M:%S on %d %B, %Y")

line1 = [sg.Text(text="--------------------" * 9,
         font='Arial 12 bold',
         text_color='#cdb6cd',
         pad=((0, 0), (145, 0)),
    justification='center',
    size=(800, None))]
line2 = [sg.Text(text="--------------------" * 9,
         font='Arial 12 bold',
         text_color='#cdb6cd',
         pad=((0, 0), (0, 100)),
    justification='center',
    size=(800, None))]

transition_layout = [
    [
        sg.Column([[sg.Text("You have logged in successfully, {}!".format(name), font="Arial 14 bold",
                justification='left')]]),
        sg.Column([[sg.Text("Logged in: {}".format(date), font="Arial 10 italic",
                justification='right', size=(70, 1))]])
    ],

    line1,
    [sg.Text("HKU MOODLE 2.0", font="Arial 65 italic",
             text_color="lightgrey", pad=((70, 50), (10, 10)))], line2,

    [sg.Button("Continue", size=(10, 2), pad=((650, 30), (80, 8)), font="Arial 9 bold"),
               sg.Button("Logout", size=(10, 2), pad=((0, 10), (80, 8)), font="Arial 9 bold")]
]

transition_window = sg.Window("{}'s moodle".format(
    name), transition_layout, size=(900, 600))
#cv2.destroyAllWindows() # Try to close once we open the next one for smoother transition
while True:
    t_event,t_values=transition_window.read()
    if t_event == sg.WIN_CLOSED or t_event=="Logout":
        update_logout_time(current_id)
        break
    if t_event == "Continue":
        transition_window.close()
        #draw_course_window(course, person, date)
        draw_timetable_window(courses, person, date)
        break