from prefect.utilities.tasks import defaults_from_attrs
from .query import Query


class QueryRankingsCompany(Query):
    def __init__(self, key, url=None):
        super().__init__(key, url)
        self.name = "Rankings"
        self.url = url
        self.key = key
        self.log_prefix = self.build_log_prefix()

    def prep(self, url: str, rankings_id: str):
        if "error" in rankings_id:
            return rankings_id
        return "{}/companies?company={}".format(url, rankings_id)

    @defaults_from_attrs('url')
    def run(self, data, url=None):
        full_url = self.prep(url, data)
        response = self.query(full_url)
        result = self.process(response)
        return result
