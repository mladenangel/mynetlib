#!/usr/bin/env python
#delwin

import getpass 
import poplib
import argparse

def mail_client(host, port, user, password):
    Mailbox = poplib.POP3_SSL(host, port) 
    Mailbox.user(user) 
    Mailbox.pass_(password) 
    numMessages = len(Mailbox.list()[1])
    print (Mailbox.retr(1)[1])
    Mailbox.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mail Server Example')
    parser.add_argument('--host', action="store", dest="host", type=str, required=True)
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    parser.add_argument('--user', action="store", dest="user", type=str, required=True)
    password = getpass.getpass("Enter your Password:")
    given_args = parser.parse_args()
    mail_client(given_args.host, given_args.port, given_args.user, password)

