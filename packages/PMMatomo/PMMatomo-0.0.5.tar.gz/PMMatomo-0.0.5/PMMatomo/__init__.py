from typing import *
import json
import requests
import datetime
import logging
from deprecated import deprecated


class MatomoReportPeriod:
    day = "day"
    week = "week"
    month = "month"
    year = "year"
    spesificRange = "range"


class Matomo:
    def __init__(self, url, token, siteId):
        self._apiUrl = url
        self._token = token
        self._siteId = siteId
        self._default_filterLimit = 100
        self._filterLimit = self._default_filterLimit
        self._period: MatomoReportPeriod = MatomoReportPeriod.day
        self._date = "2018-11-3"

    def _baseUrl(self):
        period = self._period
        # turn on or of the filter
        filter_limit = "-1" if self._filterLimit <= 0 else self._filterLimit
        _url = self._apiUrl+"/?module=API&idSite=" + \
            str(self._siteId)+"&format=json&token_auth="+self._token + \
            "&filter_limit="+str(filter_limit)+"&period=" + \
            period+"&date="+self._date
        return _url

    def _call_api_json(self, url) -> str:
        result = requests.get(url)
        if result.status_code == 200:
            return result.text
        logging.debug(
            f"This result of the Matomo api might contain some hint as to why it failed: {result.text}")
        result.raise_for_status()

    def _call_api(self, url) -> List:
        jsonResponse = self._call_api_json(url)
        if jsonResponse:
            return json.JSONDecoder().decode(jsonResponse)
        return None

    def setReportPeriod(self, period: MatomoReportPeriod):
        self._period = period

    @deprecated(version='0.0.2', reason="Use setReportDateFromDatetime() instead.")
    def setReportDateFromString(self, date: str):
        """A date in the format YYYY-MM-DD."""
        self._date = date

    def setReportDateFromDatetime(self, date: datetime.datetime):
        self._date = date.strftime("%Y-%m-%d")

    def enableFilterLimit(self, enabled=False):
        if enabled:
            if self._filterLimit > 0:
                # make sure the filter has not been set before calling enableFilterLimit()
                self._filterLimit = self._default_filterLimit
        else:
            self._filterLimit = False

    def setFilterLimit(self, limit):
        self._filterLimit = limit

    def getTestReport(self):
        """thid function can be used to test if reports are working"""
        url = self._baseUrl()
        url += "&method=API.getProcessedReport&apiModule=UserCountry&apiAction=getCountry"
        return self._call_api(url)

    def genReport(self, method, apiModule=None, apiAction=None):
        url = self._baseUrl()
        #url += "&method="+method+"&apiModule="+apiModule+"&apiAction="+apiAction
        url += "&method="+method if method else ""
        url += "&apiModule"+apiModule if apiModule else ""
        url += "&apiAction="+apiAction if apiAction else ""
        return self._call_api(url)

    def genReportLiveGetLastVisistsDetails(self):
        return self.genReport(method="Live.getLastVisitsDetails")

    def genReportLiveGetVisitorProfile(self):
        return self.genReport(method="Live.getVisitorProfile")

    def genReportLiveGetMostRecentVisitorId(self):
        return self.genReport(method="Live.getMostRecentVisitorId")
