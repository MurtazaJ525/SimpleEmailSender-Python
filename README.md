
```markdown
# SimpleEmailSender-Python

A simple Python script to send emails using the `smtplib` library with Gmail's SMTP server. This project demonstrates how to send plain text emails using secure SMTP connections with TLS encryption. Perfect for automating email tasks, sending notifications, or testing email setups.

## Features
- Send plain text emails with customizable subject and body.
- Uses Gmail's SMTP server with TLS for secure transmission.
- Simple and easy to integrate into other Python projects.

## Requirements
- Python 3.x
- A Gmail account with SMTP access enabled

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MurtazaJ525/SimpleEmailSender-Python.git
   ```


## Usage

1. Replace the `my_email` and `password` variables in `email_sender.py` with your Gmail credentials:
   ```python
   my_email = "your-email@gmail.com"
   password = "your-app-password"  # Use an App Password if 2FA is enabled on your account
   ```

2. Modify the recipient's email address and the email message content:
   ```python
   connection.sendmail(
       from_addr=my_email,
       to_addrs="recipient-email@example.com",
       msg="Subject:Your Subject Here\n\nYour email body here."
   )
   ```

3. Run the script:
   ```bash
   python email_sender.py
   ```

## Example

```python
import smtplib

my_email = "Your E-mail"
password = "App Password"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    
    # Send the email
    connection.sendmail(
        from_addr=my_email,
        to_addrs="Reciver E-mail",
        msg="Subject:Hello\n\nThis is the body of my email."
    )

print("Email sent successfully!")
```

## Notes
- **Gmail Users:** If you have 2-step verification enabled, you will need to generate an **App Password** and use it in place of your regular account password.
- For sending more complex emails (like HTML content or attachments), you can extend this script using Python's `email` module.

## License
This project is licensed under the [MIT License](LICENSE).

```

### Additional Information:
- **App Password:** If you have two-factor authentication (2FA) enabled on your Gmail account, you'll need to generate an App Password to replace the normal password.
