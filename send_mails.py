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
  display_name = "ISNASD’25 Team"
  
  start_time = time.time()
  message = MIMEMultipart()
  message['From'] = formataddr((display_name, sender))
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
attachment_paths = ["./attachment/ISNASD25_Poster-Competition.pdf"]

total_time = 0
count = 0

filepath = os.path.abspath(
  os.path.join(os.path.dirname(__file__), 'data', 'schools.json')
)

with open(filepath, 'r') as list:
  recipients = json.load(list)

for recipient in recipients:
  try:
    subject = "📢 Call for Entries – Poster & Video Competition (ISNASD'25)"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Invitation to ISNASD’25 – Poster & Video Competition for School Students</title>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; background-color: #f9f9f9; margin: 0; padding: 0;">
      <div style="max-width: 700px; margin: 30px auto; background-color: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        
        <p style="font-size: 16px;">Respected Principal / Teachers,</p>

        <p style="font-size: 16px;">We are pleased to invite students from your esteemed school to participate in the 
        <strong>Poster Presentation & Video Making Competition</strong> as part of the 
        <strong>International Symposium on “Niche Areas of Sustainable Development” (ISNASD’25)</strong>, 
        organized by <strong>Pune Vidyarthi Griha’s College of Engineering, Technology and Management, Pune-9</strong>, 
        affiliated to <strong>Savitribai Phule Pune University, Maharashtra, India</strong>.</p>

        <!-- Competition Info -->
        <h3 style="color: #2E8B57; font-weight: 700; font-size: 18px;">🖼️ Poster & Video Making Competition (Classes 9–12)</h3>
        <p style="font-size: 16px;">This competition provides a platform for school students to showcase their creativity and ideas on themes aligned with the <strong>United Nations Sustainable Development Goals (SDGs)</strong>.</p>
        <p style="font-size: 16px; background-color: #f2fdf2; padding: 10px; border-left: 4px solid #2E8B57; border-radius: 4px;">
          🏆 <strong>Exciting Prize Money:</strong><br>
          1st Prize – ₹5000<br>
          2nd Prize – ₹3000<br>
          3rd Prize – ₹1000
        </p>
        <p style="font-size: 16px;">Outstanding posters may also get the opportunity to be presented alongside professors and researchers during the main symposium sessions!</p>

        <!-- Keep as-is section -->
        <p style="font-size: 16px;"><strong>Registration is free and open to all.</strong></p>
        <p style="font-size: 16px;">You may register by scanning the QR code on the attached flyer or by clicking the link below:</p>

        <p style="font-size: 16px;">
          <a href="https://docs.google.com/forms/d/e/1FAIpQLSenDiTC0ZQumN3H1ZZkpzK3Y5PMPHMtiFNeAeQ2uFP476PfDA/viewform?usp=dialog" 
            target="_blank" 
            style="background-color: #2E8B57; color: white; padding: 10px 16px; text-decoration: none; border-radius: 4px; display: inline-block;">
            👉 Registration & Submission Form
          </a>
        </p>

        <p style="font-size: 16px;">📎 <strong>More information</strong>, including competition guidelines and deadlines, is available in the attached flyer.</p>

        <p style="font-size: 16px;">We look forward to enthusiastic participation from your school in making ISNASD’25 a memorable event!</p>

        <p style="font-size: 16px; text-align: center;">Warm Regards</p>

        <table style="width: 100%; font-size: 16px;">
          <tr>
            <td style="text-align: left; vertical-align: top;">
              <strong>Prof. Archana Mirashi</strong><br>
              Convenor, ISNASD’25
            </td>
            <td style="text-align: right; vertical-align: top;">
              <strong>Dr. Manoj Tarambale</strong><br>
              Principal, PVG’s COETM, Pune
            </td>
          </tr>
        </table>

        <hr style="border: none; border-top: 1px solid #ccc; margin: 30px 0;">

        <div style="border-left: 4px solid #2E8B57; padding-left: 16px; background-color: #f2fdf2; padding: 10px 16px; font-size: 15px;">
          <p><strong>📩 For queries, please contact:</strong></p>
          <p>📧 <a href="mailto:sustainabilitysymposium@pvgcoet.ac.in">sustainabilitysymposium@pvgcoet.ac.in</a><br>
            👨‍🏫 Faculty Coordinators: 98230 48494 | 82089 92812<br>
            👩‍🎓 Student Coordinator: 78430 08499 | 90960 82640
          </p>
        </div>

        <p style="font-size: 14px; font-style: italic; margin-top: 20px;">*Please find the competition flyer attached for full details.*</p>

        <p style="font-size: 14px; margin-top: 40px; color: #555;">On behalf of the Student Organizing Committee @ ISNASD’25</p>
      </div>
    </body>
    </html>
    """
    this_time = send_email(recipient, subject, body, password, attachment_paths)
    if this_time > 0:
      count += 1
      total_time += this_time
  except Exception as e:
    print(f"Failed to send mail to {recipient}: {e}")

print("Total IDs in the list:", len(recipients))
print("Total mails sent:", count)
print(f"Total time taken: {total_time:.2f} seconds")
print(f"Average time taken per mail: {total_time / count} seconds")
