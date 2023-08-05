import logging

from prefect.utilities.tasks import defaults_from_attrs
from .query import Query


class QueryTimeseries(Query):
    """
    Basic
    """
    def __init__(self, key, timeseries=None, url=None, order=None):
        super().__init__(key, url)
        self.name = "Timeseries"
        self.url = url
        self.key = "apiKey {}".format(key)
        self.timeseries = timeseries
        self.log_prefix = self.build_log_prefix()

    def prep(self, url: str, ca_id: str, timeseries: str):
        if "error" in ca_id:
            return ca_id
        new_url = "{url}/timeseries/{timeseries}/{ca_id}" \
            .format(url=url, ca_id=ca_id, timeseries=timeseries, skip=self.skip, limit=self.limit)
        return new_url

    @defaults_from_attrs('url', 'timeseries')
    def run(self, data, timeseries=None, url=None):
        full_url = self.prep(url, data, timeseries)
        response = self.query(full_url)
        result = self.process(response)
        return result


class GetTimeseriesData(Query):
    def __init__(self, key, timeseries=None, url=None, order=None):
        super().__init__(key, url)
        self.name = "Timeseries"
        self.url = url
        self.key = "apiKey {}".format(key)
        self.timeseries = timeseries
        self.order = order
        self.skip = 0
        self.limit = 500
        self.log_prefix = self.build_log_prefix()

    def prep(self, url: str, ca_id: str, timeseries: str):
        if "error" in ca_id:
            return ca_id
        new_url = "{url}/timeseries/{timeseries}/{ca_id}?skip={skip}&limit={limit}"\
            .format(url=url, ca_id=ca_id, timeseries=timeseries, skip=self.skip, limit=self.limit)
        if self.order:
            new_url += "order={}".format(self.order)
        logging.debug("url is {}".format(new_url))
        self.skip += self.limit # increments after call
        return new_url

    @staticmethod
    def join(final, response):
        if "error" in response:
            return response
        if "data" in response:
            final["data"] = final["data"] + response["data"]
        return final

    def done(self, final, result):
        # make data dict
        if not final["data"]:
            final = result
        else:
            final = self.join(final, result)
        # stop because bad response
        if "error" in result:
            return final, True
        # logic
        if self.limit >= result["totalCount"]:
            return final, True
        return final, False

    @defaults_from_attrs('url', 'timeseries')
    def run(self, data, timeseries=None, url=None):
        """
        Repeats API call to get all data via paging for given timeseries type & company id
        :param data:
        :param timeseries:
        :param url:
        :return:
        """
        final = {"data": []}
        while True:  # runs until no more data
            full_url = self.prep(url, data, timeseries)
            response = self.query(full_url)
            result = self.process(response)
            final, done = self.done(final, result)
            if done:
                break
        return final  # will return error or final results


class GetAllTimeseries(Query):
    def __init__(self, key, url=None):
        super().__init__(key, url)
        self.name = "TimeseriesAllSignals"
        self.url = url
        self.key = "apiKey {}".format(key)
        self.log_prefix = self.build_log_prefix()

    @staticmethod
    def prep(url: str):
        return "{url}/timeseries".format(url=url)

    @staticmethod
    def post_process(result):
        if "data" in result:
            return result["data"]
        return []

    @defaults_from_attrs('url')
    def run(self, url=None):
        full_url = self.prep(url)
        response = self.query(full_url)
        result = self.process(response)
        timeseries = self.post_process(result)
        return timeseries


class SearchCompany(Query):
    def __init__(self, key, url=None):
        super().__init__(key, url)
        self.name = "TimeseriesCompany"
        self.url = url
        self.key = "apiKey {}".format(key)
        self.log_prefix = self.build_log_prefix()

    def prep(self, url: str, timeseries_id: str):
        if "error" in timeseries_id:
            return timeseries_id
        return "{url}/companies?name={timeseries_id}".format(url=url, timeseries_id=timeseries_id)

    @defaults_from_attrs('url')
    def run(self, data, url=None):
        full_url = self.prep(url, data)
        response = self.query(full_url)
        result = self.process(response)
        return result
