from .graphql import request


def deploy(configuration):
    return request(
        """
    mutation($configuration: ConfigurationInput!) {
        deploy(configuration: $configuration)
    }
    """,
        {"configuration": configuration},
    )
