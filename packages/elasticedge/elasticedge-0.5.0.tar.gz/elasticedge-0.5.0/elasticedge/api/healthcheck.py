import time

from .graphql import request

import requests


def healthcheck(configuration):
    response = requests.get(f'https://{configuration["project"]["domain"]}')
    return response.status_code == 200
