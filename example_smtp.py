from objects.SocketObject import SocketObject

import sys

## TODO: Replace string inserts with parameterized inserts so that SMTP injections
##       does not work

##       Consider a separate function which handles sending and reading return codes

HOST_IP = "127.0.0.1"
HOST_PORT = 5001
DOMAIN = "example.com"
SENDER = "sender@test.com"
RECIPIENT = "recipient@test.com"

def send_smtp_mail():
    clientSocket = SocketObject(HOST_IP, HOST_PORT)

    conn_resp = clientSocket.connect()
    if conn_resp[:3] != '220':
        error_code('220')

    helo_resp = clientSocket.send_command("HELO " + DOMAIN + "\r\n")
    if helo_resp[:3] != '250':
        error_code('250')

    mail_from_resp = clientSocket.send_command("MAIL FROM:" + SENDER + "\r\n")
    if mail_from_resp[:3] != '250':
        error_code('250')

    clientSocket.send_no_ret_command("RCPT TO:" + RECIPIENT + "\r\n")

    ## Does not check for 354 return code
    data_resp = clientSocket.send_command("DATA\r\n")
    if data_resp[:3] != '250':
        error_code('250')
    
    content_type = "Content-Type: text/html;\n"
    smtp_headers = "From: " + SENDER + "\nTo: " + RECIPIENT + "\nSubject: Happy birthday :D\n\n"
    content = "I hope you've hade a wonderful day!"
    ending_dot = "\r\n.\r\n"
    message_command = content_type + smtp_headers + content + ending_dot

    mesg_resp = clientSocket.send_command(message_command)
    if mesg_resp[:3] != '250':
        error_code('250')

    clientSocket.close_connection()


def error_code(code):
    print(code + " not replied from SMTP-Server")
    sys.exit(1)


if __name__ == '__main__':
    send_smtp_mail()