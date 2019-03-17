# django-raduis-2fa

## PyOTP

https://github.com/pyauth/pyotp

PyOTP is a Python library for generating and verifying one-time passwords. 

## PyRAD

https://github.com/wichert/pyrad

pyrad is an implementation of a RADIUS client/server as described in RFC2865. It takes care of all the details like building RADIUS packets, sending them and decoding responses.

## QRious

https://github.com/neocotic/qrious

QRious is a pure JavaScript library for generating QR codes using HTML5 canvas.

```
def index(request):
    secret = 'HIGSGNJ34NOOBPJM'
    totp = pyotp.TOTP(secret)
    qr = pyotp.totp.TOTP(secret).provisioning_uri(
        "tom@example.com",
        issuer_name="Django"
    )
    return HttpResponse(f'''<html>
<body>
<center>
    <canvas id="qr"></canvas>

    <script src="node_modules/qrious/dist/qrious.js"></script>
    <script>
    (function() {{
        const qr = new QRious({{
            element: document.getElementById('qr'),
            size: 200,
            value: '{qr}'
        }});
    }})();
    </script>
    <h1>{totp.now()}</h1>
</center>
</body>
</html>''')

```

## qrcode-terminal

Display QR codes in terminal.

```
import pyotp
import qrcode_terminal

secret = 'HIGSGNJ34NOOBPJM'
totp = pyotp.TOTP(secret)
qr = pyotp.totp.TOTP(secret).provisioning_uri(
    "tom@example.com",
    issuer_name="Django"
)
qrcode_terminal.draw(qr)
```

## See Also:

https://github.com/Bouke/django-two-factor-auth Complete Two-Factor Authentication for Django. Built on top of the one-time password framework django-otp and Django's built-in authentication framework django.contrib.auth.

https://pypi.org/project/django-otp/ This project makes it easy to add support for one-time passwords (OTPs) to Django.


# Usage

```
npm install
python3 -m venv .env
source .env/bin/activate
pip install -r requirements/local.txt
python radius_2fa/manage.py migrate
python radius_2fa/manage.py collectstatic
python radius_2fa/manage.py runserver
```
