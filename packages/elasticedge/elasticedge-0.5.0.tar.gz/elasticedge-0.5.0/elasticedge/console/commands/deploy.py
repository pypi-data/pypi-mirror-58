import time
import os
import yaml

from pathlib import Path
from cleo import Command

from ...api import deploy, healthcheck
from ...api.exceptions import GraphQLError


class DeployCommand(Command):
    """
    Deploy

    deploy
        {spec=elasticedge.yaml : The spec file with information about what to deploy}
    """

    def handle(self):
        spec = self.argument("spec")
        spec_file = os.path.join(Path.cwd(), spec)

        if os.path.isdir(spec_file):
            spec_file = os.path.join(spec_file, "elasticedge.yaml")

        if not os.path.exists(spec_file):
            self.line_error(f"Spec file {spec_file} not found!", "error")
            return

        with open(spec_file) as f:
            configuration = yaml.load(f, Loader=yaml.FullLoader)

        configuration["project"]["env"] = self.resolve_environment(
            configuration["project"]["env"]
        )

        for service in configuration["services"]:
            service_env = service["env"]
            service["env"] = self.resolve_environment(service_env)

        project_id = configuration["project"]["id"]
        name = configuration["project"]["name"]

        self.line(f"Deploying configuration to {name} ({project_id})")

        try:
            deploy(configuration)
        except GraphQLError as e:
            if e.response.status_code >= 500:
                self.line_error(
                    "Deployer answer was a 5xx. Checking if the deployment completed with an healthcheck after 3 seconds."
                )

                time.sleep(3)

                if healthcheck(configuration):
                    self.line_error(
                        f"The service is still up, but we had a few errors:", "error"
                    )
                else:
                    self.line_error("Healthcheck failed.")
            else:
                self.line_error(f"Unable to deploy new configuration", "error")

            for error in e.errors:
                self.line_error(f"[GraphQL Error] {error}", "error")

            exit(1)

        self.line(f"New configuration uploaded and deploy requested!", "info")

    def resolve_environment(self, envs):
        if not envs:
            return []

        new_env = []

        for variable in envs:
            new_env.append({"name": variable, "value": os.getenv(variable, "")})

        return new_env
