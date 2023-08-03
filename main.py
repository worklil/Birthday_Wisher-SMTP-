from datetime import datetime
import pandas
import random
import smtplib
my_email = "new_email_1@gmail.com"
password = "abcd1234"
now = datetime.now()
today_tuple = (now.day, now.month)

data = pandas.read_csv("birthdays.csv")


birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }
if (now.month, now.day) in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        file.close()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        # made to secure our connection

        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["name"],
                            msg=f"Subject: Happy Birthday then after \n\n {contents}"
                            )

