from socket import *

UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(("192.168.1.2", 1337))

print '\nRunning...\n'

while 1:
    data, addr = UDPSock.recvfrom(1024)
    if not data:
        print 'Client has exited!'
        break
    else:
        line = '<%s>: %s' % (data[data.index("@")+1:], data[:data.index("@")])
        print '<%s>: %s' % (data[data.index("@")+1:], data[:data.index("@")])
        
UDPS.close()


