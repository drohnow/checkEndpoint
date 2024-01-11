import requests
import time
from colorama import Fore
import ssl
import datetime
import socket

# def information about list of http status codes to decimate to program user
def docMessage():
    docURL = 'https://en.wikipedia.org/wiki/List_of_HTTP_status_codes'
    print("see %s for more information about http status codes" % docURL)

# def checks https:// and http:// endpoints; takes response and returns infornamtion about http status code and site status.
def checkEndpoint(endPointl):
    try:
            ret = requests.head(endPoint)
            print(ret.status_code)
            # prints the int of the status code. Find more at httpstatusrappers.com :)

            print('checking endpoint: %s' % endPoint)
            time.sleep(2)
        
            if ret.status_code == 200:
                print('status code is: ' + Fore.GREEN + str(ret.status_code))
                print(Fore.WHITE + 'This indicates that the endpoint is online and healthy!')
                docMessage()
            elif ret.status_code == 404:
                print('status code is: ' + Fore.RED + str(ret.status_code))
                print(Fore.WHITE + 'This indicates that the endpoint is unreachable\n')
                print("This status code indicates the file or page that the browser is requesting wasn’t found by the server.")
                docMessage()
            elif ret.status_code == 410:
                print('status code is: ' + Fore.RED + str(ret.status_code))
                print(Fore.WHITE + 'This indicates that the endpoint is \n')
                print("This status code indicates that the page is no longer available from the server and no forwarding address has been set up.")
                docMessage()
            elif ret.status_code == 500:
                print('status code is: ' + Fore.RED + str(ret.status_code))
                print(Fore.WHITE + 'This indicates that the endpoint is offline and unhealthy!\n')
                print("This status code indicates status that there is an internal problem with the server.")
                docMessage()
            elif ret.status_code== 503:
                docMessage()
                print('status code is: ' + Fore.RED + str(ret.status_code))
                print(Fore.WHITE + 'This indicates that the endpoint is offline and unhealthy!\n')
                print("This status code indicates status that the server in currently overloaded or under maintenance.")
                docMessage()
            elif ret.status_code == 505:
                docMessage()
                print('status code is: ' + Fore.RED + str(ret.status_code))
                print(Fore.WHITE + 'This indicates that the endpoint is offline and unhealthy!\n')
                print("This status code indicates status that the server in currently overloaded or under maintenance.")
                docMessage()
            else:
                print('status code is: ' + Fore.YELLOW + str(ret.status_code))
                print(Fore.WHITE + 'If the the status code is "1xx", then endpoint received the request and responded with an informational response \n')
                print(Fore.WHITE + 'If the the status code is "3xx", then endpoint redirected the request another endpoint \n')
                docMessage()

    except requests.ConnectionError:
            try:
                # if endpoint fails, then attempts to check SSL certificate for SSL endpoints.
                print("failed to connect...if this is an SSL endpoint that will check SSL certificate expiry")
                hostname = (endPoint[8:].split("/"))
                print(test_host(hostname[0]))
            except:
                # response to user that endpoint does not exist.
                print("not able to check SSL certificate expiry; the endpoint may be misspelled or does not exist")

    # def returns ssl expire date
    def ssl_expiry_datetime(hostname: str) -> datetime.datetime:
        ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'

        context = ssl.create_default_context()
        conn = context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname=hostname,
    )

        conn.connect((hostname, 443))
        ssl_info = conn.getpeercert()
        return datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)

    # def to let user know when the SSL certificate will expire if within 30 days
    def ssl_valid_time_remaining(hostname: str) -> datetime.timedelta:
        """Get the number of days left in a cert's lifetime."""
        expires = ssl_expiry_datetime(hostname)

        return expires - datetime.datetime.utcnow()

    # def checks SSL certificate status
    def test_host(hostname: str, buffer_days: int=30) -> str:
        """Return test message for hostname cert expiration."""
        try:
            will_expire_in = ssl_valid_time_remaining(hostname)
        except ssl.CertificateError as e:
            return f'{hostname} cert error {e}'
        except ssl.SSLError as e:
            return f'{hostname} cert error {e}'
        except socket.timeout as e:
            return f'{hostname} could not connect'
        else:
            if will_expire_in < datetime.timedelta(days=0):
                return f'{hostname} cert will expired'
            elif will_expire_in < datetime.timedelta(days=buffer_days):
                return f'{hostname} cert will expire in {will_expire_in}'
            else:
                return f'{hostname} cert is fine'


# entry point into program
try:
    endPoint = input("Enter endpoint beginging with 'https://' or 'http://' : ")
    checkEndpoint(endPoint)
except:
    print("Input was null or was not formatted correctly")
    print("This program checks endpoints starting with 'https://' or 'http://")
    print("...please try again")
    

    
