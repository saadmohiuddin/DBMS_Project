import PySimpleGUI as sg
from datetime import datetime
import time
from send_email import send_email
from notes import notes
import os
import subprocess
import webbrowser
from Query import selectCourse

sg.theme('DarkBlue6')

default_frame_border_width = 2,
default_frame_title_color = 'white',
default_frame_font = "Arial 9 bold"
default_frame_pad = ((20, 10), (8, 8))
default_frame_element_justification = 'left'
number_to_days = ["", "Monday", "Tuesday",
    "Wednesday", "Thursday", "Friday", "Saturday"]

date = datetime.now().strftime("at %H:%M:%S on %d %B, %Y")

person = {
    "name": "Junaid Malik",
    "email": "junaidzm@connect.hku.hk",
}


def lecturer_layout(course):
    bold_text = "Arial 12 bold"
    simple_text = "Arial 12"
    text_color = "white"
    lecturer_info = [
        sg.Column([[sg.Text("Name:", font=bold_text,
                    justification='left', size=(5, 1), text_color=text_color)]]),
        sg.Column([[sg.Text("{}".format(course["lecturer"][0]), font=simple_text,
                justification='left', size=(12, 1), text_color=text_color)]]),
        sg.Column([[sg.Text("Email:", font=bold_text,
                justification='right', size=(6, 1), text_color=text_color)]]),
        sg.Column([[sg.Text("{}".format(course["lecturer"][2]), font=simple_text,
                    justification='left', size=(18, 1), text_color=text_color)]]),
        sg.Column([[sg.Text("Office address: ", font=bold_text,
                justification='right', size=(15, 1), text_color=text_color)]]),
        sg.Column([[sg.Text("{}".format(course["lecturer"][1]), font=simple_text,
                justification='left', size=(8, 1), text_color=text_color)]])
    ]

    teacher_msg = [
        sg.Column([[sg.Text("Message:", font=bold_text,
                    justification='left', size=(8, 1), text_color="white")]]),
        sg.Column([[sg.Text("{}".format(course["teacher_msg"]), font="Arial 11",
                            justification='left', size=(74, 2), text_color="white")]])
    ]

    lecturer_frame = [
        sg.Frame("Lecturer's information", [
            lecturer_info, teacher_msg],
            size=(100, 100),
            element_justification=default_frame_element_justification,
            pad=default_frame_pad,
            border_width=default_frame_border_width,
            title_color=default_frame_title_color,
            font=default_frame_font)
    ]
    return lecturer_frame

def course_materials_layout(course_materials):
    pad_inner = ((3, 5), (4, 4))
    size_listbox = (30, 5)
    frames = []
    types = ["lectures", "tutorials", "assignments"]
    for f in types:
        frames.append(
            [
                sg.Frame(f.capitalize(), [
                    [sg.Listbox(values=list(
                        map(lambda s: s[:-4], course_materials[f])),
                        size=size_listbox, key=f"{f}_list", enable_events=True,
                        font="Arial 9 bold italic",
                        tooltip=f"Open {f.strip('s')}\nmaterials")]
                ],
                    element_justification='left',
                    pad=pad_inner,
                    border_width=1,
                    font="Arial 9 bold"
                )
            ]
        )
    notes_layout_col_pad=((5, 10), (2, 2))
    main_frame_layout=[]
    for frame in frames:
        main_frame_layout.append(
            sg.Column([frame], pad=notes_layout_col_pad)
        )
    notes_layout = [

        sg.Frame("Course materials", [main_frame_layout],
            element_justification=default_frame_element_justification,
            pad=default_frame_pad,
            size=(100, 100),
            border_width=default_frame_border_width,
            title_color=default_frame_title_color,
            font=default_frame_font)
    ]
    return notes_layout

def zoom_link_layout(course):
    bold_text = "Arial 12 bold"
    simple_text = "Arial 12"
    size_of_heading = (17, 2)
    size_of_link = (64, 2)
    result = [
        sg.Frame("Zoom links", [[sg.Column([[sg.Text("Zoom link for lectures:", font=bold_text,
                text_color="lightblue", justification='left', size=size_of_heading)],
                [sg.Text("Zoom link for tutorials:", font=bold_text, text_color="#fd7698",
                        justification='left', size=size_of_heading)]]),
            sg.Column([[sg.Text(course["zoom_link_lec"], font=simple_text + " underline",
                        justification='left', size=size_of_link, text_color="#787afb",
                        enable_events=True, key="-LEC_ZOOM-", tooltip="Lecture zoom link")],
                       [sg.Text(course["zoom_link_tut"], font=simple_text + " underline",
                        justification='left', size=size_of_link, text_color="#787afb",
                        enable_events=True, key="-TUT_ZOOM-", tooltip="Tutorial zoom link")]
                       ])]],
            size=(100, 100),
            element_justification=default_frame_element_justification,
            pad=default_frame_pad,
            border_width=default_frame_border_width,
            title_color=default_frame_title_color,
            font=default_frame_font
                 )
    ]
    return result

def get_headline(course, name, date):
    headline = [
        [
            sg.Column([[sg.Text("{}".format(name), font="Arial 14 bold",
                    justification='left', size=(30, 1))]]),
            sg.Column([[sg.Text("Logged in: {}".format(date), font="Arial 10 italic",
                    justification='right', size=(70, 1))]])
        ],

        [
            sg.Text("{}: {}".format(course["code"], course["title"]), font="Arial 14 bold", text_color="white",
                            justification='left', size=(50, 1), pad=((0, 0), (8, 0)))
        ],

        [
            sg.Text("Welcome back, {}! You have a class of {} scheduled within an hour.".format(
                name, course["code"]), font="Arial 12", text_color="lightgrey", pad=((2, 0), (1, 3))),
            sg.Button("Logout", size=(10, 1), pad=((120, 10), (0, 0)),
                      font="Arial 9 bold", enable_events=True, key="-LOGOUT-", tooltip="Logout")
        ],
        [
            sg.Text("{}".format(course["course_info"]), font="Arial 9 italic",
                    text_color="lightgrey", size=(115, 3), pad=((6, 0), (0, 3)))
        ]
    ]
    return headline

def draw_course_window(course, user, login_time):
    """Draws timetable window using user info given by user, 
    course full details in dict course and the login_time timestamp.
    """
    
    name = user["name"]
    date = login_time

    course_materials, pathdict = notes(course["code"])

    # get latest materials and their fullpaths (to be used with send_email())
    fullpaths = []
    nameonly = []
    for t in ["lectures", "assignments", "tutorials"]:
        if len(course_materials[t]) > 0:
            fullpaths.append(f"{pathdict[t[:-1]]}\\{sorted(course_materials[t])[-1]}")
            nameonly.append(sorted(course_materials[t])[-1])

    # Create layouts
    headline = get_headline(course, name, date)
    notes_frame = course_materials_layout(course_materials)
    lecturer_frame = lecturer_layout(course)
    zoom_link_frame = zoom_link_layout(course)

    name = user["name"]

    # For displaying lecture and tutorial timings
    lecture_timings = ""
    for l in course["lecture"]:
        if l == course["lecture"][0]:
            lecture_timings += "{}, {}:30-{}:20".format(
                number_to_days[l[1][0]], l[1][1], l[1][1] + l[0])
        else:
            lecture_timings += " | {}, {}:30-{}:20".format(
                number_to_days[l[1][0]], l[1][1], l[1][1] + l[0])

    t = course["tutorial"]
    tutorial_timings = "{}, {}:30-{}:20".format(
        number_to_days[t[1][0]], t[1][1], t[1][1] + t[0])

    # email button plus another column for displaying course's weekly schedule
    send_email_button = [sg.Column(
        [[sg.Button("Send to email address", key="-SEND_EMAIL-",
                    size=(12, 2),
                    font="Arial 10 bold italic",
                    pad=((1, 1), (1, 1)), enable_events=True,
                    tooltip="Send information\n" + " " * 8 + "to email")]],
        element_justification='center',
        pad=((15, 0), (10, 10))),
        sg.Column(
        [[sg.Text(f"Lecture(s): {lecture_timings}",
                  font="Arial 10 bold",
                  justification='right',
                  text_color="lightblue",
                  pad=((1, 1), (1, 1)))],
         [sg.Text(f"Tutorials: {tutorial_timings}",
                  font="Arial 10 bold",
                  text_color="#fd7698",
                  justification='right',
                  pad=((1, 1), (1, 1)))]],
        element_justification='right',
        pad=((420, 0), (7, 7)))
    ]

    # Main layout
    layout = [
        headline[0], headline[2], headline[1], headline[3],
        lecturer_frame,
        zoom_link_frame,
        notes_frame,
        send_email_button
    ]

    # Create window
    window = sg.Window("{}'s moodle".format(name),
                layout, size=(900, 630))

    # Create an event loop
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "-LOGOUT-":
            window.close()
            break

        # when user clicks "send email" button
        try:
            if event == "-SEND_EMAIL-":
                send_email(course, user, fullpaths, nameonly)
        except:
            e = sys.exc_info()[0]
            print(f"Error \"{e}\" occured while sending an email!")

        #Open pdf files from course materials on click
        try:
            if event == "lectures_list":
                subprocess.Popen(os.path.join(
                    pathdict["lecture"], f"{values[event][0]}.pdf"), shell=True)

            if event == "tutorials_list":
                subprocess.Popen(os.path.join(
                    pathdict["tutorial"], f"{values[event][0]}.pdf"), shell=True)

            if event == "assignments_list":
                subprocess.Popen(os.path.join(
                    pathdict["assignment"], f"{values[event][0]}.pdf"), shell=True)
        except:
            e = sys.exc_info()[0]
            print(f"File opening error \"{e}\" occurred!")
            
        # open links when clicked
        try:
            if event == "-LEC_ZOOM-":
                webbrowser.open(course["zoom_link_lec"])

            if event == "-TUT_ZOOM-":
                webbrowser.open(course["zoom_link_tut"])
        except:
            e = sys.exc_info()[0]
            print(f"Error \"{e}\"occured while opening zoom link!")

if __name__ == '__main__':
    course = selectCourse("STAT4609")
    draw_course_window(course, person, date)
