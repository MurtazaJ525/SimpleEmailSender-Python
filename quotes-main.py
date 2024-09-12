import datetime as dt
import random
import smtplib

MY_EMAIL = "mra8135100+github@gmail.com"
MY_PASSWORD = "bnbsrvrpvolmctcq"

# Get the current date and weekday
now = dt.datetime.now()
weekday = now.weekday()

# List of days for the email subject
days_of_week = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
]

# Check if it's any day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
if 0 <= weekday <= 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes).strip()  # Remove any extra newlines or spaces
        print(quote)

    # HTML formatted email
    html_message = f"""
       <html>
           <body>
               <h1><p><strong>{days_of_week[weekday]} Motivation</strong></p></h1>
               <h1><p><strong>"{quote}"</strong></p></h1>
               <br>
               <h2><p>Best regards,<br>Murtaza</p></h2>
           </body>
       </html>
       """

    # Sending the email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=["attarsarrah53@gmail.com", "mr.murtazaj@gmail.com","vishalnarsinh@gmail.com","husainmt52@gmail.com"],
            msg=f"Subject:{days_of_week[weekday]} Motivation\n"
                f"Content-Type: text/html\n\n{html_message}"
        )

print("Email sent successfully!")
