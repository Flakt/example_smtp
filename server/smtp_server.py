from smtpd import SMTPServer

import asyncore


class EmlServer(SMTPServer):
    
    def process_message(self, peer, mailfrom, rcpttos, data, *kwargs):
        print("\n --- A new mail has been recieved --- ")
        print ("\n --- From: " + mailfrom.decode() + " using client: " + peer.decode() + " ---")
        print ("\n --- To: " + rcpttos.decode() + " ---")
        print(data.decode())


def run():
    EmlServer(('127.0.0.1', 5001), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass


if __name__ == 'main':
    run()