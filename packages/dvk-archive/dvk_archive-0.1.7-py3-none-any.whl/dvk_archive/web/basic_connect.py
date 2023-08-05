from io import BytesIO
from bs4 import BeautifulSoup
from requests import exceptions
from requests import Session
from pathlib import Path
from shutil import copyfileobj
from urllib.error import HTTPError
from dvk_archive.processing.string_processing import extend_int

from dvk_archive.processing.string_processing import get_extension


def get_headers() -> dict:
    headers = {
        "User-Agent":
        "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
        "Accept-Language":
        "en-US,en;q=0.5"}
    return headers


def basic_connect(url: str = None) -> BeautifulSoup:
    """
    Connects to a URL and returns a BeautifulSoup object.
    Incapable of working with JavaScript.

    Parameters:
        url (str): URL to retrieve

    Returns:
        BeautifulSoup: BeautifulSoup object of the url page
    """
    if url is None or url == "":
        return None
    session = Session()
    headers = get_headers()
    try:
        request = session.get(url, headers=headers)
        bs = BeautifulSoup(request.text, features="lxml")
        return bs
    except (exceptions.ConnectionError,
            exceptions.MissingSchema,
            ConnectionResetError):
        return None
    return None


def download(url: str = None, filename: str = None) -> dict:
    """
    Downloads a file from a given url to a given file path.

    Parameters:
        url (str): URL from which to download
        filename (str): File path to save to
    """
    if (url is not None
            and not url == ""
            and filename is not None
            and not filename == ""):
        file = Path(filename)
        if file.exists():
            extension = get_extension(filename)
            base = filename[0:len(filename) - len(extension)]
            num = 1
            while file.exists():
                file = Path(base + "(" + str(num) + ")" + extension)
                num = num + 1
        # SAVE FILE
        try:
            session = Session()
            headers = get_headers()
            response = session.get(url, headers=headers)
            byte_obj = BytesIO(response.content)
            byte_obj.seek(0)
            with open(str(file.absolute()), "wb") as f:
                copyfileobj(byte_obj, f)
            return response.headers
        except (HTTPError,
                exceptions.ConnectionError,
                exceptions.MissingSchema,
                ConnectionResetError):
            print("Failed to download:" + url)
    return dict()


def get_last_modified(headers: dict = None) -> str:
    """
    Returns the time a webpage was last formatted from its request headers.

    Parameters:
        headers (dict): HTML request headers

    Returns:
        str: Last formatted date and time in DVK format
    """
    if headers is None:
        return ""
    try:
        modified = headers["Last-Modified"]
    except KeyError:
        return ""
    try:
        day = int(modified[5:7])
        month_str = modified[8:11].lower()
        year = int(modified[12:16])
        hour = int(modified[17:19])
        minute = int(modified[20:22])
        # GET MONTH
        months = [
            "jan", "feb", "mar", "apr", "may", "jun",
            "jul", "aug", "sep", "oct", "nov", "dec"]
        month = 0
        while month < 12:
            if month_str == months[month]:
                break
            month += 1
        month += 1
        if month > 12:
            return ""
        time = extend_int(year, 4) + "/" + extend_int(month, 2) + "/"
        time = time + extend_int(day, 2) + "|" + extend_int(hour, 2)
        time = time + ":" + extend_int(minute, 2)
        return time
    except ValueError:
        return ""
