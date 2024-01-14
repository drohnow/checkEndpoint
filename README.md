# checkEndpoint

checkEndpoint is a Python script that checks endpoints.

The user provides input; input must start with either "https://" or "http://".

If the program detects an SSL endpoint then it will check status of the SSL certificate to the endpoint before collecting
the status of the http status code.

Usage instructions:
- clone the repo
- cd into repo directory
- run: pip install -r requirements.txt

Testing:
- test_checkEndpoint.py contains 10 tests for httpStatusCode() function.
  (The httpsStatusCode function is responsible for retrieving http status code for the endpoint.)
- Run test: python3 -m pytest