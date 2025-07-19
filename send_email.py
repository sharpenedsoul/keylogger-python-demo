import smtplib
import ssl

# Function to send an email with the given message
def sendEmail(message):
    # SMTP server configuration
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "your_email_address"
    password = "your_passkey"
    receiver_email = "receiver_email_address"

    # Create a secure SSL/TLS context
    context = ssl.create_default_context()

    try:
        # Establish a connection to the SMTP server
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Identify the client to the SMTP server
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Re-identify after starting TLS

        # Log in to the Gmail account
        server.login(sender_email, password)

        # Send the email from sender to receiver
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        # Print any error that occurs
        print(e)

    finally:
        # Ensure the server is closed properly
        server.quit()
