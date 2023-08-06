class GraphQLError(ValueError):
    def __init__(self, response):
        self.response = response

        try:
            body = response.json()
            self.errors = [error["message"] for error in body["errors"]]
        except:
            self.errors = ["Internal error"]
