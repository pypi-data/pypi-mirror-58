import json
import urllib


from mindsdk.Mapper import Mapper as mapper
from mindsdk.WS import WS as WS
import mindsdk.Constants as Constants
import pandas as pd
import cherrypy
from threading import Thread

from mindsdk.Mind.Mind import Mind


class Offline(Mind):


    def getUdsValue(signalNames, startDate, endDate,userId):

        Offline.validate(startDate)
        Offline.validate(endDate)

        # f = mapper.Mapper.getInstance()
        # signalIds = list(map(lambda x: int(f.SignalMapper[x]), signalNames))
        try:
            body = {"signalNames": signalNames,
                    "startDate": startDate,
                    "endDate": endDate,
                    "userId": userId
                    }

            targetUrl = "http://" + Constants.SDK_SERVER_IP + ":" + Constants.SDK_PORT + "/offline/getUsd"

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




        except urllib.error.HTTPError as err:
            print("{}\nError Code:{}, URL:{}".format(err, err.code, err.filename))

        except KeyError as err:
            print("ERROR: Signal Name {} not found!\n".format(err))
        return None


    def getValue(signalNames, startDate, endDate, aggregation, interval, pageNumber=1, pageSize=1000):
        try:
            Offline.validate(startDate)
            Offline.validate(endDate)
            f = mapper.Mapper.getInstance()

            # Get signalId for given signalName from the Mapper
            signalIDs = list(map(lambda x: int(f.SignalMapper[x]), signalNames))

            units= list(map(lambda x: int(x[0:2]), signalNames))

            # Request Body
            body = {"ids": signalIDs,
                    "units": units,
                    "from_date": startDate,
                    "to_date": endDate,
                    "agg": aggregation,
                    "interval": interval,
                    "page_size": pageSize,
                    "page_number": pageNumber
                    }

            targetUrl = "http://" + Constants.SDK_SERVER_IP + ":" + Constants.SDK_PORT + "/offline/get"

            req = urllib.request.Request(targetUrl)
            req.add_header('Content-Type', 'application/json; charset=utf-8')

            json_data = json.dumps(body)
            jsonDataAsBytes = json_data.encode('utf-8')  # needs to be bytes
            req.add_header('Content-Length', len(jsonDataAsBytes))

            response = urllib.request.urlopen(req, jsonDataAsBytes)

            jsonResult = response.read()

            # Convert LIST to pandas DataFrame object
            df_result = Offline.convertJsonToDataFrame(jsonResult, signalNames)

            return df_result
        except urllib.error.HTTPError as err:
            print("{}\nError Code:{}, URL:{}".format(err, err.code, err.filename))
        except KeyError as err:
            print("ERROR: Signal Name {} not found!\n".format(err))
        return None


    def getLastValue(signalNames):
        return super(Offline, Offline).getValue(signalNames)

    def setValue(signalName, value, dateAndTime, userId):

        if dateAndTime.lower() != 'now'.lower():
            Offline.validate(dateAndTime)


        # f = mapper.Mapper.getInstance()

        # signalId = f.SignalMapper[signalName]
        # Request Body
        body = {"signalName": signalName,
                "dateAndTime": dateAndTime,
                "value":value,
                "userId":userId

                }

        targetUrl = "http://" + Constants.SDK_SERVER_IP + ":" + Constants.SDK_PORT + "/offline/set"

        req = urllib.request.Request(targetUrl)
        req.add_header('Content-Type', 'application/json; charset=utf-8')

        json_data = json.dumps(body)
        jsonDataAsBytes = json_data.encode('utf-8')  # needs to be bytes
        req.add_header('Content-Length', len(jsonDataAsBytes))

        response = urllib.request.urlopen(req, jsonDataAsBytes)

        jsonResult = response.read()
        listResult = json.loads(jsonResult)

        if listResult['messageCode'] == '0000':
            return True
        else:
            return False

        return jsonResult
