import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "mail987test@gmail.com"
MY_PASS = "fzwgblshrwckyuuw"

current_date = dt.datetime.now()

today = (current_date.month, current_date.day)

bdays = list(pandas.read_csv("birthdays.csv").to_dict(orient="records"))

for bday in bdays:
    if (bday["month"], bday["day"]) == today:
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            new_letter = contents.replace("[NAME]", bday["name"])
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASS)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=bday["email"],
                                    msg=f"Subject: HBD\n\n{new_letter}")

print(bdays)
