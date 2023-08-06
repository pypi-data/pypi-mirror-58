from .graphql import request


def deploy(configuration):
    response = request(
        """
    mutation($configuration: ConfigurationInput!) {
        deploy(configuration: $configuration)
    }
    """,
        {"configuration": configuration},
    )

    json = response.json()
    return json["data"]["deploy"]
