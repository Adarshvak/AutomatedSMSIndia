#!usr/bin/python
from splinter.browser import Browser
import re
import time

br=Browser()
br.visit("http://www.160by2.com/Index")
br.fill('username','YOUR_PHONE_NUMBER_USED_TO_CREATE_160BY2_ACCOUNT')
br.fill('password','YOUR_ACCOUNT_PASSWORD')
button = br.find_by_name("")
button.click()

stringurl=br.url
stringurl2=stringurl.split("id=",1)[1]
id=stringurl2.split("id=",1)[1]
jsstring="window.parent.openPage('SendSMS?id="+id+"', 'aSendSMS', 'aSMS', 'ulSMS')"
br.execute_script(jsstring)
time.sleep(8)
br.execute_script(jsstring)
print "JS Executed"
time.sleep(8)

with br.get_iframe('by2Frame') as iframe:
	iframe.fill("sendSMSMsg","Well, I guess robot's do send SMSes when spandan wants them to ;)")
	iframe.find_by_tag("input")[10].fill("THE_PHONE_NUMBER_YOU_WANT_TO_SEND_SMS_TO")
	button2=iframe.find_by_id("btnsendsms").first
	print button2.value
	button2.click()
