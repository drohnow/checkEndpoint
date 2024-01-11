import urllib.request as urllib2
from colorama import Fore
import os
import time
from checkCert import test_host
from checkHost import hostname_resolves

# https://github.com/gruntwork-io/terraform-aws-utilities.git
# api.instrumental.ai/healthcheck
# https://localhost:8000/admin
# expired.badssl.com
# https://www.yahoo.com
url = input("Enter endpoint: ")


def checkProtocol(url):
    eval = url[:5]
    if eval == "https":
        protocol = "https"
    else: protocol = "http"
    return protocol
    

def checkEndpoint(url):
    if not hostname_resolves(url):
        print("endpoint does not resolve to an IP address, please try again")
        exit
    else:
        
        url = "https://" + url

        docURL = 'https://en.wikipedia.org/wiki/List_of_HTTP_status_codes'
        try:
            ret = urllib2.urlopen(url)

            print('checking endpoint: %s' % url)
            time.sleep(2)
        
            if ret.code == 200:
                print('status code is: ' + Fore.GREEN + str(ret.code))
                print(Fore.WHITE + 'This indicates that the endpoint is online and healthy!\n')
            elif ret.code == 404:
                print('status code is: ' + Fore.RED + str(ret.code))
                print(Fore.WHITE + 'This indicates that the endpoint is unreachable\n')
                print("This status code indicates the file or page that the browser is requesting wasn’t found by the server.")
            elif ret.code == 410:
                print('status code is: ' + Fore.RED + str(ret.code))
                print(Fore.WHITE + 'This indicates that the endpoint is \n')
                print("This status code indicates that the page is no longer available from the server and no forwarding address has been set up.")
            elif ret.code == 500:
                print('status code is: ' + Fore.RED + str(ret.code))
                print(Fore.WHITE + 'This indicates that the endpoint is offline and unhealthy!\n')
                print("This status code indicates status that there is an internal problem with the server.")
            elif ret.code == 503:
                print('status code is: ' + Fore.RED + str(ret.code))
                print(Fore.WHITE + 'This indicates that the endpoint is offline and unhealthy!\n')
                print("This status code indicates status that the server in currently overloaded or under maintenance.")
            else:
                print('status code is: ' + Fore.YELLOW + str(ret.code))
                print(Fore.WHITE + 'If the the status code is "1xx", then endpoint received the request and responded with an informational response \n')
                print(Fore.WHITE + 'If the the status code is "3xx", then endpoint redirected the request another endpoint \n')
                print("Please see %s for more information" % docURL)
            
        except:
            protocol = checkProtocol(url)
            if protocol == "http":
                exit
            else:
                print('The request encountered an exception which means that either the endpoint does not use SSL ("https://) or the SSL certificate has expired...')
                print('The endpointChecker will now check if this site is using SSL and if the SSL certificate has expired...')
                time.sleep(3)
                try:
                    testCert = test_host(url)
                    print(testCert)
                except:
                    url = url.replace("https", "http")
                    print('validated that the endpoint is not using SSL')
                    print('The endpointChecker will now check : %s' % url)
                    checkEndpoint(url)

                    print("\n\n", Fore.WHITE + 'see %s for more information about http status codes' % docURL )

checkEndpoint(url)



