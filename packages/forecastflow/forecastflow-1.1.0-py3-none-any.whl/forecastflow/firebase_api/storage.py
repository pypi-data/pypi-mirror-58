from typing import IO, Union
from urllib.parse import quote
from forecastflow.firebase_api.exceptions import APIFailed, NotFound, PermissionDenied

import requests

from forecastflow import config

_api_base_url = "https://firebasestorage.googleapis.com/v0/b/"


def download(path: str, file: IO, id_token: str):
    """
    Download object at <path> on Firebase Storage and write it to <file>.

    Args:
        path:
            Path on Firebase Storage

        file:
            IO object

        id_token:
            Firebase Auth ID token

    Raises:
        PermissionDenied:

        NotFound:

        APIFailed:
            Other Firebase API error
    """
    url = get_url(path)
    res = requests.get(url, stream=True,
                       headers={'authorization': f"Firebase {id_token}"})

    if res.status_code != 200:
        if res.status_code == 403:
            raise PermissionDenied(res.text)
        elif res.status_code == 404:
            raise NotFound(res.text)
        else:
            raise APIFailed(res.text)

    file.write(res.content)


def get_url(path):
    if path.startswith('/'):
        path = path[1:]
    api_url = _api_base_url + config.firebase['storageBucket']
    return "{0}/o/{1}?alt=media".format(api_url, quote(path, safe=''))


def upload(file: Union[IO, str], path: str, id_token):
    """
    Upload <file> to <path> on Firebase Storage

    Args:
        file:
            IO object or path to file

        path:
            Path on Firebase Storage

        id_token:
            Firebase Auth ID token

    Raises:
        PermissionDenied:

        APIFailed:
            Other Firebase API error
    """
    if path.startswith('/'):
        path = path[1:]
    if isinstance(file, str):
        file_object = open(file, 'rb')
    else:
        file_object = file
    request_ref = _api_base_url + config.firebase['storageBucket'] + "/o?name={0}".format(path)
    headers = {"Authorization": "Firebase " + id_token}
    res = requests.post(request_ref, headers=headers, data=file_object)
    if res.status_code != 200:
        if res.status_code == 403:
            raise PermissionDenied(res.text)
        else:
            raise APIFailed(res.text)
    return res.json()
