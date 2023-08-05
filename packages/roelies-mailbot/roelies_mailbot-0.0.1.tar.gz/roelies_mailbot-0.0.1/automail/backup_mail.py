import smtplib
from email.message import EmailMessage
from datetime import datetime
import os
import base64
from cryptography.fernet import Fernet
from cryptography import hazmat
from getpass import getpass

class AutoEmail():
    """
    Creates instance of an email message. Logging in using the login classmethod 
    is only required once. !You don't have to log in every time you create a new 
    instance of the class, only if the emailserver throws an error.    
    """
    loggin = False
    email = ''

    def __init__(self, reciever):
        self.msg = EmailMessage()
        self.msg['Subject'] = 'no subject given'

        try:
            address = str(reciever)
        except:
            print()

        self.msg['To'] = address
        self.message = 'no message given'
        self.footer = 'no footer given'

        self.HasAttachment = False
        self.Attachments = []

    @classmethod
    def login(cls):
        """
        Reads from encrypted files and logs user into Gmail if correct 
        credentials are given.
        """
        if not os.path.exists(os.path.expanduser('~/UniMailBot/x.x')):
            print('No account found...')
        else:
            with open(os.path.expanduser('~/UniMailBot/x.x'), 'rb') as k:
                key = k.read()
            f = Fernet(key)
            with open(os.path.expanduser('~/UniMailBot/ergoiwgo.13240nionaonwq'), 'rb') as k:
                EMAIL = f.decrypt(k.read()).decode()
            
            with open(os.path.expanduser('~/UniMailBot/0o2w3hnrawnalfe.s2k2kk1'), 'rb') as k:
                PASSWORD = f.decrypt(k.read()).decode()

            try:
                cls.smtp = smtplib.SMTP('smtp.gmail.com', 587)
                cls.smtp.ehlo()
                cls.smtp.starttls()
                cls.smtp.ehlo()
                cls.smtp.login(EMAIL, PASSWORD)
                cls.email = EMAIL
                cls.loggin = True
                EMAIL, PASSWORD = '', ''
                print('Logged in succsessfully!')
            except:
                print('Your credentials are incorrect.')
                EMAIL, PASSWORD = '', ''

    @classmethod
    def create_safe(cls):
        """
        Creates encrypted files with password and username to be read by the
        login classmethod in the future.
        """
        try:
            os.mkdir(os.path.expanduser('~/UniMailBot'))
        except FileExistsError:
            pass
        
        if os.path.exists(os.path.expanduser('~/UniMailBot/x.x')):
            print('Key already exists!')
            while True:
                try:
                    yes = input('Do you wish to create a new key and loose permanent access to your old files? (y/n)')
                    if yes == 'y' or yes =='Y':
                        break
                    elif yes == 'n' or yes =='N':
                        return True
                    else:
                        print('Invalid input')
                except:
                    print('Invalid input')

        key = Fernet.generate_key()
        with open(os.path.expanduser('~/UniMailBot/x.x'), 'wb') as k:
            k.write(key)

        print('Enter your email now:...')
        email = input().encode()
        print('Enter you password now:...')
        password = getpass().encode()

        f = Fernet(key)
        with open(os.path.expanduser('~/UniMailBot/ergoiwgo.13240nionaonwq'), 'wb') as k:
            k.write(f.encrypt(email))
        
        with open(os.path.expanduser('~/UniMailBot/0o2w3hnrawnalfe.s2k2kk1'), 'wb') as k:
            k.write(f.encrypt(password))

    def addfile(self, file):
        """Adds file as attachment to current message"""
        try:
            with open(str(file), 'rb') as f:
                file_data = f.read()
                file_name = f.name
            self.HasAttachment = True
            self.Attachments.append([file_data, file_name])
        except OSError:
            print('Error reading file')

    def change_subject(self, new_subject):
        """Changes email subject"""
        try:
            sub = str(new_subject)
        except:
            print('Invalid subject: no string given.')
            return True
        if len(sub) > 998:
            print('Invalid subject: subject too long')
            return True
        else: self.msg['Subject'] = sub

    def change_message(self, new_message, append=False):
        """Changes email message"""
        try:
            mes = str(new_message)
        except:
            print('Invalid message: no string given')
            return True
        if append:
            self.message += mes
        else:
            self.message = mes

    def set_footer(self, footer):
        """Changes footer of email message"""
        try:
            foot = str(footer)
        except:
            print('Invalid footer: no string given')
            return True
        self.footer = foot

    def set_recipiant(self, to):
        try:
            rep = str(to)
        except:
            print('Invalid recipiant: no string given')
            return True
        self.msg['To'] = rep

    def send_email(self):
        """Sends msg object as email"""
        self.message += f'\n\n---Automated footer---\nMessage sent on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} by backup email bot.\n'
        self.message += str(self.footer)
        if self.HasAttachment: self.message += 'Attachment included'
        self.message += f'\n---Automated footer---'

        self.msg.set_content(self.message)

        while not AutoEmail.loggin:
            AutoEmail.login()

        self.msg['From'] = AutoEmail.email

        if self.HasAttachment:
            for file in self.Attachments:
                self.msg.add_attachment(file[0], maintype='application', subtype='octet-stream', filename=file[1])
            print('Files uploaded!')

        AutoEmail.smtp.send_message(self.msg)
        AutoEmail.smtp.quit()
        print('Email sent!')