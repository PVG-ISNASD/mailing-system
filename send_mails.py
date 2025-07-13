import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import time
import json;


def send_email(recipient, subject, body, password, attachment_paths = None):
  sender = "sustainabilitysymposium@pvgcoet.ac.in"
  start_time = time.time()
  message = MIMEMultipart()
  message['From'] = sender
  message['To'] = recipient
  message['Subject'] = subject
  message.attach(MIMEText(body, 'html'))

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
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
      smtp_server.starttls()
      smtp_server.login(sender, password)
      smtp_server.sendmail(sender, recipient, message.as_string())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Mail sent to {recipient} in {elapsed_time:.2f} seconds.")
    return elapsed_time
  except Exception as e:
    print(f"An unexpected error occurred while sending to {recipient}: {e}")
    return 0

password = os.environ.get("EMAIL_PASSWORD")
attachment_paths = ["./attachment/ISNASD'25-FLyer.pdf"]

total_time = 0
count = 0

filepath = os.path.abspath(
  os.path.join(os.path.dirname(__file__), 'data', 'internal_team.json')
)

with open(filepath, 'r') as list:
  recipients = json.load(list)

for recipient in recipients:
  try:
    subject = "Invitation to Participate in ISNASD’25 – International Symposium on Sustainable Development"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>{subject}</title>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6;">
      <p>Dear Sir/Ma’am,</p>

      <p>We are pleased to invite faculty members and students from your esteemed institution to be a part of the upcoming 
      <strong>International Symposium on “Niche Areas of Sustainable Development” (ISNASD’25)</strong>, organized by 
      <strong>Pune Vidyarthi Griha’s College of Engineering and Technology & G. K. Pate (Wani) Institute of Management, Pune-9</strong>, 
      affiliated to <strong>Savitribai Phule Pune University, Maharashtra, India</strong>.</p>

      <p>This symposium will serve as a platform for global experts, researchers, and academicians to share insights, engage in 
      meaningful discussions, and showcase innovations contributing to a sustainable future.</p>

      <h3>📢 Call for Papers</h3>
      <p>We invite original research papers, case studies, and review articles on a wide range of sustainability-related themes.</p>
      <p>A <strong>Poster Presentation Competition</strong> is also open to students from Classes 8 to 12, with awards and opportunities for selected posters to be presented during the main symposium.</p>

      <p><strong>Registration is free and open to all.</strong></p>
      <p>You may register by scanning the QR code on the attached flyer or by clicking the link below:</p>
      <p><a href="https://docs.google.com/forms/d/e/1FAIpQLSdUVOvgylVyQ9mjJ4r2ECyZ" target="_blank">
      👉 Registration & Submission Form</a></p>

      <p>📎 <strong>More information</strong>, including themes and submission deadlines, is available in the attached flyer.</p>

      <p>We look forward to your enthusiastic participation and support in making ISNASD’25 a grand success!</p>

      <br>

      <p>Warm regards,</p>
      <p><strong>Prof. Archana Mirashi</strong><br>
      Convenor, ISNASD’25</p>

      <p><strong>Dr. Manoj Tarambale</strong><br>
      Principal, PVG’s COET & GKPIOM</p>

      <hr>

      <p><strong>📩 For queries, please contact:</strong><br>
      📧 sustainabilitysymposium@pvgcoet.ac.in<br>
      👨‍🏫 Faculty Coordinators: 98230 48494 | 82089 92812<br>
      👩‍🎓 Student Coordinator: 78430 08499</p>

      <p><em>*Please find the event flyer attached for full details.*</em></p>
    </body>
    </html>
    """
    print(f"Sending mail to {recipient}")
    this_time = send_email(recipient, subject, body, password, attachment_paths)
    if this_time > 0:
      count += 1
      total_time += this_time
  except Exception as e:
    print(f"Failed to send mail to {recipient}: {e}")

print("Total IDs in the list:", len(recipients))
print("Total mails sent:", count)
print(f"Total time taken: {total_time:.2f} seconds")
print(f"Average time taken per mail: {count / total_time} seconds")