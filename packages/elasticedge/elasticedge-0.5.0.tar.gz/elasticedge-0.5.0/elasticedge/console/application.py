from cleo import Application

from .commands import DeployCommand, LoginCommand

application = Application()
application.add(DeployCommand())
application.add(LoginCommand())


if __name__ == "main":
    application.run()
