#  0x10. Python - Network #0 

## General

- What a URL is
Stand of : (Uniform Resource Locator) Is the address of a website.
- What HTTP is
Protocal for transmitting web pages over internet.
- How to read a URL
```bash

http://www.example.com:80/path/to/page?name=example#section1

scheme://subdomain.domain:port/path?query_string#fragment

- Scheme: http => specify the protocol "http, https"
- Subdomain: www => 
- Domain: example.com
- Port: 80 => the server port 
- Path: /path/to/page
- Query String: name=example
- fragment : is to go the page that have that id for example 'id="section1'
```

- What a query string is
```bash
?name=example&
it contain the data passed to web applications 
```

- What an HTTP request is
```bash
import requests
respose = requests.get("<url>")
print(respose.text)
```
- What an HTTP response is
```bash
import requests
respose = requests.get("<url>")
print(respose.status_code)
print(respose.headers)
print(respose.text)
```
- What HTTP headers
```bash
import requests

url = 'https://example.com/api'

headers = {
    'User-Agent': 'my-app/0.0.1',
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cookie': 'sessionid=1234567890',
    'If-Modified-Since': 'Wed, 21 Oct 2015 07:28:00 GMT',
    'If-None-Match': '5d8c72a2a0c7c',
    'Host': 'example.com',
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.headers)
print(response.text)


```
- What the HTTP message body is
```bash
# is the body contain the data
import requests
response = requests.get("http://example.com")
print(reponse.constent)
```
- What an HTTP request method is
 "GET, POST, PUT, DELETE"
- What an HTTP response status code is
 "200, 404"
- What an HTTP Cookie is
 "small pieces of data stored by the browser to remember the user"
- How to make a request with cURL
```bash
curl http://example.com

```
- What happens when you type google.com in your browser (Application level)
```bash
1. DNS Lookup      : Translates google.com to ip address
2. HTTP Request    : Browser sends to Http Request to the ip address
3. Server Response : The ip server send http reponse

4. Rending         : The browser rendering the html content
```

# CURL
```bash
# set some header options
curl -H "Authorization: Bearer token"
# using silent mode 
curl --silent https://example.com/api/data
# follow http redirects  301, 302
curl -L https://example.com
# set cookie 
curl -b "name=value" <url>
# send body data
curl -d "username=johndoe&password=pass123" https://example.com/api/login
# save body to the file 
curl -o filename.txt https://example.com/api/data
# info : The first digit of status codes that indicate a server error is 5. Server error status codes in the HTTP protocol start with the digit 5, specifically in the range from 500 to 599.

```