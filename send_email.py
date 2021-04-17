import email
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(course, user, paths, filenames):
    number_to_days = ["", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]

    name = user["name"]
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
    zoom_link_lec = course["zoom_link_lec"]
    zoom_link_tut = course["zoom_link_tut"]
    course_code = course["code"]
    course_title = course["title"]
    teacher_message = course["teacher_msg"]
    professor_info = course["lecturer"]

    subject = "{}'s course info - sent from Moodle, HKU".format(
        course_code)
    sender_email = "hku.moodle2.0@gmail.com"
    receiver_email = user["email"]
    password = "a1b2c3d4!"

    # Create a multipart message and set headers
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    body = """
    Dear {0},\n\n
    Please find the requested information below:\n\n
    COURSE CODE: {1}\n
    COURSE TITLE: {2}\n
    Teacher: {3}   |   Teacher's email: {4}\n
    Teacher's message: {5}\n
    \nLectures: {6}\n
    Zoom link: {7}\n\n
    Tutorial: {8}\n
    Zoom link: {9}\n\n
    Recent lecture and tutorial materials are attached with the email. Please refer to Moodle for more information.\n\n
    """.format(name, course_code, course_title,
               professor_info[0], professor_info[2],
               teacher_message,
               lecture_timings, zoom_link_lec,
               tutorial_timings, zoom_link_tut)

    html = """
    <html>
      <body>
        <p>Dear {0},
        <br>
        <br>Please find the requested information below:
        <br>
        <br><span style="font-weight: bold">COURSE CODE:</span> {1}
        <br><span style="font-weight: bold">COURSE TITLE:</span> {2}
        <br><span style="font-weight: bold">Teacher:</span> {3}  <span style="font-weight: bold"> |   Teacher's email:</span> {4}
        <br><span style="font-weight: bold">Teacher's message:</span> {5}
        <br>
        <br><span style="font-weight: bold">Lectures:</span> {6}
        <br><span style="font-weight: bold">Zoom link:</span> {7}
        <br>
        <br><span style="font-weight: bold">Tutorial:</span> {8}
        <br><span style="font-weight: bold">Zoom link:</span> {9}
        <br>
        <br>Recent lecture and tutorial materials are attached. Please refer to <a href="https://moodle.hku.hk/login/" style="font-weight: bold; color: red; text-decoration: underline;">Moodle</a> for more information.
        <br>
        <p></p>
        <p></p>
        </p>
        </body>
    </html>
    """.format(name, course_code, course_title,
               professor_info[0], professor_info[2],
               teacher_message,
               lecture_timings, zoom_link_lec,
               tutorial_timings, zoom_link_tut)

    # Turn these into plain/html MIMEText objects (plain in case html is not enabled for some users)
    message.attach(MIMEText(body, "plain"))
    part2 = MIMEText(html, "html")
    message.attach(part2)

    # Attach lecture materials
    for i in range(len(filenames)):
        filename = paths[i]
        name = filenames[i]

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {name}",
        )
        
        # Add attachment to message and convert message to string
        message.attach(part)

    text = message.as_string()

    try:
        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)

            
    except:
        message = MIMEMultipart("alternative")
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email
        
        html = html.replace("Recent lecture and tutorial materials are attached with the email.",
                     "Failed to attach recent course materials due to message size limits.")
        body = body.replace("Recent lecture and tutorial materials are attached with the email.",
                     "Failed to attach recent course materials due to message size limits.")
        # Turn these into plain/html MIMEText objects (plain in case html is not enabled for some users)
        message.attach(MIMEText(body, "plain"))
        part2 = MIMEText(html, "html")
        message.attach(part2)
        
        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)        