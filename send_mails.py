
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import formataddr
import os
import time
import json


def send_email(recipient, subject, body, password, attachment_paths=None):
    sender = "sustainabilitysymposium@pvgcoet.ac.in"
    display_name = "ISNASD’26 Team"

    start_time = time.time()
    message = MIMEMultipart()
    message["From"] = formataddr((display_name, sender))
    message["To"] = recipient
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))

    if attachment_paths:
        for attachment_path in attachment_paths:
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename={os.path.basename(attachment_path)}",
                )
                message.attach(part)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp_server:
            smtp_server.starttls()
            smtp_server.login(sender, password)
            smtp_server.sendmail(
                sender, recipient, message.as_string()
            )

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(
            f"Mail sent to {recipient} in {elapsed_time:.2f} seconds."
        )
        return elapsed_time

    except Exception as e:
        print(
            f"An unexpected error occurred while sending to "
            f"{recipient}: {e}"
        )
        return 0


password = os.environ.get("EMAIL_PASSWORD")

# Update this path if your flyer has a different filename.
attachment_paths = ["./Event flyer.jpeg", "./About the event.jpeg"]

total_time = 0
count = 0

filepath = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "data",
        "recipients.json",
    )
)

with open(filepath, "r") as file:
    recipients = json.load(file)

for recipient in recipients:
    try:
        subject = (
            "Invitation to Participate in ISNASD’26 – "
            "International Symposium on Niche Areas of "
            "Sustainable Development"
        )

        body = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset="UTF-8">
          <title>{subject}</title>
        </head>

        <body style="font-family: Arial, sans-serif; line-height: 1.6; background-color: #f9f9f9; margin: 0; padding: 0;">

          <div style="max-width: 700px; margin: 30px auto; background-color: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">

            <p style="font-size: 16px;">Dear Sir/Ma’am,</p>

            <p style="font-size: 16px;">
              We are pleased to invite faculty members and students from your
              esteemed institution to be a part of the upcoming
              <strong>International Symposium on “Niche Areas of Sustainable
              Development” (ISNASD’26)</strong>, scheduled on
              <strong>3rd, 4th and 5th of November</strong>, organized by
              <strong>Pune Vidyarthi Griha’s College of Engineering, Technology
              and Management, Pune-9</strong>, affiliated to
              <strong>Savitribai Phule Pune University, Maharashtra, India</strong>.
            </p>

            <p style="font-size: 16px;">
              This symposium will serve as a platform for global experts,
              researchers, and academicians to share insights, engage in
              meaningful discussions, and showcase innovations contributing
              to a sustainable future.
            </p>

            <h3 style="color: #d32f2f; font-weight: 700; font-size: 18px;">
              ‼️ Event Highlights
            </h3>

            <ul style="font-size: 16px; padding-left: 24px;">
              <li style="margin-bottom: 10px;">
                <strong>Expert Talks on 3rd, 4th &amp; 5th November:</strong>
                Insights from international and national leaders.
              </li>

              <li style="margin-bottom: 10px;">
                <strong>Live Panel Discussions:</strong>
                Exciting prizes for the best panelists and certificates
                for all participants.
              </li>

              <li style="margin-bottom: 10px;">
                <strong>Global Network:</strong>
                Collaborate, Connect, Create and Impact.
              </li>
            </ul>

            <p style="font-size: 16px;">
              <strong>Registration is free and open to all.</strong>
            </p>

            <p style="font-size: 16px;">
              You may register by scanning the QR code on the attached flyer
              or by clicking the link below:
            </p>

            <p style="font-size: 16px;">
              <a href="https://docs.google.com/forms/d/e/1FAIpQLScAycjab-lVZEiAYNVADG0YNCneCkMEBwMdCscQld7Yr_DgzA/viewform"
                 target="_blank"
                 style="background-color: #2E8B57; color: white; padding: 10px 16px; text-decoration: none; border-radius: 4px; display: inline-block;">
                👉 Registration &amp; Submission Form
              </a>
            </p>

            <p style="font-size: 16px;">
              📎 <strong>More information</strong>, including themes and
              submission deadlines, is available in the attached flyer.
            </p>

            <p style="font-size: 16px;">
              We look forward to your enthusiastic participation and support
              in making ISNASD’26 a grand success!
            </p>

            <p style="font-size: 16px; text-align: center;">
              Warm Regards
            </p>

            <table style="width: 100%; font-size: 16px; border-collapse: collapse;">
              <tr>
                <td style="text-align: left; vertical-align: top; width: 50%;">
                  <strong>Prof. Archana Mirashi</strong><br>
                  Convenor, ISNASD’26
                </td>

                <td style="text-align: right; vertical-align: top; width: 50%;">
                  <strong>Dr. Sandip R. Patil</strong><br>
                  Principal, PVG’s COETM, Pune
                </td>
              </tr>
            </table>

            <hr style="border: none; border-top: 1px solid #ccc; margin: 30px 0;">

            <div style="border-left: 4px solid #2E8B57; padding-left: 16px; background-color: #f2fdf2; padding: 10px 16px; font-size: 15px;">

              <p>
                <strong>📩 For queries, please contact:</strong>
              </p>

              <p>
                📧 <a href="mailto:sustainabilitysymposium@pvgcoet.ac.in">
                  sustainabilitysymposium@pvgcoet.ac.in
                </a><br>

                👨‍🏫 Faculty Coordinators: 98230 48494 | 82089 92812<br>

                👩‍🎓 Student Coordinators: 7058181866 | 7887889484
              </p>

            </div>

            <p style="font-size: 14px; font-style: italic; margin-top: 20px;">
              *Please find the event flyer attached for full details.*
            </p>

            <p style="font-size: 14px; margin-top: 40px; color: #555;">
              On behalf of the Student Organizing Committee @ ISNASD’26
            </p>

          </div>

        </body>
        </html>
        """

        this_time = send_email(
            recipient,
            subject,
            body,
            password,
            attachment_paths,
        )

        if this_time > 0:
            count += 1
            total_time += this_time

    except Exception as e:
        print(f"Failed to send mail to {recipient}: {e}")


print("Total IDs in the list:", len(recipients))
print("Total mails sent:", count)
print(f"Total time taken: {total_time:.2f} seconds")

if count > 0:
    print(f"Average time taken per mail: {total_time / count:.2f} seconds")
else:
    print("Average time taken per mail: N/A (no emails sent)")
