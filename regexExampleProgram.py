#! python3
import re, pyperclip

#DONE: Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 123345, x12345

(
((\d\d\d)|(\(\d\d\d\)))?    #area code (optional)
(\s|-)    #first seperator
\d\d\d    #first 3 digits
-    #seperator
\d\d\d\d    #last 4 digits
(((ext(\.)?\s)|x)   #extension word-part (optional)
(\d{2,5}))?   #extension number-part (optional)
)
''', re.VERBOSE)

#DONE: Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.place

[a-zA-Z0-9_.+]+    # name part
@    # @ sympbol
[a-zA-Z0-9_.+]+    # domain name part
''', re.VERBOSE)

#DONE: Get the text off the clipboard
text = pyperclip.paste()

#DONE: Extract the email/phone from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)
allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#DONE: Copy the extracted email/phone to clipboard
results = "\n".join(allPhoneNumbers) + "\n" + "\n".join(extractedEmail)
pyperclip.copy(results)
