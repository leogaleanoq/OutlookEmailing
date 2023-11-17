import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def EmailHandler(Receiver, content):
    # SMTP server settings
    smtp_server = 'smtp.office365.com'
    smtp_port = 587  # Use the appropriate SMTP port (587 for TLS)
    smtp_username = 'leonardo.galeano@swapsupport.es'
    # The normal password, do not works, is needed an app paswword
    #doc: https://support.microsoft.com/en-us/account-billing/manage-app-passwords-for-two-step-verification-d6dc8c6d-4bf7-4851-ad95-6d07799387e9
    smtp_password = ''

    # Sender and recipient email addresses
    sender_email = 'leonardo.galeano@swapsupport.es'
    recipient_email = Receiver

    # Create a message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = 'TEST TEST TES'

    # Add email body
    body = content
    message.attach(MIMEText(body, 'plain'))

    # Establish a connection to the SMTP server
    try:
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()  # Use TLS encryption
        smtp_connection.login(smtp_username, smtp_password)

        # Send the email
        smtp_connection.sendmail(sender_email, recipient_email, message.as_string())

        # Close the connection
        smtp_connection.quit()

        print('Email sent successfully')

    except Exception as e:
        print('An error occurred:', str(e))