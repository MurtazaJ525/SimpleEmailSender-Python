import smtplib

my_email = "abc@gmail.com"
password = "Your AppPass"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    # Send the email
    connection.sendmail(
        from_addr=my_email,
        to_addrs="ab12@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )

print("Email sent successfully!")
