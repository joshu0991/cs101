
import requests
import json
import datetime
counter = 0
def init():
    global counter
    counter = 0
def restful_request():
    global counter
    counter = counter + 1
    print ("counter " + str(counter))
    mytime = datetime.datetime.now()
    print(mytime)

    now = datetime.datetime.now() - datetime.timedelta(minutes=240)
    now.strftime("%I:%M%p on %B %d, %Y")

    url = 'http://54.191.52.234:7272/api/v0.1/eaaefbeed081427b8fd74561f396bd41/push'
    data_push_statistic = dict(tile='listing', key='id_13', data=json.dumps({"title": "Statistics",
    "items": [[" "],["  Mail Recieved on "],["Date : " ],
              ["Time : " ],
              [""]]}))

    data_push_group_memebrs = dict(tile='listing',
                     key='id_1',
                     data=json.dumps({
                         "title": "Group Memebers",
                         "items": [["\t\tCS 101 GROUP PROJECT"],["1. "],["2. "],["3. "],["4. "]]}))

    data_push_mail_notification = dict(tile='big_value',
                                       key='id_20',
                                       data=json.dumps({"title": "Mail Notification",
                                                        "description": "number of New Mails",
                                                        "big-value": " No New Mail",
                                                       }))


    data_push_mail_pie_chart = dict(tile='pie_chart', key='id_14',  data=json.dumps({"title": "Mail Analyzation", "pie_data": [["NEW MAil", 0], ["Old Mail", 100], ["Deleted", 0]]}))

    data_push_simple_percentage = dict(tile='simple_percentage',
                     key='id_15',
                 data=json.dumps({
                         "title": "CHECKED", "subtitle": "SPEED = 72.2 mbps", "big_value": "100%",
                   "left_value": "50%", "left_label": "Old Mails",
                   "right_value": "25%", "right_label": "Unread Mails"}))


    r = requests.post(url, data=data_push_mail_notification)
    r = requests.post(url, data=data_push_group_memebrs)
    r = requests.post(url, data=data_push_statistic)
    r = requests.post(url, data=data_push_simple_percentage)
    print(r.status_code, r.reason)
    print(r.text)
    print(r.status_code, r.reason)
restful_request()

