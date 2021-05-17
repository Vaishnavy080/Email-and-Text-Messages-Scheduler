from Email_Scheduler import checkadd, scheduler
from TextMessage import send_sms_get, send_sms_post
import pandas as pd
import smtplib
import datetime as dt
import requests
import json
API_ENDPOINT = "https://api.sms-magic.com/v1/sms/send"
msg_delivery_status_url = 'https://api.sms-magic.com/v1/sms/status'
API_KEY = "54b197ee146649517b9e5b47172cd1ee"

def message_status(ids):
    status_payload = {"sms_id_list": ids}
    headers_status = {'apiKey': API_KEY,
                      'content_type': 'application/json'}
    response_status = requests.post(msg_delivery_status_url, headers=headers_status, json=status_payload)
    res = json.loads(response_status.text)
    print("Message Sent Status as per api response: {}.\n\n".format(res[0]['status']))
    txtfile = open("Dataset\Message_History.txt", "a")
    txtfile.write("\n\nStatus of Message Sent: {}.\n\n".format(res[0]['status']))

    return response_status.status_code

def send_email (receiver_address, sender_address, mail_content):
    print("Sending email to {}...............\n".format(receiver_address))
    sub_content = """\
Subject: Test Mail for Assignment.
                    
                    
"""
    sub_content += mail_content
    session.sendmail(sender_address, receiver_address, sub_content)
    print("Email sent\n\n")
    txtf=open("Dataset\Mail_History.txt", "a")
    txtf.write("{} {}\n  Email Status:Success.\n  Sent at {}\n\n".format("*", receiver_address, dt.datetime.now()))

# Main method
if __name__ == '__main__':

    print("Running the application...............\n")

    # creation of new files
    txtfile = open('Dataset\Mail_History.txt', "w+")
    txtf2 = open("Dataset\Message_History.txt", "w+")

    # reading csv file using pandas
    rd = pd.read_csv('Dataset\Data.csv')
    df = pd.DataFrame(rd)
    df.rename(columns={'Scheduled On': 'ScheduledOn'}, inplace=True)

    # expression to check if the mail is valid or not
    regex = '^(.+)@(.+)$'

    sender_address = 'testmail080080@gmail.com'
    sender_pass = 'Testmail@080080'
    subject = 'Test Email sent using dataset'

    # creating an smtp session
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address,sender_pass)

    try:
        for i in range(0, len(df)):
            mail_content = df.Message[i]
            receiver_address = df.Email[i]
            flag = checkadd(regex, receiver_address)

            # get scheduled_on date
            send_day = list(str(df.ScheduledOn[i]).split("/"))
            for j in range(0, len(send_day)):
                send_day[j] = int(send_day[j])

            # Sending emails
            # If data elements fit in given criteria then send email
            if flag == 0 :
                if df.Country[i] == "USA" or df.Country[i] == "INDIA":
                    txtfile = open("Dataset\Mail_History.txt", "a")
                    txtfile.write("*****************************************************************************\n\n")

                    x = scheduler(send_day)
                    if x == 2:
                        send_email(receiver_address, sender_address, mail_content)
                    else:
                        print("Not Scheduled for today.\n\n")
                        txtfile = open("Dataset\Mail_History.txt", "a")
                        txtfile.write("{}:\n  Status: Failure.\n  Reason: Not Scheduled for today!.\n\n".format(receiver_address))
                else:
                    txtfile = open("Dataset\Mail_History.txt", "a")
                    txtfile.write("*****************************************************************************\n\n")
                    txtfile.write("{}:\n  Email Status: Failure.\n  Reason: Country other than USA or INDIA.\n\n".format(receiver_address))

            else:
                    print("Invalid Email address: {}\n\n".format(receiver_address))
                    txtfile = open("Dataset\Mail_History.txt", "a")
                    txtfile.write("*****************************************************************************\n\n")

            # Sending messages
            # If data elements fit in given criteria then send messages
            length = len(str(df.Phone[i]))
            ph_no = int(df.Phone[i])
            message = str(df.Message[i])
            x = scheduler(send_day)
            if x == 2:
                txtfile = open("Dataset\Message_History.txt", "a")
                txtfile.write("*************************************************************************************************************\n\n")
                if length == 10:
                    if 0 < len(message) <= 160:
                        print("Sending message to {}...............\n\n".format(ph_no))

                        txtfile = open("Dataset\Message_History.txt", "a")
                        txtfile.write("{}:\n\n".format(ph_no))

                        # using SEND SMS-get from api.sms-magic.com
                        send_sms_get(ph_no, message)

                        # using SEND SMS-post from api.sms-magic.com
                        id_received = send_sms_post(ph_no, message)
                        print("Message Id:{}\n\n".format(id_received))

                        txtfile = open("Dataset\Message_History.txt", "a")
                        txtfile.write("ID:{}\n\n".format(id_received))

                        # using SMS STATUS from api.sms-magic.com
                        # get status of message using id received from SEND SMS-post
                        response_code = message_status(str(id_received))

                        # Here response_code is response.status_code
                        if response_code == 200:
                            txtfile = open("Dataset\Message_History.txt", "a")
                            txtfile.write("API Response Status:Success\n\n")
                        else:
                            print("Message could not be sent due to no api response!\n\n")
                            txtfile = open("Dataset\Message_History.txt", "a")
                            txtfile.write("API Response Status:Failure\n\n")

                    else:
                        print("Length of message exceeded!\n\n")
                        txtfile = open("Dataset\Message_History.txt", "a")
                        txtfile.write("{}:\n\nMessage Status: Failure.\n\nReason: Message length is {}.It should be between 0 to 160!.\n\n".format(ph_no, len(message)))
                else:
                    if length != 10:
                        print("Phone number should be a ten digit number!\n\n")
                        txtfile = open("Dataset\Message_History.txt", "a")
                        txtfile.write("{}:\n\nMessage Status: Failure.\n\nReason: Phone number should be a ten digit number!.\n\n".format(ph_no))
            else:
                print("Not Scheduled for today.\n\n")
                txtfile = open("Dataset\Message_History.txt", "a")
                txtfile.write("*************************************************************************************************************\n")
                txtfile.write("{}:\n\nStatus: Failure.\n\nReason: Not Scheduled for today!.\n\n".format(ph_no))

    except Exception as e:
        print(e)

    print('******************************************************************************************\n'
          'Operations successful!\n'
          'Email statuses are stored at ScreenMagic Assignment\Dataset\Mail_History\n'
          'Message Statuses are stored at ScreenMagic Assignment\Dataset\Message_History\n'
          '******************************************************************************************\n')
    session.quit()

