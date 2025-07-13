# Mailing-System

This repository provides a general mailing system for ISNASD, using GitHub Actions and Python, designed to automate email sending for event.

## Usage

Currently under developement!

## Important Notes

* **Email Password Security:** Your email password (or App Password) is securely stored as a GitHub Actions secret and is not visible in the repository code.
* **Email Sending Limits:** To avoid GitHub Actions timeouts, do not attempt to send more than 4000 emails in a single run. GitHub Actions workflows are subject to a 6-hour time limit.
* **Python Script:** The core email sending logic is in the `send_mails.py` file.
* **GitHub Actions Workflow:** The automation is defined in the `send-emails.yml` file.
* **Attachments:** Attachments should be saved in the attachment folder, and the script needs to be modified to use the correct path to the attachment.

## All the best!

From, Jagdish
On behalf of the Student Organizing Committee @ ISNASD’25
