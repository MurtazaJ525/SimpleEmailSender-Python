import smtplib

my_email = "mra8135100@gmail.com"
password = "bnbsrvrpvolmctcq"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    # Send the email
    connection.sendmail(
        from_addr=my_email,
        to_addrs="mr.murtazaj+github@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )

print("Email sent successfully!")
