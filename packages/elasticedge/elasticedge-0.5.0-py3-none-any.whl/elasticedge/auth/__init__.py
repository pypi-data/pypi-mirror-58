import dataclasses
import json
import os

from pathlib import Path


@dataclasses.dataclass
class Auth:
    FILE_PATH: str = dataclasses.field(
        default=os.path.join(Path.cwd(), "auth.json"), init=False
    )

    token: str
    backend: str

    @classmethod
    def load(cls) -> "Auth":
        with open(cls.FILE_PATH, "r") as f:
            contents = json.load(f)

            token = contents["token"]
            backend = contents["backend"]

        auth = cls(token=token, backend=backend)
        return auth

    @classmethod
    def write(cls, token: str, backend: str) -> None:
        data = {"token": token, "backend": backend}

        with open(cls.FILE_PATH, "w") as f:
            f.write(json.dumps(data))
