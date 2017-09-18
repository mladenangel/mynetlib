#!/usr/bin/env python
#delwin

import smtpd
import asyncore
import argparse

class CustomSMTPServer(smtpd.SMTPServer):
    
    def process_message(self, peer, mailfrom, rcpttos, data):
        print ('Message Received from:', peer)
        print ('From:', mailfrom)
        print ('To  :', rcpttos)
        print ('Message :', data)
        return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mail Server Example')
    parser.add_argument('--host', action="store", dest="host", type=str, required=True)
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    server = CustomSMTPServer((given_args.host, given_args.port), None)
    asyncore.loop()


