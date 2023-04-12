#HANDLING REQUEST ERRORS
import requests

reply = requests.get('http://localhost:3000')
print(reply.status_code)
print(reply.headers)
print(reply.text)

#HEAD, #CONNECT, #OPTIONS, #TRACE


##RequestException
##|___HTTPError
##|___ConnectionError
##|   |___ProxyError	
##|   |___SSLError	
##|___Timeout
##|   |___ConnectTimeout
##|   |___ReadTimeout
##|___URLRequired
##|___TooManyRedirects
##|___MissingSchema
##|___InvalidSchema
##|___InvalidURL
##|   |___InvalidProxyURL
##|___InvalidHeader
##|___ChunkedEncodingError
##|___ContentDecodingError
##|___StreamConsumedError
##|___RetryError
##|___UnrewindableBodyError


try:
    reply = requests.get('http://localhost:3001', timeout=1)
except requests.exceptions.ConnectionError:
    print('Nobody\'s home, sorry!')
else:
    print('Everything fine!')



try:
    reply = requests.get('http:////////////')
except requests.exceptions.InvalidURL:
    print('Recipient unknown!')
else:
    print('Everything fine!')




try:
    reply = requests.get('http://localhost:3000', timeout=1)
except requests.exceptions.Timeout:
    print('Sorry, Mr. Impatient, you didn\'t get your data')
else:
    print('Here is your data, my Master!')



