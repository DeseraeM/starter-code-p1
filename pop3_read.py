#!/usr/bin/env python3

# Include needed libraries. Do _not_ include any libraries not included with
# Python3 (i.e. do not use `pip`).
import socket
import sys

BUFFER_SIZE = 4096
PASSWORD = 'password'

# Parse command-line arguments.
host     = sys.argv[1]
port     = int(sys.argv[2])
username = sys.argv[3]

# Establish a TCP connection with the POP3 server.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Read greeting from the server.
data = s.recv(BUFFER_SIZE)
response = data.decode('utf-8')

if not response.startswith('+OK'):
    raise Exception('+OK not received from server.')

# Note: the POP3 spec requires every command to end with \r\n, not just \n.

# Log in with USER and PASS commands.
s.send(f"USER {username}\r\n".encode())
data = s.recv(BUFFER_SIZE)
response = data.decode('utf-8')

if not response.startswith('+OK'):
    raise Exception('+OK not received from server.')

s.send(f"PASS {PASSWORD}\r\n".encode())
data = s.recv(BUFFER_SIZE)
response = data.decode('utf-8')

if not response.startswith('+OK'):
    raise Exception('+OK not received from server.')


# Get the number of messages with the LIST command.
# Note: the LIST response spans multiple lines and ends with a line
# containing only '.'. Do not assume a fixed number of recv() calls will
# capture the full response — depending on the network, the entire response
# may arrive in a single recv() or be split across several. Accumulate data
# until you have seen the terminator.
s.send('LIST\r\n'.encode())
data = s.recv(BUFFER_SIZE)
response = data.decode('utf-8')

if not response.startswith('+OK'):
    raise Exception('+OK not received from server.')
ldata = []
response = '' 
while '\r\n.\r\n' not in response:
    ldata.append(s.recv(BUFFER_SIZE))
    last = ldata[-1]
    response = b''.join(ldata).decode('utf-8')

# Retrieve andl print each message with the RETR command.
# The same caveat about multi-line responses applies here.
# Print messages separated by a line containing only '---'.
new_response = b''.join(ldata).decode('utf-8')
for d in new_response.split()[1:]
    if d.splrip() == '.'
        break 
    s.send(f"RETR {newdata.split()[0]}\r\n".encode())
    rdata = []
    response = '' 
    while '\r\n.\r\n' not in response:
        rdata.append(s.recv(BUFFER_SIZE))
        new =rdata[-1] 
        response = b''.join(rdata).decode('utf-8')
    print(b''.join(rdata).decode('utf-8'))
    print("---")
s.send('QUIT\r\n'.encode())


# Close the socket when finished.
s.close()