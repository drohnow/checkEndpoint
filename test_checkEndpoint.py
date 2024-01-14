from checkEndpoint import httpStatusCode, checkCert

# start - httpStatusCode() test validation
def test_statusCode101(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "https://httpstat.us/101")
    endPoint, status_code = httpStatusCode()
    assert status_code == 101
    
def test_statusCode200(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "https://httpstat.us/200")
    endPoint, status_code = httpStatusCode()
    assert status_code == 200


def test_statusCode400(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "https://httpstat.us/400")
    endPoint, status_code = httpStatusCode()
    assert status_code == 400

def test_statusCode404(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "https://httpstat.us/404")
    endPoint, status_code = httpStatusCode()
    assert status_code == 404

def test_statusCode410(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "https://httpstat.us/410")
    endPoint, status_code = httpStatusCode()
    assert status_code == 410

def test_statusCode500(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "https://httpstat.us/500")
    endPoint, status_code = httpStatusCode()
    assert status_code == 500

def test_statusCode503(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "https://httpstat.us/503")
    endPoint, status_code = httpStatusCode()
    assert status_code == 503

def test_statusCode505(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "https://httpstat.us/505")
    endPoint, status_code = httpStatusCode()
    assert status_code == 505

def test_statusCodeInstrumentalai(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "https://api.instrumental.ai/healthcheck")
    endPoint, status_code = httpStatusCode()
    assert status_code == 200

def test_statusCodeNegative(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "https://api.instrumental.ai/healthcheck")
    endPoint, status_code = httpStatusCode()
    assert status_code != 404
# end - httpStatusCode() test validation


# start - checkCert() test validation
def test_checkCertExpired():
    certStatus = checkCert("expired.badssl.com")
    assert certStatus == "expired.badssl.com cert error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1006)"

def test_checkCertNotExpired():
    certStatus = checkCert("api.instrumental.ai")
    assert certStatus == "api.instrumental.ai cert is fine"
# end - checkCert() test validation

