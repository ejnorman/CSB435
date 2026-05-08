#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#  "pyotp"
# ]
# ///

import urllib.request
import urllib.parse
import sys
import pyotp

BASE_URL = "http://class.nsc.aoeu.com/d/totp-check"

def main():
    username = "your-username"
    otp_secret = "PSNKXNVTM7SZ5G77445JYAMLE5IE6YTU"
    totp = pyotp.TOTP(otp_secret)
    otp_code = totp.now()

    params = urllib.parse.urlencode({'username': username, 'otp': otp_code})
    url = f"{BASE_URL}?{params}"

    try:
        with urllib.request.urlopen(url) as response:
            result = response.read().decode('utf-8')
            print(result)
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        print("\nResponse body:")
        error_body = e.read().decode('utf-8')
        print(error_body)
        sys.exit(1)

if __name__ == "__main__":
    main()
