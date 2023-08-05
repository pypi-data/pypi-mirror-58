import urllib.request
import urllib.parse
import json

import mindsdk.Constants as Constants

class Mapper:
    __instance=None

    SignalMapper=None

    @staticmethod
    def getInstance():

        if Mapper.__instance==None:
            Mapper()
        return Mapper.__instance


    @staticmethod
    def getMapper():
        try:
            url = 'http://'+Constants.SIGNALSERVICE_SERVER_IP+':'+Constants.SIGNALSERVICE_PORT+'/getmapper'
            f = urllib.request.urlopen(url)
            jsonResponse = f.read().decode('utf-8')

            dictResponse = json.loads(jsonResponse)
            dictResult = {}
            for signal in dictResponse:
                if dictResponse[signal]['plantId']==3:
                    dictResult[dictResponse[signal]['signalName']] = signal
                # if dictResponse[signal]['signalClass'] == 4:
                #     dictResult[dictResponse[signal]['signalName']] = signal


            # pprint(response)
            return dictResult
        except urllib.error.HTTPError as err:
            print("{}\nError Code:{}, URL:{}".format(err, err.code, err.filename))
            return None

    def __init__(self):
        """ Virtually private constructor. """
        if Mapper.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Mapper.SignalMapper=Mapper.getMapper()
            Mapper.__instance = self



