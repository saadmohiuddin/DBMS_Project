import email
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email():
    number_to_days = ["", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]
    course = {
        "code": "COMP3278",
        "title": "Introduction to database management systems",
        "lecture": [(2, (5, 9, 30))],
        "tutorial": (1, (2, 9, 30))
    }

    name = "Jack Greyson"
    lecture_timings = ""
    for l in course["lecture"]:
        if l == course["lecture"][0]:
            lecture_timings += "{}, {}:30-{}:20".format(
                number_to_days[l[1][0]], l[1][1], l[1][1] + l[0])
        else:
            lecture_timings += " | {}, {}-{}".format(
                number_to_days[l[1][0]], l[1][1], l[1][1] + l[0])
    t = course["tutorial"]
    tutorial_timings = "{}, {}:30-{}:20".format(
        number_to_days[t[1][0]], t[1][1], t[1][1] + t[0])
    zoom_linkL = "https://hku.zoom.us/j/97686555806?pwd=NWxSNVRKTlNDU0NjYTgremxaQ3pldz09"
    zoom_linkT = "https://hku.zoom.com.cn/j/2640918958?pwd=UmFpek1YMkUzNTFoL0ljRW84M1VLUT09"
    course_code = course["code"]
    teacher_message = "Test on 24th March"
    classroom_address = "Room1225, Run Run Shaw Building"

    subject = "{}'s course info - sent from Moodle 2.0, HKU".format(
        course_code)
    body = "This is an email with attachment sent from Python"
    sender_email = "jackgreyson11@gmail.com"
    receiver_email = "jackgreyson11@gmail.com"
    password = "a1b2c3d4!"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    #message.attach(MIMEText(body, "plain"))

    html = """
    <html>
      <body>
        <p>Dear {0},
        <br>
        <br>Please find the requested information below:
        <br>
        <br><span style="font-weight: bold">COURSE CODE:</span> {1}
        <br><span style="font-weight: bold">Teacher's message:</span> {2}
        <br><span style="font-weight: bold">Classroom's address:</span> {3}
        <br>
        <br><span style="font-weight: bold">Lectures:</span> {4}
        <br><span style="font-weight: bold">Zoom link:</span> {5}
        <br>
        <br><span style="font-weight: bold">Tutorial:</span> {6}
        <br><span style="font-weight: bold">Zoom link:</span> {7}
        <br>
        <br>Recent lecture and tutorial materials are attached with the email. Please
        refer to <a href="https://moodle.hku.hk/login/" style="font-weight: bold; color: red; text-decoration: underline;">Moodle</a> for more information.
        <br>
        <p></p>
        <p></p>
        </p>
      </body>
    </html>
    """.format(name, course_code, teacher_message, classroom_address, lecture_timings, zoom_linkL, tutorial_timings, zoom_linkT)

    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(html, "html")
    message.attach(part2)

    filenames = ["FM_Exam.pdf", "Question.pdf"]
    for filename in filenames:

        # filename in the same directory as script

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)

    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
