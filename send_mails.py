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
attachment_paths = ["./attachment/ISNASD'25_FLYER.pdf", "./attachment/Paper_format.png"]

total_time = 0
count = 0

filepath = os.path.abspath(
  os.path.join(os.path.dirname(__file__), 'data', 'internal_team.json')
)

with open(filepath, 'r') as list:
  recipients = json.load(list)

for recipient in recipients:
  try:
    subject = "📢 Final Call for Paper Submission – ISNASD’25 (Sustainability Symposium)"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Final Call for Paper Submission – ISNASD’25</title>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; background-color: #f9f9f9; margin: 0; padding: 0;">
      <div style="max-width: 700px; margin: 30px auto; background-color: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        
        <p style="font-size: 16px;">Hello {recipient['name']},</p>

        <p style="font-size: 16px;">Greetings from the Organizing Committee of the 
        <strong>International Symposium on “Niche Areas of Sustainable Development” (ISNASD’25)</strong>, 
        organized by <strong>Pune Vidyarthi Griha’s College of Engineering, Technology and Management, Pune-9</strong>, 
        affiliated to <strong>Savitribai Phule Pune University, Maharashtra, India</strong>.</p>

        <!-- Final Call Message -->
        <h3 style="color: #2E8B57; font-weight: 700; font-size: 18px;">📢 Final Call for Paper Submission</h3>

        <p style="font-size: 16px;">We sincerely thank you for submitting your <strong>abstract</strong> titled 
        <em>“{recipient['topic']}”</em> earlier under ISNASD’25.</p>

        <p style="font-size: 16px;">As per our records, we have not yet received your <strong>final paper</strong>. 
        Although the deadline for final paper submission has already passed, the Organizing Committee is providing 
        a <strong>final opportunity</strong> for authors to complete their submission.</p>

        <p style="font-size: 16px;">You are kindly requested to send your <strong>final paper (PDF or Word format)</strong> 
        at the earliest by replying to this email. Submissions received promptly will still be considered for inclusion 
        in the proceedings and presentation schedule.</p>

        <p style="font-size: 16px;">The symposium is scheduled on <strong>3<sup>rd</sup>, 4<sup>th</sup> and 5<sup>th</sup> November 2025</strong>. 
        We would be delighted to have your active participation in this academic event.</p>

        <p style="font-size: 16px;">For your convenience, we have attached the following:</p>
        <ul style="font-size: 16px;">
          <li><strong>Paper Format</strong> – to prepare your final paper</li>
          <li><strong>Speakers Flyer</strong> – featuring our distinguished speakers</li>
        </ul>

        <p style="font-size: 16px;">We truly value your contribution and encourage you to submit your final paper at the earliest possible.</p>

        <!-- WhatsApp Group -->
        <p style="font-size: 16px;">
          <a href="https://chat.whatsapp.com/KLZyOua6T0p5L7RA2nP0yJ?mode=ems_wa_t" 
            target="_blank" 
            style="background-color: #2E8B57; color: white; padding: 10px 16px; text-decoration: none; border-radius: 4px; display: inline-block;">
            👉 Join WhatsApp Group
          </a>
        </p>

        <p style="font-size: 16px;">If you have not yet joined the WhatsApp group, please do so using the above link to receive important symposium updates.</p>

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

        <p style="font-size: 14px; margin-top: 40px; color: #555;">On behalf of the Student Organizing Committee @ ISNASD’25</p>
      </div>
    </body>
    </html>
    """
    print(f"Sending mail to {recipient['name']} ({recipient['email']})...")
    this_time = send_email(recipient["email"], subject, body, password, attachment_paths)
    if this_time > 0:
      count += 1
      total_time += this_time
  except Exception as e:
    print(f"Failed to send mail to {recipient}: {e}")

print("Total IDs in the list:", len(recipients))
print("Total mails sent:", count)
print(f"Total time taken: {total_time:.2f} seconds")
print(f"Average time taken per mail: {total_time / count} seconds")
