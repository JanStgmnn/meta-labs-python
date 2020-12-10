import urllib3
import json

"""
Meta-Labs SDK

SDK for MetaLabs API
"""

__version__ = "0.0.1"
__author__ = 'Jeffrey Annaraj'


def get_license(api_key, license_key):
    headers = {
        'Authorization': f'Basic {api_key}',
        'Content-Type': 'application/json'
    }

    http = urllib3.PoolManager()
    r = http.request('GET', f'https://api.metalabs.io/v2/licenses/{license_key}', headers=headers)

    return r.data.decode('utf-8')


def update_license(api_key, license_key, metadata):
    headers = {
        'Authorization': f'Basic {api_key}',
        'Content-Type': 'application/json',
    }

    body = json.dumps(metadata)

    http = urllib3.PoolManager()
    r = http.request(body=body, method='PATCH', url=f'https://api.metalabs.io/v2/licenses/{license_key}',
                     headers=headers)

    return r.data.decode('utf-8')