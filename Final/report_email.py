#!/usr/bin/env python3

import os
import datetime
import reports
import emails

indir = 'supplier-data/descriptions'

def process_data():
    body = ""
    # iterate images inside in folder
    for infile in os.listdir(indir):
        with open(os.path.join(indir, infile)) as f:
            lines = f.readlines()
            name = lines[0].strip()
            weight = lines[1].strip()
            body += "name: {}<br/>weight: {}<br/><br/>".format(name, weight)
    return body


if __name__ == "__main__":
    attachment = "processed.pdf"
    title = "Processed Update on {}".format(datetime.date.today().strftime("%B %d, %Y"))
    paragraph = process_data()
    reports.generate_report(attachment, title, paragraph)

    sender = "automation@example.com"
    receiver = "username@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)
