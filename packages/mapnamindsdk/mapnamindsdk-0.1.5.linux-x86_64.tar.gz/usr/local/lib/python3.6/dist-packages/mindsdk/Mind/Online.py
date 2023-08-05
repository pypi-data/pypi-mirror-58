import json
import urllib

from mindsdk.Mapper import Mapper as mapper
from mindsdk.WS import WS as WS
import mindsdk.Constants as Constants
import cherrypy
from threading import Thread

from mindsdk.Mind.Mind import Mind


class Online(Mind):

    def __init__(self):
        super(Online,self).__init__()

    @staticmethod
    def _startWS():
        cherrypy.quickstart(WS.MindSdkWebService)

    @staticmethod
    def startWS():
        Thread(target=Online._startWS).start()

    @staticmethod
    def callback():
        print("finished!")

    @staticmethod
    def set(key, value):
        WS.MindSdkWebService.set(key=key, value=value)

    @staticmethod
    def add(key, value):
        WS.MindSdkWebService.add(key=key, value=value)

    @staticmethod
    def getResult(key):
        return WS.MindSdkWebService.getResult(key)

    @staticmethod
    def getResultList(key):
        return WS.MindSdkWebService.getList(key)

    @staticmethod
    def getValue(signalNames,startDate,endDate,userId):

        Mind.validate(startDate)
        Mind.validate(endDate)

        # f = mapper.Mapper.getInstance()
        # signalIds = list(map(lambda x: int(f.SignalMapper[x]), signalNames))
        try:
            body = {"signalNames": signalNames,
                    "startTime": startDate,
                    "endTime": endDate,
                    "userId": userId
                    }

            targetUrl = "http://" + Constants.SDK_SERVER_IP + ":" + Constants.SDK_PORT + "/online/get"

            req = urllib.request.Request(targetUrl)
            req.add_header('Content-Type', 'application/json; charset=utf-8')

            json_data = json.dumps(body)
            jsonDataAsBytes = json_data.encode('utf-8')  # needs to be bytes
            req.add_header('Content-Length', len(jsonDataAsBytes))
            response = urllib.request.urlopen(req, jsonDataAsBytes)
            jsonResult = response.read()
            listResult = json.loads(jsonResult)
            print(listResult)
            return listResult

            # if ('message' in listResult):
            #
            #     return listResult;
            #
            # else:
            #
            #     resultJson = Mind.convertJsonToListOfDict(listResult, signalNames, signalIds)
            #     return resultJson
        except urllib.error.HTTPError as err:
            print("{}\nError Code:{}, URL:{}".format(err, err.code, err.filename))

        except KeyError as err:
            print("ERROR: Signal Name {} not found!\n".format(err))
        return None
        # super(Online, Online).getValue(signalNames)

    # def createSignal(signalName):
    #     # Create Signal with FALSE Historical Tag
    #     super(Online,Online).createSignal(signalName, False)


    def setValue(signalName, value, dateAndTime, userId):
        super(Online,Online).setValue(signalName, value, dateAndTime, userId)
