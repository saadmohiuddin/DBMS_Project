import PySimpleGUI as sg
from datetime import datetime
import time

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
person = {
    "name": "Junaid Malik",
    "email": "junaidzm@connect.hku.hk",
}
date = datetime.now().strftime("at %H:%M:%S on %d %B, %Y")


def timetable(courses):
    """This function contains the main GUI logic for creating the timetable given
    #courses details courses."""
    data = [["{}:30 -\n{}:20".format(i, i + 1) if j == 0 else "" for j in range(0, 7)]
                                    for i in range(8, 20)]
    for k, v in courses.items():
        t = v["lecture"]
        for tup in t:
            i = 0
            while i < tup[0]:
                data[tup[1][1] - 8 +
                            i][tup[1][0]] = "Lecture\n{}".format(v["code"])
                i += 1

        tut_time = v["tutorial"]
        data[tut_time[1][1] -
            8][tut_time[1][0]] = "Tutorial\n{}".format(v["code"])
    header_list = ["Time", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    tt = [
        sg.Table(values=data,
                    justification='center',
                    enable_events=True,
                    display_row_numbers=False,
                    font='Courier 8',
                    key='_table_',
                    text_color='black',
                    headings=header_list,
                    max_col_width=23,
                    def_col_width=17,
                    background_color='#bfc4dc',
                    auto_size_columns=False,
                    row_height=30,
                    hide_vertical_scroll=True,
                    alternating_row_color="#cdb6cd",
                    num_rows=12,
                    header_text_color="white",
                    header_background_color="#505d9c",
                    header_font='Courier 9 bold',
                    pad=((20, 0), (1, 1))
                 )
    ]
    return tt

def draw_timetable_window(courses, user, login_time):
    """Draws timetable window uses user info user, courses details courses 
    and the login_time"""
    name = user["name"]
    date = login_time

    headline = [
        [
            sg.Column([[sg.Text("{}".format(name), font="Arial 14 bold",
                                    justification='left', size=(30, 1))]]),
            sg.Column([[sg.Text("Logged in: {}".format(date), font="Arial 10 italic",
                                    justification='right', size=(70, 1))]])
        ],
        [
            sg.Text("Welcome back, {}! You have no classes scheduled within at least an hour.".format(
                name), font="Arial 12", text_color="lightgrey", pad=((0, 0), (5, 5))),
            sg.Button("Logout", size=(10, 1), pad=((150, 10), (8, 8)),
                      font="Arial 9 bold", tooltip="Logout")
        ]
    ]

    line = [sg.Text(text="--------------------" * 9,
             font='Arial 12 bold',
             text_color='#cdb6cd',
             pad=((0, 0), (10, 10)),
            justification='center',
            size=(800, None))]

    layout3 = [
        headline[0],
        headline[1],
        line,
        [sg.Text(text="Your Weekly Schedule",
                 font='Arial 12 bold',
                 text_color='lightgrey',
                 pad=((0, 0), (10, 10)),
                justification='center',
                size=(800, None))],
        timetable(courses)

    ]

    # Create the window
    window3 = sg.Window("{}'s moodle".format(name),
                layout3, size=(900, 600))

    # Create an event loop
    while True:
        event3, values3 = window3.read()

        if event3 == sg.WIN_CLOSED or event3 == "Logout":
            window3.close()
            break

if __name__ == '__main__':
    draw_timetable_window(courses, person, date)
