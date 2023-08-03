import smtplib
import datetime as dt
import random
my_email = "new_email_1@gmail.com"
password = "abcd1234"
# the same password from App password
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
if day_of_week == 2:
    # 0 it's monday using this for test your code
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        # made to secure our connection

        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="new_email_2@yahoo.com",
                            msg=f"Subject: Motivation\n\n{quote}"
                            )



