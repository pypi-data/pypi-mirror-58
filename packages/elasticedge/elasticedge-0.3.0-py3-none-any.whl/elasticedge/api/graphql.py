import requests

from ..auth import Auth

from .exceptions import GraphQLError


def request(query, variables={}):
    auth = Auth.load()

    response = requests.post(
        f"{auth.backend}graphql/",
        json={"query": query.strip(), "variables": variables},
        headers={"Authorization": auth.token},
    )

    if response.status_code == 400:
        raise GraphQLError(response)

    return response
