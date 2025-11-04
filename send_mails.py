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
attachment_paths = ["./attachment/ISNASD'25_FLYER.pdf"]

total_time = 0
count = 0

filepath = os.path.abspath(
  os.path.join(os.path.dirname(__file__), 'data', 'internal_team.json')
)

with open(filepath, 'r') as list:
  recipients = json.load(list)

for recipient in recipients:
  try:
    subject = "Presentation Schedule & Instructions – ISNASD’25 (Day 3, 5th November 2025)"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Presentation Schedule & Instructions – ISNASD’25</title>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; background-color: #f9f9f9; margin: 0; padding: 0;">
      <div style="max-width: 700px; margin: 30px auto; background-color: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        
        <p style="font-size: 16px;">Hello {recipient['resource_person']},</p>

        <p style="font-size: 16px;">Greetings from the Organizing Committee of the 
        <strong>International Symposium on “Niche Areas of Sustainable Development” (ISNASD’25)</strong>, 
        organized by <strong>Pune Vidyarthi Griha’s College of Engineering, Technology and Management, Pune–9</strong>, 
        affiliated with <strong>Savitribai Phule Pune University, Maharashtra, India</strong>.</p>

        <h3 style="color: #2E8B57; font-weight: 700; font-size: 18px;">📢 Presentation Schedule & Instructions – ISNASD’25</h3>

        <p style="font-size: 16px;"><strong>Please find your paper presentation details below:</strong></p>

        <table style="font-size: 16px; margin-top: 10px;">
          <tr><td><strong>Date:</strong></td><td>5th November 2025</td></tr>
          <tr><td><strong>Day:</strong></td><td>Wednesday</td></tr>
          <tr><td><strong>Time Slot:</strong></td><td>{recipient['time']}</td></tr>
          <tr><td><strong>Topic:</strong></td><td>{recipient['topic']}</td></tr>
          <tr><td><strong>Mode:</strong></td><td>Online</td></tr>
          <tr><td><strong>Format:</strong></td><td>12-minute presentation + 1–2 minutes Q&A</td></tr>
        </table>

        <p style="font-size: 16px; margin-top: 18px;"><strong>🔗 Meeting Link:</strong> The Day 3 session link will be shared in the official WhatsApp group at <strong>11:45 AM</strong> on 5th November.</p>

        <h4 style="color: #2E8B57; margin-top: 25px;">⚠ Important Instructions</h4>

        <ul style="font-size: 16px;">
          <li>Your time slot may vary by <strong>±30 minutes</strong> depending on the flow of presentations.</li>
          <li>Please ensure your presence in the session at least <strong>30 minutes before</strong> your allotted time.</li>
          <li>If you are unavailable during your slot or the surrounding buffer, your presentation may be passed.</li>
        </ul>

        <h4 style="color: #2E8B57; margin-top: 25px;">✅ Action Required (Please reply to this email):</h4>
        <ol style="font-size: 16px;">
          <li><strong>Consent for Test Meeting (11:00–11:45 AM on 5th Nov):</strong><br>
          Reply <strong>“OK”</strong> or <strong>“NOT OK”</strong>.</li>
          <li><strong>Name(s) of Presenters</strong> (only those who will present).</li>
          <li><strong>Mobile Number(s)</strong> of the presenters for session coordination.</li>
        </ol>

        <p style="font-size: 16px;">If you reply <strong>“OK”</strong>, the <strong>Test Meeting Link</strong> will be emailed before <strong>11:00 AM</strong> on the same day.</p>

        <p style="font-size: 16px;">Your timely response helps ensure smooth coordination during the presentation session.</p>

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
