
import datetime
import socket
import ssl

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


def ssl_valid_time_remaining(hostname: str) -> datetime.timedelta:
    """Get the number of days left in a cert's lifetime."""
    expires = ssl_expiry_datetime(hostname)

    return expires - datetime.datetime.utcnow()


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
        