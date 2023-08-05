# TODO:
# -do all technical indicators
# -add functionality to add extra columns to the dataframe if you want
# -add functionality to precompute some values
# -change saved dl fileName to be more specific to the data eg AAPL-Daily-2018-2019
# -make display() print() compatible
import sys
import pandas as pd
import numpy as np
import datetime as dt
import warnings
import pickle
import os
import pathos.multiprocessing as mp

class dataloader:
    # Checks some things:
    # -if the source of data is given and is supported
    # -if the instrument is given
    # Then calls the required functions to lod the data from the relevant sources
    def __init__(self, source=None, apiKey=None, dataType=None, instrument=None, fileName=None, verbose=1):
        if(verbose>0):
            print("Data loading")
        if(source==None):
            raise ValueError("dataloader requires a source.")
        elif(type(source)!=str):
            raise ValueError("dataloader requires source input to be a string")
        elif(source!="local" and source!="alphavantage" and source!="preloaded"):
            raise ValueError("Invalid source for dataloader. Use local, alphavantage or preloaded instead.")
        elif(instrument==None):
            raise ValueError("dataloader requires an instrument.")
        elif(dataType==None):
            raise ValueError("dataloader requires a dataType.")
        elif(type(dataType)!=str):
            raise ValueError("dataloader requires dataType input to be a string")
        elif(type(instrument)!=str):
            raise ValueError("dataloader requires instrument input to be a string")
        self.__instrument = instrument
        self.__dataType = dataType
        self.__source = source
        self.__precompute = []
        self.__verbose =  verbose
        if(source=='local'):
            self.__load_LOCAL(fileName)
        if(source=="alphavantage"):
            self.__load_ALPHAVANTAGE(apiKey, dataType, instrument)
        if(source=="preloaded"):
            self.__load()
        if(verbose>0):
            print("Loading done")

    # Function role: Loads data from alphavantage api
    # Checks some things:
    # -Checks that an api key is given
    # -checks that a dataType is given
    # -checks that an instrument is given
    # Then it checks if the dataType is a correct one and converts it to a string that the alphavantage api understands
    # Then loads the data from the api
    # Then sorts it and stores it in self.data
    def __load_ALPHAVANTAGE(self, apiKey=None, dataType=None, instrument=None):
        if(apiKey==None):
            raise ValueError("dataloader requires an apiKey when using alphavantage.")
        elif(type(apiKey)!=str):
            raise ValueError("dataloader requires apiKey to be a string.")
        alphavantageDataType = None
        if(dataType=="intraday"):
            alphavantageDataType = "TIME_SERIES_INTRADAY"
        if(dataType=="daily"):
            alphavantageDataType = "TIME_SERIES_DAILY"
        if(dataType=="weekly"):
            alphavantageDataType = "TIME_SERIES_WEEKLY"
        if(dataType=="monthly"):
            alphavantageDataType = "TIME_SERIES_MONTHLY"
        if(alphavantageDataType==None):
            raise ValueError("Invalid dataType. Use intraday, daily, weekly or monthly.")
        data = pd.read_csv('https://www.alphavantage.co/query?function='+alphavantageDataType+'&outputsize=full&symbol='+instrument+'&interval=1min&apikey='+apiKey+'&datatype=csv')
        if(data.columns.any()=="{"):
            raise ValueError("Alphvantage has responded with an error: " + data["{"][0])
        data = data.rename(columns={"timestamp":"Date","open":"Open","high":"High","low":"Low","close":"Close","volume":"Volume"})
        warnings.filterwarnings('ignore', '.*.*',)
        for x in range(0,data.shape[0]):
            data["Date"][x] = pd.to_datetime(data.iloc[x]["Date"], format='%Y-%m-%d')
        self.data= data
        for index in range(0,self.data.shape[0]-2):
            if(self.data["Date"][index].day==self.data["Date"][index+1].day):
                raise ValueError("The data comtains two sets of data for a single day")

    #Function role: loads data from local Files
    # Checks some things:
    # -fileName is given
    # -file exists
    # Then loads the data into a dataframe and sorts it out while checking all relevant columns are given
    # Then stores the data in self.data
    def __load_LOCAL(self, fileName=None):
        if(fileName==None):
            raise ValueError("dataloader requires a fileName when loading a local file.")
        if(type(fileName)!=str):
            raise ValueError("fileName must be a string.")
        elif(os.path.exists(fileName)!=True):
            raise ValueError("dataloader requires a valid file in the directory.")
        elif(fileName[len(fileName)-1]!="v" or fileName[len(fileName)-2]!="s" or fileName[len(fileName)-3]!="c" or fileName[len(fileName)-4]!="."):
            raise ValueError("fileName must be a csv file in the directory.")
        else:
            data = pd.read_csv(fileName)
            newData = pd.DataFrame()
            found = -1
            lower = -1
            for x in range(0,data.columns.shape[0]):
                if(data.columns[x]=="Date" ):
                    found = x
                    break
                if(data.columns[x]=="date"):
                    found = x
                    lower = 1
                    break
            if(found==-1):
                raise ValueError("dataloader requires a Date column in localy loaded csv files.")
            if(lower == 1):
                newData['Date'] = data['date']
            else:
                newData['Date'] = data['Date']
            newData["Date"] = self.__sortDate(newData["Date"])

            found = -1
            lower = -1
            for x in range(0,data.columns.shape[0]):
                if(data.columns[x]=="Open"):
                    found=x
                    break
                if(data.columns[x]=="open"):
                    found = x
                    lower = 1
                    break
            if(found==-1):
                raise ValueError("dataloader requires a Open column in localy loaded csv files.")
            if(lower == 1):
                newData['Open'] = data['open']
            else:
                newData['Open'] = data['Open']

            found = -1
            lower = -1
            for x in range(0,data.columns.shape[0]):
                if(data.columns[x]=="High"):
                    found=x
                    break
                if(data.columns[x]=="high"):
                    found = x
                    lower = 1
                    break
            if(found==-1):
                raise ValueError("dataloader requires a High column in localy loaded csv files.")
            if(lower == 1):
                newData['High'] = data['high']
            else:
                newData['High'] = data['High']

            found = -1
            lower = -1
            for x in range(0,data.columns.shape[0]):
                if(data.columns[x]=="Low"):
                    found=x
                    break
                if(data.columns[x]=="low"):
                    found = x
                    lower = 1
                    break
            if(found==-1):
                raise ValueError("dataloader requires a Low column in localy loaded csv files.")
            if(lower == 1):
                newData['Low'] = data['low']
            else:
                newData['Low'] = data['Low']

            found = -1
            lower = -1
            for x in range(0,data.columns.shape[0]):
                if(data.columns[x]=="Close"):
                    found=x
                    break
                if(data.columns[x]=="close"):
                    found = x
                    lower = 1
                    break
            if(found==-1):
                raise ValueError("dataloader requires a Close column in localy loaded csv files.")
            if(lower == 1):
                newData['Close'] = data['close']
            else:
                newData['Close'] = data['Close']

            found = -1
            lower = -1
            for x in range(0,data.columns.shape[0]):
                if(data.columns[x]=="Volume"):
                    found=x
                    break
                if(data.columns[x]=="volume"):
                    found = x
                    lower = 1
                    break
            if(found==-1):
                raise ValueError("dataloader requires a Volume column in localy loaded csv files.")
            if(lower == 1):
                newData['Volume'] = data['volume']
            else:
                newData['Volume'] = data['Volume']
            newData = newData.sort_values(by='Date',ascending=False)
            newData.index = range(newData.shape[0])
            self.data= newData
            for index in range(0,self.data.shape[0]-2):
                if(self.data["Date"][index].day==self.data["Date"][index+1].day):
                    raise ValueError("The data comtains two sets of data for a single day")

    # precomputes values and add the to the dataframe
    def precompute(self, indicators=[], multiCore = False, verbose=None):
        if(verbose==None):
            verbose=self.__verbose
        if(verbose>0):
            print("precomputing values")
        if(multiCore==True):
            from pathos.multiprocessing import ProcessingPool as Pool
            import multiprocessing
            for indicator in indicators:
                found = False
                if(indicator in self.__precompute):
                    continue
                pool = Pool(nodes=multiprocessing.cpu_count())
                self.dashes = self.__return_Dashes(indicator)
                dashes =self.dashes
                self.indicator = indicator


                if(indicator[:dashes[0]-1] == "EMA"):
                    self.data[indicator] = np.nan
                    self.data[indicator] = pool.map(self.__precomputeApply_EMA, range(0,self.data.shape[0]))
                    found = True
                if(indicator[:dashes[0]-1] == "SMA"):
                    self.data[indicator] = np.nan
                    self.data[indicator] = pool.map(self.__precomputeApply_SMA, range(0,self.data.shape[0]))
                    found = True

                if(indicator[:dashes[0]-1] == "WMA"):
                    self.data[indicator] = np.nan
                    self.data[indicator] = pool.map(self.__precomputeApply_WMA, range(0,self.data.shape[0]))
                    found = True

                if(indicator[:dashes[0]-1] == "DEMA"):
                    self.data[indicator] = np.nan
                    self.data[indicator] = pool.map(self.__precomputeApply_DEMA, range(0,self.data.shape[0]))
                    found = True

                if(indicator[:dashes[0]-1] == "TEMA"):
                    self.data[indicator] = np.nan
                    self.data[indicator] = pool.map(self.__precomputeApply_TEMA, range(0,self.data.shape[0]))
                    found = True

                if(indicator[:dashes[0]-1] == "TRIMA"):
                    self.data[indicator] = np.nan
                    self.data[indicator] = pool.map(self.__precomputeApply_TRIMA, range(0,self.data.shape[0]))
                    found = True

                if(indicator[:dashes[0]-1] == "VWAP"):
                    self.data[indicator] = np.nan
                    self.data[indicator] = pool.map(self.__precomputeApply_VWAP, range(0,self.data.shape[0]))
                    found = True

                if(found==False):
                    raise ValueError( indicator + " is not a recognised indicator for use in precompute")

                self.__precompute.append(indicator)
        else:
            for indicator in indicators:
                found = False
                if(indicator in self.__precompute):
                    continue

                self.dashes = self.__return_Dashes(indicator)
                dashes =self.dashes
                self.indicator = indicator


                if(indicator[:dashes[0]-1] == "EMA"):
                    self.data[indicator] = range(0,self.data.shape[0])
                    self.data[indicator] = self.data[indicator].apply(self.__precomputeApply_EMA)
                    found = True
                if(indicator[:dashes[0]-1] == "SMA"):
                    self.data[indicator] = range(0,self.data.shape[0])
                    self.data[indicator] = self.data[indicator].apply(self.__precomputeApply_SMA)
                    found = True

                if(indicator[:dashes[0]-1] == "WMA"):
                    self.data[indicator] = range(0,self.data.shape[0])
                    self.data[indicator] = self.data[indicator].apply(self.__precomputeApply_WMA)
                    found = True

                if(indicator[:dashes[0]-1] == "DEMA"):
                    self.data[indicator] = range(0,self.data.shape[0])
                    self.data[indicator] = self.data[indicator].apply(self.__precomputeApply_DEMA)
                    found = True

                if(indicator[:dashes[0]-1] == "TEMA"):
                    self.data[indicator] = range(0,self.data.shape[0])
                    self.data[indicator] = self.data[indicator].apply(self.__precomputeApply_TEMA)
                    found = True

                if(indicator[:dashes[0]-1] == "TRIMA"):
                    self.data[indicator] = range(0,self.data.shape[0])
                    self.data[indicator] = self.data[indicator].apply(self.__precomputeApply_TRIMA)
                    found = True

                if(indicator[:dashes[0]-1] == "VWAP"):
                    self.data[indicator] = range(0,self.data.shape[0])
                    self.data[indicator] = self.data[indicator].apply(self.__precomputeApply_VWAP)
                    found = True

                if(found==False):
                    raise ValueError( indicator + " is not a recognised indicator for use in precompute")

                self.__precompute.append(indicator)
        if(verbose>0):
            print("Finished precomputing")


    # The following functions are helper functions to precompute
    def __precomputeApply_EMA(self, row):
        return self.get_EMA(row, int(self.indicator[self.dashes[0]:self.dashes[1]-1]), self.indicator[self.dashes[1]:], 2)

    def __precomputeApply_SMA(self, row):
        return self.get_SMA(row, int(self.indicator[self.dashes[0]:self.dashes[1]-1]), self.indicator[self.dashes[1]:])

    def __precomputeApply_WMA(self, row):
        return self.get_WMA(row, int(self.indicator[self.dashes[0]:self.dashes[1]-1]), self.indicator[self.dashes[1]:])

    def __precomputeApply_DEMA(self, row):
        return self.get_DEMA(row, int(self.indicator[self.dashes[0]:self.dashes[1]-1]), self.indicator[self.dashes[1]:])

    def __precomputeApply_TEMA(self, row):
        return self.get_TEMA(row, int(self.indicator[self.dashes[0]:self.dashes[1]-1]), self.indicator[self.dashes[1]:])

    def __precomputeApply_TRIMA(self, row):
        return self.get_TRIMA(row, int(self.indicator[self.dashes[0]:self.dashes[1]-1]), self.indicator[self.dashes[1]:])

    def __precomputeApply_VWAP(self, row):
        return self.get_VWAP(row, int(self.indicator[self.dashes[0]:self.dashes[1]-1]), self.indicator[self.dashes[1]:])

    def __return_Dashes(self, string):
        out = []
        for x in range(0,len(string)):
            if(string[x]=="-"):
                out.append(x+1)
        return out

    # Returns a list of precomputed values for the dataloader
    def get_PRECOMPUTED_VALUES(self, verbose=None):
        if(verbose==None):
            verbose=self.__verbose
        out = []
        for col in self.data.columns:
            if(col!="High" and col!="Low" and col!="Open" and col!="Close" and col!="Volume"  and col!="Fundamentals date" and col!="Date"):
                out.append(col)
        if(verbose>0):
            print(out)
        return out



    # Function role: Helper function for __load_LOCAL  (Sorts the dates into the required format using one conversion to avoid confusion of pd.to_datetime())
    def __sortDate(self,newDates1):
        warnings.filterwarnings('ignore', '.*.*',)
        holder = newDates1
        newDates = newDates1
        try:
            for x in range(0,newDates1.shape[0]):
                newDates.loc[x] = pd.to_datetime(newDates.iloc[x], format='%Y-%m-%d')
        except ValueError:
            try:
                newDates = holder
                for x in range(0,newDates1.shape[0]):
                    newDates.loc[x] = pd.to_datetime(newDates.iloc[x], format='%Y-%d-%m')
                return
            except ValueError:
                try:
                    newDates = holder
                    for x in range(0,newDates1.shape[0]):
                        newDates.loc[x] = pd.to_datetime(newDates.iloc[x], format='%d-%m-%Y')
                except ValueError:
                    try:
                        newDates = holder
                        for x in range(0,newDates1.shape[0]):
                            newDates.loc[x] = pd.to_datetime(newDates.iloc[x], format='%m-%d-%Y')
                    except ValueError:
                        try:
                            for x in range(0,newDates1.shape[0]):
                                newDates.loc[x] = pd.to_datetime(newDates.iloc[x], format='%Y/%m/%d')
                        except ValueError:
                            try:
                                newDates = holder
                                for x in range(0,newDates1.shape[0]):
                                    newDates.loc[x] = pd.to_datetime(newDates.iloc[x], format='%Y/%d/%m')
                                return
                            except ValueError:
                                try:
                                    newDates = holder
                                    for x in range(0,newDates1.shape[0]):
                                        newDates.loc[x] = pd.to_datetime(newDates.iloc[x], format='%d/%m/%Y')
                                except ValueError:
                                    try:
                                        newDates = holder
                                        for x in range(0,newDates1.shape[0]):
                                            newDates.loc[x] = pd.to_datetime(newDates.iloc[x], format='%m/%d/%Y')
                                    except ValueError:
                                        raise ValueError("Inputs for the date column are not of supported format try '%Y-%m-%d' format.")

        return newDates

    # def addFundamentals(self,fileName=None, timeFrame=None):
    #
    #     if(fileName==None):
    #         raise ValueError("addFundamentals requires a fileName attribute.")
    #     if(os.path.isfile(fileName)==False):
    #         raise ValueError("fileName is not a file in the directory.")
    #     if(type(fileName)!=str):
    #         raise ValueError("fileName must be a string.")
    #     if(fileName[len(fileName)-1]!="v" or fileName[len(fileName)-2]!="s" or fileName[len(fileName)-3]!="c" or fileName[len(fileName)-4]!="."):
    #         raise ValueError("fileName must be a csv file in the directory.")
    #     if(timeFrame==None):
    #         raise ValueError("addFundamentals requires a timeFrame attribute.")
    #     if(type(timeFrame)!=str):
    #         raise ValueError("timeFrame must be a string.")
    #     if(timeFrame!="Quarter" and timeFrame!="Year"):
    #         raise ValueError("timeFrame must either be: Quarter or Year")
    #
    #
    #     inputData = pd.read_csv(fileName)
    #     if(timeFrame=="Quarter"):
    #
    #         if("Quarter end"!=inputData.columns.any()):
    #             raise ValueError("for a timeFrame of Quarter a 'Quarter end' column is required")
    #
    #         inputData["Quarter end"] = self.__sortDate(inputData["Quarter end"])
    #         inputData = inputData.sort_values(by="Quarter end", ascending=False )
    #         self.data["Fundamentals date"] = np.nan
    #         inputPointer = 0
    #         holder = []
    #         for x in range(0,self.data.shape[0]):
    #             go = True
    #             while(go==True):
    #                 if(inputData["Quarter end"][inputPointer]<self.data["Date"][x]):
    #                     holder.append(inputData["Quarter end"][inputPointer])
    #                     go = False
    #                 elif(inputData["Quarter end"][inputPointer]==self.data["Date"][x]):
    #                     holder.append(inputData["Quarter end"][inputPointer])
    #                     go = False
    #                 elif(inputPointer==inputData.shape[0]-1):
    #                     holder.append(np.datetime64("NaT"))
    #                     go = False
    #                 else:
    #                     inputPointer = inputPointer + 1
    #         self.data["Fundamentals date"] = pd.DataFrame(holder)
    #         inputData = inputData.rename(columns={"Quarter end":"Time period end"})
    #         inputData = inputData.set_index("Time period end")
    #         self.__fundamentals = inputData
    #
    #     if(timeFrame=="Year"):
    #         if("Year end"!=inputData.columns.any()):
    #             raise ValueError("for a timeFrame of Year a 'Year end' column is required")
    #
    #         inputData["Year end"] = self.__sortDate(inputData["Year end"])
    #         inputData = inputData.sort_values(by="Year end", ascending=False )
    #         self.data["Fundamentals date"] = np.nan
    #         inputPointer = 0
    #         holder = []
    #         for x in range(0,self.data.shape[0]):
    #             go = True
    #             while(go==True):
    #                 if(inputData["Year end"][inputPointer]<self.data["Date"][x]):
    #                     holder.append(inputData["Year end"][inputPointer])
    #                     go = False
    #                 elif(inputData["Year end"][inputPointer]==self.data["Date"][x]):
    #                     holder.append(inputData["Year end"][inputPointer])
    #                     go = False
    #                 elif(inputPointer==inputData.shape[0]-1):
    #                     holder.append(np.datetime64("NaT"))
    #                     go = False
    #                 else:
    #                     inputPointer = inputPointer + 1
    #         self.data["Fundamentals date"] = pd.DataFrame(holder)
    #         inputData = inputData.rename(columns={"Year end":"Time period end"})
    #         inputData = inputData.set_index("Time period end")
    #         self.__fundamentals = inputData

    # Function role: cleans the data with option to remove zero values and very low values
    def clean(self, nans=True, zerosAndLows=0, verbose=None):
        if(verbose==None):
            verbose=self.__verbose
        if(verbose>0):
            print("Cleaning data ...")
        cols = self.data.columns
        for y in range(0,self.data.shape[1]):
            for b in range(0,self.data.shape[0]):
                x = self.data.shape[0] - (b + 1)
                if(nans==True and cols[y]!="Date" and cols[y]!="Volume" and cols[y]!="Fundamentals date"):
                    self.data.at[x, cols[y]] = self.__sortNan(cols[y], x, -1)
                if(zerosAndLows!=0 and cols[y]!="Date" and cols[y]!="Volume" and cols[y]!="Fundamentals date" and x<self.data.shape[0]-2):
                    self.data.at[x, cols[y]] = self.__sortZeros(cols[y], x, 1, zerosAndLows)
                elif(zerosAndLows!=0 and cols[y]!="Date" and cols[y]!="Volume" and cols[y]!="Fundamentals date" and x<self.data.shape[0]-1):
                    self.data.at[x, cols[y]] = self.__sortZeros(cols[y], x, -1, zerosAndLows)
        for y in range(1,self.data.shape[1]-1):
            if(self.data[cols[y]][self.data.shape[0]-1]==0 and cols[y]!="Date" and cols[y]!="Volume" and cols[y]!="Fundamentals date"):
                self.data[cols[y]][self.data.shape[0]-1] = self.data[cols[y]][self.data.shape[0]-2]
        if(verbose>0):
            print("Data cleaned")

    # Function role: Helper function for clean()
    def __sortNan(self, colName, index, upOrDown):
        if(np.isnan(self.data[colName][index])):
            if(index<self.data.shape[0]-1 and index>0):
                return self.__sortNan(colName, index+upOrDown, upOrDown)
            else:
                if(index>self.data.shape[0]-2):
                    return self.__sortNan(colName, index-1, -1)
                if(index<1):
                    return self.__sortNan(colName, index+1, +1)
        else:
            return self.data[colName][index]

    # Function role: Helper function for clean()
    def __sortZeros(self, colName, index, upOrDown, zerosAndLows):
        if(self.data[colName][index]==0 or self.data[colName][index]<self.data[colName][index+1]/zerosAndLows):
            if(index<=self.data.shape[0]-1 and index>=0):
                return self.__sortZeros(colName, index+upOrDown, upOrDown, zerosAndLows)
            else:
                if(index>self.data.shape[0]-2):
                    return self.__sortZeros(colName, index-1, -1, zerosAndLows)
                if(index<1):
                    return self.__sortZeros(colName, index+1, +1, zerosAndLows)
        else:
            return self.data[colName][index]

    # Function role: Displays the data in the dataloader
    def display(self):
        print(self.data)


    # Function role: Saves a copy of the data in the dataloader in "./dataloaders"
    def save(self, verbose=None):
        if(verbose==None):
            verbose=self.__verbose
        try:
            # Create target Directory
            os.mkdir("dataloaders")
            try:
                file = open("./dataloaders/" + str(self.__instrument) + "-dataloader.pkl", 'wb')
                pickle.dump([self.data,self.__fundamentals], file)
                file.close()
            except AttributeError:
                file = open("./dataloaders/" + str(self.__instrument) + "-dataloader.pkl", 'wb')
                pickle.dump([self.data], file)
                file.close()
        except FileExistsError:
            try:
                file = open("./dataloaders/" + str(self.__instrument) + "-dataloader.pkl", 'wb')
                pickle.dump([self.data,self.__fundamentals], file)
                file.close()
            except AttributeError:
                file = open("./dataloaders/" + str(self.__instrument) + "-dataloader.pkl", 'wb')
                pickle.dump([self.data], file)
                file.close()
        if(verbose>0):
            print(self.__instrument+" "+self.__dataType+" from "+self.__source+" dataloader saved")

    # Function role: Called by __intit__() and loads the data saved with instrument name that was provided
    def __load(self):
        if(os.path.exists("./dataloaders/" + str(self.__instrument) + "-dataloader.pkl")==False):
            raise ValueError("preload requires saved data for this instument and none was found.")
        file = open("./dataloaders/" + str(self.__instrument) + "-dataloader.pkl", 'rb')
        data = pickle.load(file)
        file.close()
        if(len(data)==2):
            self.data= data[0]
            self.__fundamentals  = data[1]
        else:
            self.data= data[0]
        for col in self.data:
            if(col != "Date" and col != "Open" and col != "High" and col != "Low" and col != "Close" and col != "Volume"):
                self.__precompute.append(col)

    # Function role: returns the data in the dataloader
    def output(self):
        return self.data

    # Function role: returns the info in the dataloader
    def info(self, verbose=None):
        if(verbose==None):
            verbose=self.__verbose
        if(verbose>0):
            print(self.__instrument, self.__dataType, self.__source)
        return  self.__instrument, self.__dataType, self.__source

    # def get_FUNDAMENTALS(self, index, amount):
    #     date = self.data["Fundamentals date"][index]
    #     if(str(date)==str(np.datetime64("NaT"))):
    #         return None
    #     funData = self.__fundamentals
    #     indexs = funData.index
    #     found=False
    #     x=0
    #     index1 = 0
    #     while(found==False):
    #         if(indexs[x]==date):
    #             index1 = x
    #             found = True
    #         else:
    #             x = x + 1
    #     if(x+amount>=indexs.shape[0]):
    #         out =  funData[date:indexs[indexs.shape[0]-1]]
    #         out.reset_index(level=0, inplace=True)
    #         return out
    #     else:
    #         out =  funData[date:indexs[x+amount-1]]
    #         out.reset_index(level=0, inplace=True)
    #         return out

# The following functions compute different technical indicators for the data
    def get_SMA(self, index, days, type):
        if(self.__precompute!=[]):
            if("SMA-"+str(days)+"-"+type in self.__precompute):
                if(np.isnan(self.data["SMA-"+str(days)+"-"+type][index])):
                    return None
                else:
                    return self.data["SMA-"+str(days)+"-"+type][index]
            else:
                if(index+days>self.data.shape[0] or days<1):
                    return None
                else:
                    return self.data[type][index:index+days].mean()
        else:
            if(index+days>self.data.shape[0] or days<1):
                return None
            else:
                return self.data[type][index:index+days].mean()

    def get_EMA(self, index, days, type, smoothing):
        if(self.__precompute!=[]):
            if("EMA-"+str(days)+"-"+type in self.__precompute):
                if(np.isnan(self.data["EMA-"+str(days)+"-"+type][index])):
                    return None
                else:
                    return self.data["EMA-"+str(days)+"-"+type][index]
            else:
                if(index+days>self.data.shape[0] or days<1):
                    return None
                else:
                    sum = 0
                    x=index+days-1
                    sum = self.data[type][x]
                    while x>index-1 and x>=0:
                        sum = (self.data[type][x]-sum)*(smoothing/(days+1)) + sum
                        x = x - 1
                    return sum
        else:
            if(index+days>self.data.shape[0] or days<1):
                return None
            else:
                sum = 0
                x=index+days-1
                sum = self.data[type][x]
                while x>index-1 and x>=0:
                    sum = (self.data[type][x]-sum)*(smoothing/(days+1)) + sum
                    x = x - 1
                return sum

    def get_WMA(self, index, days, type):
        if(self.__precompute!=[]):
            if("WMA-"+str(days)+"-"+type in self.__precompute):
                if(np.isnan(self.data["WMA-"+str(days)+"-"+type][index])):
                    return None
                else:
                    return self.data["WMA-"+str(days)+"-"+type][index]

            else:
                if(index+days>self.data.shape[0] or days<1):
                    return None
                else:
                    sum = 0
                    xsum = 0
                    data=self.output()[index:index+days]
                    for x in range(index,index+days):
                        sum = sum + data[type][x]*(days+index-x)
                        xsum = xsum + (x - index + 1)
                    sum = sum/xsum
                    return sum
        else:
            if(index+days>self.data.shape[0] or days<1):
                return None
            else:
                sum = 0
                xsum = 0
                data=self.output()[index:index+days]
                for x in range(index,index+days):
                    sum = sum + data[type][x]*(days+index-x)
                    xsum = xsum + (x - index + 1)
                sum = sum/xsum
                return sum

    def get_DEMA(self, index, days, type):
        if(self.__precompute!=[]):
            if("DEMA-"+str(days)+"-"+type in self.__precompute):
                if(np.isnan(self.data["DEMA-"+str(days)+"-"+type][index])):
                    return None
                else:
                    return self.data["DEMA-"+str(days)+"-"+type][index]
            else:
                if(index+2*days-1>self.data.shape[0] or days<1):
                    return None
                else:
                    emas = np.zeros(days)
                    for x in range(0,days):
                        emas[x] = self.get_EMA(index+x,days,type,2)
                    sum = 0
                    sum = emas.sum()/days
                    x=days-2
                    while(x>=0):
                        sum = (emas[x]-sum)*(2/(days+1)) + sum
                        x = x - 1
                    emaEma =  sum
                    return 2*emas[0] - emaEma
        else:
            if(index+2*days-1>self.data.shape[0] or days<1):
                return None
            else:
                emas = np.zeros(days)
                for x in range(0,days):
                    emas[x] = self.get_EMA(index+x,days,type,2)
                sum = 0
                sum = emas.sum()/days
                x=days-2
                while(x>=0):
                    sum = (emas[x]-sum)*(2/(days+1)) + sum
                    x = x - 1
                emaEma =  sum
                return 2*emas[0] - emaEma

    def get_TEMA(self, index, days, type):
        if(self.__precompute!=[]):
            if("TEMA-"+str(days)+"-"+type in self.__precompute):
                if(np.isnan(self.data["TEMA-"+str(days)+"-"+type][index])):
                    return None
                else:
                    return self.data["TEMA-"+str(days)+"-"+type][index]
            else:
                if(index+3*days-1>self.data.shape[0] or days<1):
                    return None
                else:
                    ema1 = self.get_EMA(index, days, type, 2)
                    ema2s = np.zeros(days)
                    for x in range(0,days):
                        ema2s[x] = -1*(self.get_DEMA(index+x, days, type) - 2*self.get_EMA(index+x, days, type, 2))
                    sum = ema2s.sum()/days
                    x=days-2
                    while(x>=0):
                        sum = (ema2s[x]-sum)*(2/(days+1)) + sum
                        x = x - 1
                    ema3 =  sum
                    return 3*ema1 - 3*ema2s[0] + ema3
        else:
            if(index+3*days-1>self.data.shape[0] or days<1):
                return None
            else:
                ema1 = self.get_EMA(index, days, type, 2)
                ema2s = np.zeros(days)
                for x in range(0,days):
                    ema2s[x] = -1*(self.get_DEMA(index+x, days, type) - 2*self.get_EMA(index+x, days, type, 2))
                sum = ema2s.sum()/days
                x=days-2
                while(x>=0):
                    sum = (ema2s[x]-sum)*(2/(days+1)) + sum
                    x = x - 1
                ema3 =  sum
                return 3*ema1 - 3*ema2s[0] + ema3

    def get_TRIMA(self, index, days, type):
        if(self.__precompute!=[]):
            if("TRIMA-"+str(days)+"-"+type in self.__precompute):
                if(np.isnan(self.data["TRIMA-"+str(days)+"-"+type][index])):
                    return None
                else:
                    return self.data["TRIMA-"+str(days)+"-"+type][index]
            else:
                if(index+2*days-1>self.data.shape[0] or days<1):
                    return None
                else:
                    sum = 0
                    for x in range(0,days):
                        sum = sum + self.get_SMA(index + x,days,type)
                    return sum/days
        else:
            if(index+2*days-1>self.data.shape[0] or days<1):
                return None
            else:
                sum = 0
                for x in range(0,days):
                    sum = sum + self.get_SMA(index + x,days,type)
                return sum/days

    # # # TODO: implement this
    # def get_KAMA(self, index, days):
    #     this = todo
    # # # TODO: implement this
    # def get_MAMA(self, index, type):
    #     this = todo

    def get_VWAP(self, index, days, type):
        if(self.__precompute!=[]):
            if("VWAP-"+str(days)+"-"+type in self.__precompute):
                if(np.isnan(self.data["VWAP-"+str(days)+"-"+type][index])):
                    return None
                else:
                    return self.data["VWAP-"+str(days)+"-"+type][index]
            else:
                if(index+days>self.data.shape[0] or days<1):
                    return None
                else:
                    sumPriTVol = 0
                    sumVol = 0
                    for x in range(0,days):
                        sumPriTVol = sumPriTVol + self.data[type][index+x]*self.data["Volume"][index+x]
                        sumVol = sumVol + self.data["Volume"][index+x]
                    return sumPriTVol/sumVol
        else:
            if(index+days>self.data.shape[0] or days<1):
                return None
            else:
                sumPriTVol = 0
                sumVol = 0
                for x in range(0,days):
                    sumPriTVol = sumPriTVol + self.data[type][index+x]*self.data["Volume"][index+x]
                    sumVol = sumVol + self.data["Volume"][index+x]
                return sumPriTVol/sumVol

    def get_MACD(self, index, type):
        if(index+26>self.data.shape[0]):
            return None
        else:
            return self.get_EMA(index, 12, type, 2) - self.get_EMA(index, 26, type, 2)

    def get_MACDEXT(self, index, type, funct, slow, fast):
        if(index+slow>self.data.shape[0] or slow<fast):
            return None
        else:
            if(funct=="EMA"):
                return self.get_EMA(index, fast, type, 2) - self.get_EMA(index, slow, type, 2)
            elif(funct=="SMA"):
                return self.get_SMA(index, fast, type) - self.get_SMA(index, slow, type)
            elif(funct=="DEMA"):
                if(index+slow*2-1>self.data.shape[0]):
                    return None
                else:
                    return self.get_DEMA(index, fast, type) - self.get_DEMA(index, slow, type)
            elif(funct=="WMA"):
                return self.get_WMA(index, fast, type) - self.get_WMA(index, slow, type)
            elif(funct=="VWAP"):
                return self.get_VWAP(index, fast, type) - self.get_VWAP(index, slow, type)
            elif(funct=="TRIMA"):
                if(index+slow*2-1>self.data.shape[0]):
                    return None
                else:
                    return self.get_TRIMA(index, fast, type) - self.get_TRIMA(index, slow, type)
            else:
                raise ValueError("Check funct is a valid string: EMA, SMA, DEMA, WMA, WVAP or TRIMA.")

    def get_STOCH(self, index):
        if(index+17>self.data.shape[0]):
            return None
        else:
            high = 0
            low = 999999999999
            for x in range(0,14):
                if(self.data["High"][index+x]>high):
                    high = self.data["High"][index+x]
                if(self.data["Low"][index+x]<low):
                    low = self.data["Low"][index+x]
            perK = 100*(self.data["Close"][index]-low)/(high-low)
            k1 = perK
            high = 0
            low = 999999999999
            for x in range(0,14):
                if(self.data["High"][index+1+x]>high):
                    high = self.data["High"][index+1+x]
                if(self.data["Low"][index+1+x]<low):
                    low = self.data["Low"][index+1+x]
            k2 = 100*(self.data["Close"][index+1]-low)/(high-low)
            high = 0
            low = 999999999999
            for x in range(0,14):
                if(self.data["High"][index+2+x]>high):
                    high = self.data["High"][index+2+x]
                if(self.data["Low"][index+2+x]<low):
                    low = self.data["Low"][index+2+x]
            k3 = 100*(self.data["Close"][index+2]-low)/(high-low)
            perD = (k1+k2+k3)/3
            return (perK, perD)

    def get_RSI(self, index, days, type):
        if(index+days>=self.data.shape[0] or days<1):
            return None
        else:
            up = 0
            down = 0
            for x in range(index, index+days):
                if(self.data[type][x]>self.data[type][x+1]):
                    up = up + (self.data[type][x]-self.data[type][x+1])
                else:
                    down = down + (self.data[type][x+1]-self.data[type][x])
            if(down==0):
                return 100
            up = up/days
            down = down/days
            return( 100-(100/( 1 + (up/down))))

    def get_STOCHRSI(self, index, days, type):
        if(index+2*days>self.data.shape[0] or days<1):
            return None
        else:
            high = 0
            low = 9999999
            for x in range(0,days):
                rsi = self.get_RSI(index+x, days, type)
                if(rsi>high):
                    high = rsi
                if(rsi<low):
                    low = rsi
            if(self.get_RSI(index, days, type)==0):
                return 0
            elif(high==low ):
                return 100
            else:
                return 100*(self.get_RSI(index,days,type)-low)/(high-low)

    def get_WILLR(self, index, days):
        if(index+days>self.data.shape[0] or days<1):
            return None
        else:
            high = 0
            low = 999999999999
            for x in range(0,days):
                if(self.data["High"][index+x]>high):
                    high = self.data["High"][index+x]
                if(self.data["Low"][index+x]<low):
                    low = self.data["Low"][index+x]
            return 100*(high - self.data["Close"][index])/(high-low)

# # # TODO: implement this
#     def get_ADX(self, index, days):

#
# # # TODO: implement this
#     def get_ADXR(self, index, fast, slow):
#         this = todo

    def get_APO(self, index, fast, slow, type):
        if(index+slow>self.data.shape[0] or fast<1 or slow<1):
            return None
        else:
            return self.get_EMA(index,fast,type,2)-self.get_EMA(index,slow,type,2)

    def get_PPO(self, index, type):
        if(index+26>self.data.shape[0]):
            return None
        else:
            return 100*(self.get_EMA(index,12,type,2)-self.get_EMA(index,26,type,2))/self.get_EMA(index,26,type,2)

    def get_MOM(self, index, days, type):
        if(index+days>=self.data.shape[0] or days<1):
            return None
        else:
            return self.data[type][index]-self.data[type][index+days]

    def get_BOP(self, index, days):
        if(index+days>=self.data.shape[0] or days<1):
            return None
        else:
            sum = 0
            for x in range(0,days):
                sum = sum + (self.data["Close"][index+x]-self.data["Open"][index+x])/(self.data["High"][index+x]-self.data["Low"][index+x])
            sum = sum/days
            return sum

    def get_CCI(self, index, days):
        if(index+days*2>self.data.shape[0] or days<2):
            return None
        else:
            typicals = np.zeros(days)
            for x in range(0,days):
                sum = 0
                for y in range(0,days):
                    sum = sum + (self.data["Close"][index+x+y] + self.data["Low"][index+x+y] + self.data["High"][index+x+y])/3
                typicals[x] = sum
            MA = typicals.sum()/days
            meanDev = 0
            for x in range(0,days):
                meanDev = meanDev + abs(typicals[x] - MA)
            meanDev = meanDev/days
            return (typicals[0]-MA)/(0.015*meanDev)

    def get_CMO(self, index, days):
        if(index+days>=self.data.shape[0] or days<1):
            return None
        else:
            su = 0
            sd = 0
            for x in range(0,days):
                if(self.data["Close"][index+x+1]<self.data["Close"][index+x]):
                    su = su + self.data["Close"][index+x] - self.data["Close"][index+x+1]
                if(self.data["Close"][index+x+1]>self.data["Close"][index+x]):
                    sd = sd + self.data["Close"][index+x+1] - self.data["Close"][index+x]
            return 100*((su-sd)/(su+sd))

    def get_ROC(self, index, days):
        if(index+days>=self.data.shape[0] or days<1):
            return None
        else:
            return 100*(self.data["Close"][index]-self.data["Close"][index+days])/self.data["Close"][index+days]
