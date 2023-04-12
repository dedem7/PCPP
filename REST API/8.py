#ACCESS SERVER USING SOCKET MODULE
import sys
import socket

if len(sys.argv) not in [2, 3]:
    print("Improper number of arguments: at least one is required and not more than two are allowed:\
        \n- http server's address (required)\
        \n- port number (defaults to 80 if not specified)")
    sys.exit(1)


elif len(sys.argv) == 3 and not sys.argv[2].isdigit():
    print("Port number is invalid - exiting.")
    sys.exit(2)
    
elif len(sys.argv) == 3 and sys.argv[2].isdigit():
    if int(sys.argv[2])<1 or int(sys.argv[2])>=65535:
        print("Port number is invalid - exiting. Not allowed range.")
        sys.exit(2)


server_addr = sys.argv[1]
if len(sys.argv)==3:
    port_number = int(sys.argv[2])
else:
    port_number = 80
    


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
sock.settimeout(5)

try: 
    sock.connect((server_addr, port_number))
    
    sock.send(b"HEAD / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")

except (TimeoutError,socket.timeout):
    print("Connection Timed out")
    sys.exit(3)

except ConnectionError:
    print("Connection failed")
    sys.exit(4)

except socket.gaierror:
    print("Wrong address")

    
except socket.error as se:
    print(se)
    print("HTTP 1.1 302 Found")

else:
    reply = sock.recv(10000)
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
    print(reply.decode().split('\r\n')[0])
    
    
