# checkEndpoint

checkEndpoint is a Python script that checks endpoints.

The user provides input; input must start with either "https://" or "http://".

If the program failes to connect to the endpoint; it will attempt attemmpt to check SSL certificate expiry
if is an SSL endpoint (ie: "https://yahoo.com").

Usage instructions:
- clone the repo
- cd into repo directory
- run: pip install -r requirements.txt

Testing:
- test_checkEndpoint.py contains 10 tests for httpStatusCode() function.
  (The httpsStatusCode function is responsible for retrieving http status code for the endpoint.)
- Run test: python3 -m pytest