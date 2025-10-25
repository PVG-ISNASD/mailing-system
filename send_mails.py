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
attachment_paths = ["./attachment/ISNASD'25_FLYER.pdf", "./attachment/ISNASD'25_Poster_Extended_Flyer.pdf"]

total_time = 0
count = 0

filepath = os.path.abspath(
  os.path.join(os.path.dirname(__file__), 'data', 'recipients.json')
)

with open(filepath, 'r') as list:
  recipients = json.load(list)

for recipient in recipients:
  try:
    subject = "📢 ISNASD’25 – Event Schedule & Poster Competition Extension Announcement"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>ISNASD’25 – Event Schedule & Poster Competition Extension</title>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; background-color: #f9f9f9; margin: 0; padding: 0;">
      <div style="max-width: 700px; margin: 30px auto; background-color: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        
        <p style="font-size: 16px;">Respected Sir/Madam,</p>

        <p style="font-size: 16px;">Greetings from the Organizing Committee of the 
        <strong>International Symposium on “Niche Areas of Sustainable Development” (ISNASD’25)</strong>, 
        organized by <strong>Pune Vidyarthi Griha’s College of Engineering, Technology and Management, Pune-9</strong>, 
        affiliated to <strong>Savitribai Phule Pune University, Maharashtra, India</strong>.</p>

        <!-- Event Information -->
        <h3 style="color: #2E8B57; font-weight: 700; font-size: 18px;">🌍 ISNASD’25 – Event Schedule Announcement</h3>
        <p style="font-size: 16px;">We are pleased to announce that the <strong>International Symposium on Niche Areas of Sustainable Development (ISNASD’25)</strong> will be held on:</p>

        <p style="font-size: 16px; background-color: #f2fdf2; padding: 10px; border-left: 4px solid #2E8B57; border-radius: 4px;">
          📅 <strong>Dates:</strong> 3<sup>rd</sup>, 4<sup>th</sup>, and 5<sup>th</sup> November 2025<br>
        </p>

        <p style="font-size: 16px;">We look forward to welcoming faculty, researchers, students, and participants from various institutions to join this 3-day symposium featuring expert talks, technical paper presentations, and student innovation showcases.</p>

        <!-- Poster Competition Update -->
        <h3 style="color: #2E8B57; font-weight: 700; font-size: 18px;">🖼️ Poster & Video Making Competition – Extended Eligibility!</h3>
        <p style="font-size: 16px;">We are delighted to announce that the <strong>Poster & Video Making Competition</strong>, originally for Classes 9–12 school students, has now been <strong>extended to include:</strong></p>

        <ul style="font-size: 16px; margin-left: 20px; line-height: 1.6;">
          <li><strong>First-year students</strong> of any course or stream</li>
          <li><strong>Equivalent year students</strong> after 12th from any recognized institute</li>
        </ul>

        <p style="font-size: 16px;">This expansion aims to encourage more young minds to share innovative ideas on sustainability and contribute to the global dialogue on <strong>SDGs (Sustainable Development Goals)</strong>.</p>

        <p style="font-size: 16px; background-color: #fff3e0; padding: 10px; border-left: 4px solid #d32f2f; border-radius: 4px;">
          🏆 <strong>Poster / Video Competition Awards:</strong><br>
          1st Prize – ₹5000<br>
          2nd Prize – ₹3000<br>
          3rd Prize – ₹1000
        </p>

        <p style="font-size: 16px;">📎 Please find attached the <strong>Event Schedule Flyer</strong> and the <strong>Poster Competition Flyer</strong> for detailed information.</p>

        <!-- WhatsApp Group -->
        <h3 style="color: #2E8B57; font-weight: 700; font-size: 18px;">📱 Stay Connected for Updates</h3>
        <p style="font-size: 16px;">Join our official WhatsApp group to receive timely updates regarding the symposium sessions, competitions, and announcements:</p>

        <p style="font-size: 16px;">
          <a href="https://chat.whatsapp.com/LvNfxZanwZC4D6Z0ZPozrA?mode=wwc" 
            target="_blank" 
            style="background-color: #2E8B57; color: white; padding: 10px 16px; text-decoration: none; border-radius: 4px; display: inline-block;">
            👉 Join ISNASD’25 Updates Group
          </a>
        </p>

        <p style="font-size: 16px;">If you’ve already joined the group, you can ignore this message. Otherwise, please do join to stay updated.</p>

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

        <p style="font-size: 14px; font-style: italic; margin-top: 20px;">*Please find the Event Flyer and Poster Competition Flyer attached.*</p>

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
