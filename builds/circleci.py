import requests
from utils import colors


class BuildFetcher:
    api_url = "https://circleci.com/api/v1"

    def __init__(self, project, token, num_builds):
        self.project = project
        self.num_builds = num_builds
        self.project_endpoint = "%(url)s/project/%(project)s" % {"url": self.api_url, "project": project}
        self.token = token

    def builds(self):
        build_list = requests.get(
            self.project_endpoint,
            params={"circle-token": self.token, "limit": self.num_builds},
            headers={"Accept": "application/json"}
        ).json()

        return map(lambda build: Build(build.get("status", "unknown"), self.project), build_list)


class Build:
    color_map = {
        "failed": colors.red,
        "fixed": colors.green,
        "success": colors.green,
        "running": colors.yellow,
        "not_run": colors.blue,
        "canceled": colors.blue,
        "unknown": colors.gray,
    }

    def __init__(self, status, project):
        self.status = status
        self.project = project

    def to_color(self):
        return self.color_map.get(self.status, self.color_map["not_run"])
