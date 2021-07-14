from datetime import datetime
from smtpd import SMTPServer
import asyncore


class EmlServer(SMTPServer):
    no = 0

    def process_message(self, peer, mailfrom, rcpttos, data, mail_options=None, rcpt_options=None):
        (ip, port) = peer
        print("\n --- A new mail has been recieved --- ")
        print("\nUsing address " + ip + " and port " + str(port))
        print("\nFrom: " + mailfrom)
        print("To following:")
        print(' '.join(map(str, rcpttos)))
        print("\n ------------------------------------ ")
        print(data.decode())


def run():
    EmlServer(('127.0.0.1', 5001), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()