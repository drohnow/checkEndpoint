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
- test_checkEndpoint.py contains the following tests:
  - 10 tests for httpStatusCode() function.
  - 2 tests for test_host() function.
- Run test: python3 -m pytest