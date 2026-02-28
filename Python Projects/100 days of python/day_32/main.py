import smtplib
import os
password=""
with open(".env") as file:
    for line in file:
        key, value = line.strip().split("=")
        if key == "EMAIL_PASSWORD":
            password = value

my_email = "diksclaude1@gmail.com"
connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, 
                    to_addrs="diksclaude2@gmail.com", 
                    msg="Subject:Hello\n\nThis is the body of the email.")
connection.close()