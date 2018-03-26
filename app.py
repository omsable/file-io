#!/usr/bin/env python

import os
import sys
import requests


def main(obj, expires=None):
    url = 'https://file.io'
    if expires:
        url = '%s?expires=%s' % (url, expires)

    if os.path.exists(obj):
        with open(obj, 'rb') as f:
            res = requests.post(url, files={'file': f})
    else:
        res = requests.post(
            url,
            files={'file': ('file', obj)}
        )

    try:
        res.raise_for_status()
    except:
        sys.stderr.write(res.text)
        raise
    else:
        return res.text


if __name__ == '__main__':
    sys.stdout.write(main(*sys.argv[1:]))
