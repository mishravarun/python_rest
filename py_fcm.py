#!/usr/bin/env/python
'''
    File name: py_fcm.py
    Author: varun
    Date created: 08-11-2017
    Date last modified: Wed Nov  8 14:26:49 2017
'''
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="<YOUR API KEY>")

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id ="<client registation token>"
message_title = "Uber update"
message_body = "Hi john, your customized news for today is ready"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)


print result

