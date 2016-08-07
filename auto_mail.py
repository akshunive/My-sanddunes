import smtplib
fromaddr = 'nivethamyilvaganan@gmail.com'
toaddrs  = 'sugankumar016@gmail.com'
msg = 'Hiii loosu this is an automated mail...'
# Credentials (if needed)
username = 'nivethamyilvaganan@gmail.com'
password = 'nive5678'
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()