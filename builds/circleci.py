import requests
from utils import colors


class CircleCiBuildFetcher():
    api_url = "https://circleci.com/api/v1"

    def __init__(self, project, token):
        self.project_endpoint = "%(url)s/project/%(project)s" % {"url": self.api_url, "project": project}
        self.token = token

    def builds(self):
        build_list = requests.get(
            self.project_endpoint,
            params={"circle-token": self.token, "limit": 5},
            headers={"Accept": "application/json"}
        ).json()

        return map(lambda build: Build(build["status"]), build_list)


class Build:
    color_map = {
        "failed": colors.red,
        "fixed": colors.green,
        "success": colors.green,
        "running": colors.yellow,
        "not_run": colors.black
    }

    def __init__(self, status):
        self.status = status

    def to_color(self):
        return self.color_map.get(self.status, self.color_map["not_run"])