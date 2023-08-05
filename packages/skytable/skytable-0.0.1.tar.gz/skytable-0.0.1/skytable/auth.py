from __future__ import absolute_import
import os
import requests


def SkytableAuth(api_key=None):

    try:
        api_key = api_key or os.environ["SKYTABLE_API_KEY"]
    except KeyError:
        raise KeyError(
            "Api Key not found. Pass api_key as a kwarg \
             or set an env var SKYTABLE_API_KEY with your mongodb `user:pass` string"
        )
    return api_key
