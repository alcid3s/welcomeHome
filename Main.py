import subprocess, smtplib, time, datetime

flag = True
host = "192.168.1.1" # Change this to the static IP of the device you want to control.

while True:
    #Checking if the host in the network.
    response = subprocess.getoutput(f"ping -c 1 {host}")

    # Device is not in network.
    if("Destination Host Unreachable" in response or "Request timed out" in response or "100% packet loss" in response):
        disconnected = (datetime.datetime.now().strftime('[%d-%m-%y %H:%M:%S] Device disconnected'))
        print(disconnected)
        if(flag == False):
            # If you want an event when the device disconnects, you can place that here.
            flag = True
            print(f"Flag is {flag}")

    # Device is in the network.
    elif("Destination Host Unreachable" not in response or "Request timed out" not in response or "100% packet loss" not in response):
        connected = (datetime.datetime.now().strftime('[%d-%m-%y %H:%M:%S] Device connected'))
        print(connected)
        if(flag == True):
            # Event you want to happen when device is connected to the network. In this example an email is send when the device is connected.
            server = smtplib.SMTP( "smtp.gmail.com", 587 )
            server.starttls()
            server.login('example@hotmail.com', 'password123' )
            server.sendmail('Raspberry Pi', 'receiver@hotmail.com', 'Welcome home!')
            server.quit()
            flag = False
            print(f"Flag is {flag}")
    else:
        # Impossible to reach this piece of code.
        print("Device is not connected nor disconnected")
    # Every 30 seconds the loop will be executed.
    time.sleep(30)