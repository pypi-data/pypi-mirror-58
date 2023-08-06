__author__ = "Luca Rebuffi"

from orangecontrib.xrayserver.util.xrayserver_util import HttpManager

APPLICATION = "/cgi/www_dbli.exe"

class ListUtility:
    @classmethod
    def get_list(cls, x0hdb=""):

        parameters = {}
        parameters.update({"x0hdb" : x0hdb})
        parameters.update({"textout" : "1" })
        parameters.update({"namesonly" : "1"})

        try:
            response = HttpManager.send_xray_server_request_GET(APPLICATION, parameters)

            list = response.split('\n')
            return [x.strip() for x in list[1:len(list)-1]]

        except Exception as e:
            return []


    @classmethod
    def get_help(cls, x0hdb=""):

        parameters = {}
        parameters.update({"x0hdb" : x0hdb})

        try:
            return HttpManager.send_xray_server_request_GET(APPLICATION, parameters)

        except Exception as e:
            return ""
