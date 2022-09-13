import pyperclip
import re

def main():
    text = str(pyperclip.paste())
    phone_regex = re.compile(r"""
        (\d{2}|\(\d{2}\)|\d{3}|\(\d{3}\))? # br area code
        (\s|-|\.) # separator
        (\d{4,5}|\d{3}) # first 4 or 5 digits
        (\s|-|\.) # separator
        (\d{4}) # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
        """, re.VERBOSE)
    email_regex = re.compile(r"""
        [a-zA-Z0-9._%+-]+ # username
        @ # @ symbol
        [a-zA-Z0-9.-]+ # domain name
        \.[a-zA-Z]{2,4} # dot-something
        """, re.VERBOSE)
    matches = []
    phonenumbers = phone_regex.findall(text)
    for groups in phonenumbers:
        phone_number = '-'.join([groups[0], groups[2], groups[4]])
        if groups[5] != '':
            phone_number += ' x' + groups[5]
        matches.append(phone_number)
    email_adresses = email_regex.findall(text)
    for groups in email_adresses:
        matches.append(groups)
    if len(matches) > 0:
        text = '\n'.join(matches)
        modified_text = text
        pyperclip.copy(modified_text)
        print('Copied to clipboard')
        print(text)
    else:
        print('No phone numbers or email adresses found.')


if __name__ == '__main__':
    main()