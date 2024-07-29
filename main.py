import smtplib
import random
from datetime import datetime
import pandas

MY_MAIL = ""
PASSWORD = ""

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
# print(data)
birthday_disc = {(data_row["month"], data_row["day"]): data_row for index, data_row in data.iterrows()}
# print(birthday_disc)
if today_tuple in birthday_disc:
    birthday_person = birthday_disc[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        name = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_MAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"subject:Happy Birthday!\n\n{name}"
                            )
    print(birthday_person)
