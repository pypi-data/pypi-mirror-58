import json
import urllib
import datetime
import pandas as pd
from mindsdk.Mapper import Mapper as mapper
from mindsdk.WS import WS as WS
import mindsdk.Constants as Constants
import cherrypy
from threading import Thread

class Mind(object):

    def __init__(self):
        pass

    def removeSignal(signalName, userId):

        try:
            body = {"signalName": signalName,
                    "userId": userId
                    }

            targetUrl = "http://" + Constants.SDK_SERVER_IP + ":" + Constants.SDK_PORT + "/remove"

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

        except urllib.error.HTTPError as err:
            print("{}\nError Code:{}, URL:{}".format(err, err.code, err.filename))

        except KeyError as err:
            print("ERROR: Signal Name {} not found!\n".format(err))
        return None



    def createSignal(signalName, signalDescription,unitMeasurment, userId):

        try:
            body = {"signalName": signalName,
                    "description": signalDescription,
                    "unitMeasurment": unitMeasurment,
                    "userId": userId
                    }

            targetUrl = "http://" + Constants.SDK_SERVER_IP + ":" + Constants.SDK_PORT + "/create"

            req = urllib.request.Request(targetUrl)
            req.add_header('Content-Type', 'application/json; charset=utf-8')

            json_data = json.dumps(body)
            jsonDataAsBytes = json_data.encode('utf-8')  # needs to be bytes
            req.add_header('Content-Length', len(jsonDataAsBytes))
            response = urllib.request.urlopen(req, jsonDataAsBytes)
            jsonResult = response.read()
            listResult = json.loads(jsonResult)

            if listResult['messageCode']=='0000':
                return True
            else:
                return False




        except urllib.error.HTTPError as err:
            print("{}\nError Code:{}, URL:{}".format(err, err.code, err.filename))

        except KeyError as err:
            print("ERROR: Signal Name {} not found!\n".format(err))
        return None

        # TODO Check Signal duplication with performance signals


    def setValue(signalName, value, dateAndTime, userId):
        '''
        Insert data into ONLINE table
        :param signalName:
        :param value:
        :param dateAndTime:
        :param userId:
        :return:
        '''
        pass

    @staticmethod
    def getValue(signalNames):
        '''
        Get value from ONLINE table
        :return:
        '''
        try:

            f = mapper.Mapper.getInstance()

            # Get signalId for given signalName from the Mapper
            signalID = int(f.SignalMapper[signalNames])

            # Request Body
            body = {'ids': [signalID], 'type': "TIMESERIES"}

            # Create and Send HTTP request
            targetUrl = "http://" + Constants.DATASERVICE_SERVER_IP + ":" + Constants.DATASERVICE_PORT + "/online/get"
            req = urllib.request.Request(targetUrl)
            req.add_header('Content-Type', 'application/json; charset=utf-8')

            jsonData = json.dumps(body)
            jsonDataAsBytes = jsonData.encode('utf-8')  # needs to be bytes
            req.add_header('Content-Length', len(jsonDataAsBytes))

            response = urllib.request.urlopen(req, jsonDataAsBytes)

            # get jsonResult from byte strings
            jsonResult = response.read()

            # Convert Json to List/Dict composition
            dictResult = json.loads(jsonResult)[0]

            return dictResult
        except urllib.error.HTTPError as err:
            print("{}\nError Code:{}, URL:{}".format(err, err.code, err.filename))
        except KeyError as err:
            print("ERROR: Signal Name {} not found!\n".format(err))
        return None

    @staticmethod
    def mapHistorian2DataFrame(x, signalNames):
        '''
        Map function for converting each row of the given list (x) to dictionary
        :param x: A single row of list
        :param signalNames: list of signal_names for columns title
        :return: Input list rows in dict format
        '''

        # Create an empty row
        dictCurrentRow = {}

        # add first column of DataFrame table and its value
        dictCurrentRow.update({'time': x['time']})

        # Create rest of columns using list of signal_names and their values
        valueColumns = {signalNames[i]: x['values'][i] for i in range(0, len(signalNames))}

        # Add rest of the columns and values to the current row
        dictCurrentRow.update(valueColumns)

        # Return the row
        return dictCurrentRow

    @staticmethod
    def convertJsonToDataFrame(jsonResponse, signalNames):
        """
        Converts given json_response to pandas DataFrame
        :param jsonResponse: Query result in json_response format
        :param signal_names: List of signal names in query to set as columns name of DataFrame
        :return: DataFrame object of json_response
        """

        # Convert JSON to LIST
        listResult = json.loads(jsonResponse)

        # list_result->dictionary->DataFrame
        dataFrameResult = pd.DataFrame(map(lambda x: Mind.mapHistorian2DataFrame(x,signalNames), listResult))

        return dataFrameResult


    def convertJsonToListOfDict(listResult,signalNames,signalIds) :
        ii = 0
        totaldict = {}
        for i in listResult:
            dict = i
            mediumlist = dict.get(str(signalIds[ii]))
            listofvaluetimetotal = []
            for l in mediumlist:

                time = l.get('TIME')
                value = l.get('VALUE')
                listofvaluetime = [time, value]
                listofvaluetimetotal.append(listofvaluetime)
            totaldict[signalNames[ii]] = listofvaluetimetotal
            ii = ii + 1

        print(totaldict)
        return totaldict

    def validate(date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y/%m/%d-%H:%M:%S')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY/MM/DD-HH:mm:SS")