import smtplib

hostname = 'smtp.gmail.com'
email = 'atul.arya993@gmail.com'
password = 'kiwbqafplroavsfn'  # this password we got from app password from manage accounts -> security -> app password

with smtplib.SMTP(host=hostname) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs=email,
        msg=f'Subject: Test python email\n\n Hi Atul hope you are doing good'
    )
