# AutomatedSMSIndia
I was recently contacted by an NGO, BloodConnect, to automate their process of sending SMS reminders to their previous blood donors. After a LOT of fiddling with three python libraries and 3-4 Indian SMS websites, I was able to make this work!

What you need to run this :-
1) python
2) splinter for python. (Install on mac using pip install splinter)
3) Mozilla Firefox
4)You'll have to register on www.160by2.com, and it should work out just fine. 

Just change the following in the code :-

1)YOUR_PHONE_NUMBER_USED_TO_CREATE_160BY2_ACCOUNT
2)YOUR_ACCOUNT_PASSWORD
3) The message you want to send. right now it's set to "Well, I guess robot's do send SMSes when spandan wants them to ;)"
4)THE_PHONE_NUMBER_YOU_WANT_TO_SEND_SMS_TO

After making these changes, simply go to the terminal and type "python file_name_with_full_path.py"
