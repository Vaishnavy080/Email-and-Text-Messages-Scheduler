import re
import datetime

def checkadd(regex,email):
    print("-----------------------------------------------------------------------------------------------\n")
    print("Validating the email address...........\n")
    if(re.search(regex, email)):
        return 0
    else:
        return 1


def scheduler(send_day):
    day = send_day[0]
    month = send_day[1]
    year = send_day[2]
    today_date = datetime.date.today()
    print("Checking the Scheduled date.............\n")
    send_date = datetime.date(int(year), int(month), int(day))   # set your sending time in UTC
    if today_date == send_date:
        # returns 2 if scheduled for today
        return 2
    else:
        # returns 3 if not scheduled for today
        return 3

