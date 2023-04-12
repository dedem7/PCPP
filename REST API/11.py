#WORKING WITH SERVER AND HANDLING EXCEPTIONS

import sys
import requests



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


if len(sys.argv) == 3:
    port_number = sys.argv[2]
    if "http://" in sys.argv[1] or "https://" in sys.argv[1]:
        server_addr = sys.argv[1] + ":" + port_number
    else:
        server_addr="http://" + sys.argv[1] + ":" + port_number
    
elif len(sys.argv)<3:
    if "http://" in sys.argv[1]:
        server_addr = sys.argv[1]+":80"
    elif "https://" in sys.argv[1]:
        server_addr = sys.argv[1]+":443"
    else:
        server_addr="http://"+sys.argv[1]+":80"
print(server_addr)

try:
    reply = requests.head(server_addr,timeout=5)

except requests.exceptions.InvalidURL:
    print("Wrong address")

except requests.exceptions.HTTPError:
    print("HTTP Server error")
   
except requests.exceptions.Timeout:
    print("Connection Timed out")
    sys.exit(3)

except requests.exceptions.ConnectionError:
    print("Connection failed")
    sys.exit(4)
 
except Exception as se:
    print(se)
    print("HTTP 1.1 302 Found")

else:
    #print(requests.codes.__dict__)
    code_messages = []
    for k,v in requests.codes.__dict__.items():
        if reply.status_code == v:
            code_messages.append(k)
    print("The status code is:",reply.status_code,"\nThe messages related to this code:",code_messages)
            
    
    
