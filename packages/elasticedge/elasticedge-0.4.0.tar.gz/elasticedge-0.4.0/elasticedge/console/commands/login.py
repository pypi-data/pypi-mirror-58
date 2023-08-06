import os
import json

from pathlib import Path
from cleo import Command

from ...auth import Auth


class LoginCommand(Command):
    """
    Login

    login
        {token : Token to connect}
        {backend=https://elasticedge.dev/ : The service to connect to}
    """

    def handle(self):
        token = self.argument("token")
        backend = self.argument("backend")

        Auth.write(token, backend)

        self.line(f"Login authentication saved", "info")
