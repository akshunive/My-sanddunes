#automating the mail
import smtplib
fromaddr = 'nivethamyilvaganan@gmail.com'    #sender mail-id
toaddrs  = 'sugankumar016@gmail.com'         #recepient mail-id
msg = 'Hi da donkey this is an automated mail'#message to be sent
# Credentials (if needed)
username = 'nivethamyilvaganan@gmail.com'  
password = ''
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')  #server name
server.starttls()                            #start connection
server.login(username,password)              #login with the username and password provided
server.sendmail(fromaddr, toaddrs, msg)      #sending the mail to the recepient 
server.quit()