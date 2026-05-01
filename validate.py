import re

def valid_username(str):
    str = str.strip()
    pattern = r'^[A-Za-z0-9\-]{3,20}$'
    if not re.fullmatch(pattern, str):
        raise ValidationError(f"Invalid username '{str}': must be 3-20 letters, digits, or dashes")
    return str
 
def valid_email(str):
    str = str.strip()
    pattern = r'^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$'
    if not re.fullmatch(pattern, str):
        raise ValidationError(f"Invalid email '{str}': must be a valid email address")
    return str
 
def valid_filename(str):
    str = str.strip()
    pattern = r'^[A-Za-z0-9._\-]{1,255}$'
    if not re.fullmatch(pattern, str):
        raise ValidationError(f"Invalid filename '{str}': only letters, digits, dots, underscores, and dashes allowed")
    if str in ('.', '..'):
        raise ValidationError(f"Invalid filename '{str}': . and .. are not allowed")
    return str
 
def valid_int(str, min, max):
    str = str.strip()
    pattern = r'^-?[0-9]+$'
    if not re.fullmatch(pattern, str):
        raise ValidationError(f"Invalid integer '{str}': must be a whole number")
    n = int(str)
    if n < min or n > max:
        raise ValidationError(f"Invalid integer {n}: must be between {min} and {max} (inclusive)")
    return n
 
def valid_ipv4(str):
    str = str.strip()
    pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    m = re.fullmatch(pattern, str)
    if not m:
        raise ValidationError(f"Invalid IPv4 address '{str}': must be four dot-separated octets (0-255)")
    for sect in m.groups():
        if int(sect) > 255:
            raise ValidationError(f"Invalid IPv4 address '{str}': each section must be 0-255")
    return str
 
def valid_url(str):
    str = str.strip()
    ipv4 = r'(?:\d{1,3}\.){3}\d{1,3}'
    hostname = r'[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*'
    pattern = rf'^https?://(?:{ipv4}|{hostname})(?::\d{{1,5}})?(?:/[^\s]*)?$'
    if not re.fullmatch(pattern, str):
        raise ValidationError(f"Invalid URL '{str}': must be an HTTP/HTTPS URL with a valid hostname or IPv4 address")
    return str
 
if __name__ == '__main__':
    main()
