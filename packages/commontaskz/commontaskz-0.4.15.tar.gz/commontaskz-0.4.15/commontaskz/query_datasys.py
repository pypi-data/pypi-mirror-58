from prefect.utilities.tasks import defaults_from_attrs
from .query import Query


class QueryDatasysCompany(Query):
    def __init__(self, key, url=None):
        super().__init__(key, url)
        self.name = "Datasys"
        self.url = url
        self.key = key
        self.log_prefix = self.build_log_prefix()

    def prep(self, url: str, datasys_id: str):
        if "error" in datasys_id:
            return datasys_id
        return "{}/repository/company/{}?trace=false".format(url, datasys_id)

    @defaults_from_attrs('url')
    def run(self, data, url=None):
        full_url = self.prep(url, data)
        response = self.query(full_url)
        result = self.process(response)
        return result
