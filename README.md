# checkEndpoint

checkEndpoint is a Python script that checks endpoints.

The user provides input; input must start with either "https://" or "http://".

If the program failes to connect to the endpoint; it will attempt attemmpt to check SSL certificate expiry
if is an SSL endpoint (ie: "https://yahoo.com").

Usage instructions:
- clone the repo
- cd into repo directory
- run: pip install -r requirements.txt
- on the commandline type: python3 checkEndpoint.py
