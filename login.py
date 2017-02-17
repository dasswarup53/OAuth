from __future__ import print_function
import httplib2
import os
import webbrowser as wb
from tkinter import *
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Quickstart'

def fb():
    print ("fb")
    wb.open("https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwi1zaKa88DRAhVLgI8KHWfrD0EQFggZMAA&url=https%3A%2F%2Fen-gb.facebook.com%2Flogin%2F&usg=AFQjCNFmud4e0oTnY2Kyg4MS0-FsguMS3g&sig2=pjHd8Nhd6DA6V5qxGCOqFQ&bvm=bv.144224172,d.c2I")

def google():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

def get_credentials():

    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """
    root=Tk()
    b=Button(root,command=fb)
    b.grid(row=0,column=0)
    photo=PhotoImage(file="fb.gif")
    b.config(image=photo,width="500",height="100",bg="grey")
    #b.pack(side=LEFT)

    b2=Button(root,command=google)
    b2.grid(row=1,column=0)
    photo2=PhotoImage(file="google.gif")
    b2.config(image=photo2,width="500",height="100",bg="grey")
    #b2.pack(side=BOTTOM)

    root.mainloop()

    
    
##    results = service.users().labels().list(userId='me').execute()
##    labels = results.get('labels', [])
##
##    if not labels:
##        print('No labels found.')
##    else:
##      print('Labels:')
##      for label in labels:
##        print(label['name'])


if __name__ == '__main__':
    main()
