from multiprocessing.pool import ThreadPool
from circleci import BuildFetcher


class MultiCircleBuildFetcher:
    def __init__(self, projects, token):
        self.projects = projects
        self.token = token
        self.results = {}
        self.pool = None

    def fetch_single_build(self, project):
        return BuildFetcher(project, self.token, 1).builds()[0]

    def kickoff(self):
        self.results = {}
        self.pool = ThreadPool(20)
        for project in self.projects:
            self.pool.apply_async(self.fetch_single_build, args=(project,), callback=self.on_complete)

    def on_complete(self, build):
        self.results[build.project] = build

    def is_done(self):
        return len(self.results) == len(self.projects)

    def builds(self):
        self.pool.close()
        self.pool.join()
        return self.results
