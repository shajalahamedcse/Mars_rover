import socket
import sys

class MarsRoverMainClass:

    def Server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the address given on the command line
        #server_name = sys.argv[1]
        server_name='localhost'
        server_address = (server_name, 10000)
        print >>sys.stderr, 'starting up on %s port %s' % server_address
        sock.bind(server_address)
        sock.listen(1)

        while True:
            print >>sys.stderr, 'waiting for a connection'
            connection, client_address = sock.accept()
            try:
                print >>sys.stderr, 'client connected:', client_address
                while True:
                    data = connection.recv(16)
                    print >>sys.stderr, 'received "%s"' % data
                    if data:
                        connection.sendall(data)
                    else:
                        break
            finally:
                connection.close()

    def Client(self):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port on the server given by the caller
        #server_name=sys.argv[1]
        server_name='localhost'
        server_address = (server_name, 10000)
        print >>sys.stderr, 'connecting to %s port %s' % server_address
        sock.connect(server_address)

        try:
    
            message = 'This is the message.  It will be repeated.'
            print >>sys.stderr, 'sending "%s"' % message
            sock.sendall(message)

            amount_received = 0
            amount_expected = len(message)
            while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                print >>sys.stderr, 'received "%s"' % data

        finally:
            sock.close()

newRobot=MarsRoverMainClass()


input_choice=raw_input("{Do you need server?")
if(input_choice[0]=='y'):
    newRobot.Server()
else:
    continue

