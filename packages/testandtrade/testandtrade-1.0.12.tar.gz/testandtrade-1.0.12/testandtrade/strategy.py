from testandtrade.dataloader import dataloader
import numpy as np
import math
import sys
import time
import copy
import threading
import inspect
import warnings

class strategy:

    # Adds the functions for the stratergy
    def __init__(self, stratName = "Stratergy", everyDayOpen=None, everyDayClose=None, everyWeek=None, everyMonth=None, everyYear=None, verbose=1):
        if(inspect.isfunction(everyDayOpen)!=True and everyDayOpen!=None):
            raise ValueError("everyDayOpen must be a function.")
        if(inspect.isfunction(everyDayClose)!=True and everyDayClose!=None):
            raise ValueError("everyDayClose must be a function.")
        if(inspect.isfunction(everyWeek)!=True and everyWeek!=None):
            raise ValueError("everyWeek must be a function.")
        if(inspect.isfunction(everyMonth)!=True and everyMonth!=None):
            raise ValueError("everyMonth must be a function.")
        if(inspect.isfunction(everyYear)!=True and everyYear!=None):
            raise ValueError("everyYear must be a function.")
        self.__everyYear = everyYear
        self.__everyMonth = everyMonth
        self.__everyWeek = everyWeek
        self.__everyDayOpen = everyDayOpen
        self.__everyDayClose = everyDayClose
        self.__stratName = stratName
        self.testMode = False
        self.__verbose = verbose
        self.__original_dict__ = copy.deepcopy(self.__dict__)

    # Runs a test for the stratergy
    def runTest(self, data=None, verbose=None, startingCapital=100000, plot=[]):
        if(verbose==None):
            verbose=self.__verbose
        if(type(data)!=dataloader):
            raise ValueError("data parameter must be a dataloader object.")
        try:
           val = int(startingCapital)
        except ValueError:
            raise ValueError("startingCapital must be an integer.")
        if(verbose>0):
            print("Running test")

        self.__startingIndex = data.output().shape[0]-2
        self.__startingCapital = startingCapital
        self.__currentCapital = startingCapital
        self.__currentIndex = self.__startingIndex
        self.__testData = data
        self.__currentFunction = None
        self.__currentStockPossition = 0

        functions = []
        if(self.__everyYear!=None):
            functions.append(self.__doYear)
        if(self.__everyMonth!=None):
            functions.append(self.__doMonth)
        if(self.__everyWeek!=None):
            functions.append(self.__doWeek)
        if(self.__everyDayOpen!=None):
            functions.append(self.__doDayOpen)
        if(self.__everyDayClose!=None):
            functions.append(self.__doDayClose)
        if(plot!=[]):
            self.__plotFunctions = []
            found = False

            # add ploting functions here
            found = True
            self.__strategyPlotData = np.zeros(self.__startingIndex+1)
            def y(self):
                self.__strategyPlotData[self.__currentIndex] = self.get_TOTALCAPITAL()
            self.__plotFunctions.append(y)
            plot.append("Strategy")

            def pltDataCollector(self):
                # sets the value of the stuff to be plotted
                self.__currentFunction = "do"
                for plotFunct in self.__plotFunctions:
                    plotFunct(self)

        if(verbose>0):
            self.__progressBarPoints = []
            self.__progressBarPointer = 0
            self.__progressBarPoints.append(self.__startingIndex)
            split = math.floor(self.__testData.data.shape[0]/20)
            x=19
            while(x>-1):
                self.__progressBarPoints.append(split*x)
                x=x-1
            def progressBar(self):
                if(self.__currentIndex==self.__progressBarPoints[self.__progressBarPointer]):
                    sys.stdout.write('\r')
                    # the exact output you're looking for:
                    sys.stdout.write("[%-80s] %d%%" % ('='*(4*self.__progressBarPointer-1)+">", 5*self.__progressBarPointer))
                    sys.stdout.flush()
                    self.__progressBarPointer = self.__progressBarPointer + 1

        if(len(plot)>0):
            if(verbose>0):
                while(self.__currentIndex>=0):
                    progressBar(self)
                    pltDataCollector(self)
                    for funct in functions:
                        funct()
                    # do plotting assignmets
                    self.__currentIndex = self.__currentIndex - 1
            else:
                while(self.__currentIndex>=0):
                    pltDataCollector(self)
                    for funct in functions:
                        funct()
                    # do plotting assignmets
                    self.__currentIndex = self.__currentIndex - 1
        else:
            if(verbose>0):
                while(self.__currentIndex>=0):
                    progressBar(self)
                    for funct in functions:
                        funct()
                    # do plotting assignmets
                    self.__currentIndex = self.__currentIndex - 1
            else:
                while(self.__currentIndex>=0):
                    for funct in functions:
                        funct()
                    # do plotting assignmets
                    self.__currentIndex = self.__currentIndex - 1

        if(verbose!=0):
            print()

        if(plot!=[] and self.testMode==False):
            thread1 = threading.Thread(target = self.__plot, args = (plot,self.__testData,self.__strategyPlotData/self.__startingCapital))
            thread1.start()


        if(self.testMode==True):
            holder = self.__strategyPlotData
        else:
            self.__currentIndex = self.__currentIndex + 1
            holder = self.get_TOTALCAPITAL()/self.__startingCapital

        # Clear all data so it can be ran again
        self.__dict__ = self.__original_dict__
        self.__original_dict__ = copy.deepcopy(self.__dict__)


        return holder

    # helper function of runTest that plots data in a dash app
    def __plot(self, plot, dataloader, plotData):
        from testandtrade.strategyDashApp import Launch
        labels = []
        data = []
        dates = dataloader.data["Date"][:dataloader.data.shape[0]-1]
        if("All" in plot):
            for col in dataloader.data.columns:
                if(col!="Date"):
                    if(col=="High" or col=="Low" or col=="Open" or col=="Close"):
                        labels.append(col)
                        data.append(dataloader.data[col][:dataloader.data.shape[0]-1].values/dataloader.data["Open"][dataloader.data.shape[0]-2])
                    elif(col=="Volume"):
                        labels.append(col)
                        max=0
                        for x in range (0, dataloader.data.shape[0]-1):
                            if(dataloader.data["Volume"][x]>max):
                                max = dataloader.data[col][x]
                        out = dataloader.data["Volume"][:dataloader.data.shape[0]-1].values/max
                        for x in range(0,out.shape[0]):
                            out[x] = out[x]*dataloader.data["Open"][x]/dataloader.data["Open"][dataloader.data.shape[0]-2]
                        data.append(out)
                    else:
                        labels.append(col)
                        data.append(dataloader.data[col][:dataloader.data.shape[0]-1].values/dataloader.data["Open"][dataloader.data.shape[0]-2])

            labels.append("Strategy")
            data.append(plotData)
        else:
            for col in dataloader.data.columns:
                if col in plot:
                    if("Strategy"==col):
                        labels.append("Strategy")
                        data.append(plotData)
                    elif(col=="High" or col=="Low" or col=="Open" or col=="Close"):
                        labels.append(col)
                        data.append(dataloader.data[col][:dataloader.data.shape[0]-1].values/dataloader.data["Open"][dataloader.data.shape[0]-2])
                    elif(col=="Volume"):
                        labels.append(col)
                        max=0
                        for x in range (0, dataloader.data.shape[0]-1):
                            if(dataloader.data["Volume"][x]>max):
                                max = dataloader.data[col][x]
                        out = dataloader.data["Volume"][:dataloader.data.shape[0]-1].values/max
                        for x in range(0,out.shape[0]):
                            out[x] = out[x]*dataloader.data["Open"][x]/dataloader.data["Open"][dataloader.data.shape[0]-2]
                        data.append(out)
                    else:
                        labels.append(col)
                        data.append(dataloader.data[col][:dataloader.data.shape[0]-1].values/dataloader.data["Open"][dataloader.data.shape[0]-2])
        Launch(stratName = self.__stratName, labels = labels, data = data, dates = dates)

# The following are helper functions for runTest
    def __doYear(self,a=1):
        if(self.__testData.data["Date"][self.__currentIndex].year>self.__testData.data["Date"][self.__currentIndex+1].year):
            self.__currentFunction = "y"
            self.__everyYear(self)

    def __doMonth(self,a=1):
        if(self.__testData.data["Date"][self.__currentIndex].month>self.__testData.data["Date"][self.__currentIndex+1].month or self.__testData.data["Date"][self.__currentIndex].month<0.5*self.__testData.data["Date"][self.__currentIndex+1].month):
            self.__currentFunction = "m"
            self.__everyMonth(self)

    def __doWeek(self,a=1):
        if(self.__testData.data["Date"][self.__currentIndex].week>self.__testData.data["Date"][self.__currentIndex+1].week or self.__testData.data["Date"][self.__currentIndex].week<0.5*self.__testData.data["Date"][self.__currentIndex+1].week):
            self.__currentFunction = "w"
            self.__everyWeek(self)

    def __doDayOpen(self,a=1):
        self.__currentFunction = "do"
        self.__everyDayOpen(self)

    def __doDayClose(self,a=1):
        self.__currentFunction = "dc"
        self.__everyDayClose(self)

    # Carries out a buy order
    def buy(self, quantity):
        if(quantity>0):
            self.__currentStockPossition = self.__currentStockPossition + quantity
            if(self.__currentFunction=="dc"):
                self.__currentCapital = self.__currentCapital - quantity*self.__testData.data["Close"][self.__currentIndex]
            else:
                self.__currentCapital = self.__currentCapital - quantity*self.__testData.data["Open"][self.__currentIndex]

    # carries out a sell order
    def sell(self, quantity):
        if(quantity>0):
            self.__currentStockPossition = self.__currentStockPossition - quantity
            if(self.__currentFunction=="dc"):
                self.__currentCapital = self.__currentCapital + quantity*self.__testData.data["Close"][self.__currentIndex]
            else:
                self.__currentCapital = self.__currentCapital + quantity*self.__testData.data["Open"][self.__currentIndex]

    # returns liquid capital
    def get_AVALIABLECAPITAL(self):
        return self.__currentCapital

    # returns total value of the strat
    def get_TOTALCAPITAL(self):
        if(self.__currentFunction=="dc"):
            return float(self.__currentCapital+self.__currentStockPossition*self.__testData.data["Close"][self.__currentIndex])
        else:
            return float(self.__currentCapital+self.__currentStockPossition*self.__testData.data["Open"][self.__currentIndex])

    # returns quantity of stock held
    def get_STOCKCOUNT(self):
        return self.__currentStockPossition

    # returns data of the past n days
    def get_DATA(self,numberOfDays):
        if(self.__currentFunction=="dc"):
            if(self.__currentIndex+numberOfDays<self.__testData.data.shape[0]):
                out = self.__testData.data.iloc[self.__currentIndex:self.__currentIndex+numberOfDays ,:5]
            else:
                out = self.__testData.data.iloc[self.__currentIndex:self.__testData.data.shape[0] ,:5]
            out.index = range(out.shape[0])
            return out
        else:
            if(self.__currentIndex+numberOfDays<self.__testData.data.shape[0]):
                out = self.__testData.data.iloc[self.__currentIndex:self.__currentIndex+numberOfDays ,:5]
            else:
                out = self.__testData.data.iloc[self.__currentIndex:self.__testData.data.shape[0] ,:5]
            out = out.copy()
            out.index = range(out.shape[0])
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", message="")
                out.set_value(0,"High",None)
                out.set_value(0,"Low",None)
                out.set_value(0,"Close",None)
                out.set_value(0,"Volume",None)
            return out

    # def get_FUNDAMENTALS(self, amount):
    #     return self.__testData.get_FUNDAMENTALS(self.__currentIndex, amount)

















# the following functions return tecnical indicators for the datain dataloader
    def get_SMA(self,numberOfDays, type="Open"):
        try:
            if(self.__currentFunction!="dc"):
                if(type=="Open"):
                    return self.__testData.get_SMA(self.__currentIndex, numberOfDays, type)
                else:
                    return self.__testData.get_SMA(self.__currentIndex+1, numberOfDays, type)
            else:
                return self.__testData.get_SMA(self.__currentIndex, numberOfDays, type)
        except (KeyError, TypeError):
            raise ValueError("Check that type is a valid string and numberOfDays is an integer.")


    def get_EMA(self, numberOfDays, smoothing=2, type="Open"):
        try:
            if(self.__currentFunction!="dc"):
                if(type=="Open"):
                    return self.__testData.get_EMA(self.__currentIndex, numberOfDays, type, smoothing)
                else:
                    return self.__testData.get_EMA(self.__currentIndex+1, numberOfDays, type, smoothing)
            else:
                return self.__testData.get_EMA(self.__currentIndex, numberOfDays, type, smoothing)
        except (KeyError, TypeError):
            raise ValueError("Check that type is a valid string and smoothing is a float double or interger if you have provided a value for it and numberOfDays is an integer.")

    def get_WMA(self, numberOfDays, type="Open"):
        try:
            if(self.__currentFunction!="dc"):
                if(type=="Open"):
                    return self.__testData.get_WMA(self.__currentIndex, numberOfDays, type)
                else:
                    return self.__testData.get_WMA(self.__currentIndex+1, numberOfDays, type)
            else:
                return self.__testData.get_WMA(self.__currentIndex, numberOfDays, type)
        except (KeyError, TypeError):
            raise ValueError("Check that type is a valid string and numberOfDays is an integer.")

    def get_DEMA(self, numberOfDays, type="Open"):
        try:
            if(self.__currentFunction!="dc"):
                if(type=="Open"):
                    return self.__testData.get_DEMA(self.__currentIndex, numberOfDays, type)
                else:
                    return self.__testData.get_DEMA(self.__currentIndex+1, numberOfDays, type)
            else:
                return self.__testData.get_DEMA(self.__currentIndex, numberOfDays, type)
        except (KeyError, TypeError):
            raise ValueError("Check that type is a valid string and numberOfDays is an integer.")

    def get_TEMA(self, numberOfDays, type="Open"):
        try:
            if(self.__currentFunction!="dc"):
                if(type=="Open"):
                    return self.__testData.get_TEMA(self.__currentIndex, numberOfDays, type)
                else:
                    return self.__testData.get_TEMA(self.__currentIndex+1, numberOfDays, type)
            else:
                    return self.__testData.get_TEMA(self.__currentIndex, numberOfDays, type)
        except (KeyError, TypeError):
            raise ValueError("Check that type is a valid string and numberOfDays is an integer.")

    def get_TRIMA(self, numberOfDays, type="Open"):
        try:
            if(self.__currentFunction!="dc"):
                if(type=="Open"):
                    return self.__testData.get_TRIMA(self.__currentIndex, numberOfDays, type)
                else:
                    return self.__testData.get_TRIMA(self.__currentIndex+1, numberOfDays, type)
            else:
                return self.__testData.get_TRIMA(self.__currentIndex, numberOfDays, type)
        except (KeyError, TypeError):
            raise ValueError("Check that type is a valid string and numberOfDays is an integer.")

    # # todo
    #     def get_KAMA(self, numberOfDays):
    #         this = todo
    # # todo
    #     def get_MAMA(self, numberOfDays):
    #         this = todo

    def get_VWAP(self, numberOfDays, type="Open"):
        try:
            if(self.__currentFunction!="dc"):
                if(type=="Open"):
                    return self.__testData.get_VWAP(self.__currentIndex, numberOfDays, type)
                else:
                    return self.__testData.get_VWAP(self.__currentIndex+1, numberOfDays, type)
            else:
                return self.__testData.get_VWAP(self.__currentIndex, numberOfDays, type)
        except (KeyError, TypeError):
            raise ValueError("Check that type is a valid string and numberOfDays is an integer.")

    def get_MACD(self, type="Open"):
        try:
            if(self.__currentFunction!="dc"):
                if(type=="Open"):
                    return self.__testData.get_MACD(self.__currentIndex, type)
                else:
                    return self.__testData.get_MACD(self.__currentIndex+1, type)
            else:
                return self.__testData.get_MACD(self.__currentIndex, type)
        except (KeyError, TypeError):
            raise ValueError("Check that type is a valid string.")

    def get_MACDEXT(self, type="Open", funct="EMA", slow=26, fast=12):
        try:
            if(self.__currentFunction!="dc"):
                if(type=="Open"):
                    return self.__testData.get_MACDEXT(self.__currentIndex, type, funct, slow, fast)
                else:
                    return self.__testData.get_MACDEXT(self.__currentIndex+1, type, funct, slow, fast)
            else:
                return self.__testData.get_MACDEXT(self.__currentIndex, type, funct, slow, fast)
        except (KeyError, TypeError):
            raise ValueError("Check that type is a valid string and slow and fast are integers.")

    def get_STOCH(self, numberOfDays):
        if(self.__currentFunction!="dc"):
            return self.__testData.get_STOCH(self.__currentIndex+1)
        else:
            return self.__testData.get_STOCH(self.__currentIndex)

    def get_RSI(self, numberOfDays, type="Open"):
        try:
            if(self.__currentFunction!="dc"):
                if(type=="Open"):
                    return self.__testData.get_RSI(self.__currentIndex, numberOfDays, type)
                else:
                    return self.__testData.get_RSI(self.__currentIndex+1, numberOfDays, type)
            else:
                return self.__testData.get_RSI(self.__currentIndex, numberOfDays, type)
        except (KeyError, TypeError):
            raise ValueError("Check that type is a valid string and numberOfDays is an integer.")

    def get_STOCHRSI(self, numberOfDays, type="Open"):
        try:
            if(self.__currentFunction!="dc"):
                if(type=="Open"):
                    return self.__testData.get_STOCHRSI(self.__currentIndex, numberOfDays, type)
                else:
                    return self.__testData.get_STOCHRSI(self.__currentIndex+1, numberOfDays, type)
            else:
                return self.__testData.get_STOCHRSI(self.__currentIndex, numberOfDays, type)
        except (KeyError, TypeError):
            raise ValueError("Check that type is a valid string and numberOfDays is an integer.")

    def get_WILLR(self, numberOfDays):
        try:
            if(self.__currentFunction!="dc"):
                return self.__testData.get_WILLR(self.__currentIndex+1, numberOfDays)
            else:
                return self.__testData.get_WILLR(self.__currentIndex, numberOfDays)
        except (KeyError, TypeError):
            raise ValueError("Check that numberOfDays is an integer.")

    # # todo
    #     def get_ADX(self, numberOfDays, type="Open"):
    #         this = todo
    # # todo
    #     def get_ADXR(self, numberOfDays, type="Open"):
    #         this = todo

    def get_APO(self, fast, slow, type="Open"):
        try:
            if(self.__currentFunction!="dc"):
                if(type=="Open"):
                    return self.__testData.get_APO(self.__currentIndex, fast, slow, type)
                else:
                    return self.__testData.get_APO(self.__currentIndex+1, fast, slow, type)
            else:
                return self.__testData.get_APO(self.__currentIndex, fast, slow, type)
        except (KeyError, TypeError):
            raise ValueError("Check that fast and slow are integers and type is a valid string.")

    def get_PPO(self, type="Open"):
        try:
            if(self.__currentFunction!="dc"):
                if(type=="Open"):
                    return self.__testData.get_PPO(self.__currentIndex, type)
                else:
                    return self.__testData.get_PPO(self.__currentIndex+1, type)
            else:
                return self.__testData.get_PPO(self.__currentIndex, type)
        except (KeyError, TypeError):
            raise ValueError("Check that type is a valid string.")

    def get_MOM(self, numberOfDays, type="Open"):
        try:
            if(self.__currentFunction!="dc"):
                if(type=="Open"):
                    return self.__testData.get_MOM(self.__currentIndex, numberOfDays, type)
                else:
                    return self.__testData.get_MOM(self.__currentIndex+1, numberOfDays, type)
            else:
                return self.__testData.get_MOM(self.__currentIndex, numberOfDays, type)
        except (KeyError, TypeError):
            raise ValueError("Check that type is a valid string and numberOfDays is an integer.")

    def get_BOP(self, numberOfDays):
        try:
            if(self.__currentFunction!="dc"):
                return self.__testData.get_BOP(self.__currentIndex+1, numberOfDays)
            else:
                return self.__testData.get_BOP(self.__currentIndex, numberOfDays)
        except (KeyError, TypeError):
            raise ValueError("Check that numberOfDays is an integer.")

    def get_CCI(self, numberOfDays):
        try:
            if(self.__currentFunction!="dc"):
                return self.__testData.get_CCI(self.__currentIndex+1, numberOfDays)
            else:
                return self.__testData.get_CCI(self.__currentIndex, numberOfDays)
        except (KeyError, TypeError):
            raise ValueError("Check that numberOfDays is an integer.")

    def get_CMO(self, numberOfDays):
        try:
            if(self.__currentFunction!="dc"):
                return self.__testData.get_CMO(self.__currentIndex+1, numberOfDays)
            else:
                return self.__testData.get_CMO(self.__currentIndex, numberOfDays)
        except (KeyError, TypeError):
            raise ValueError("Check that numberOfDays is an integer.")

    def get_ROC(self, numberOfDays):
        try:
            if(self.__currentFunction!="dc"):
                return self.__testData.get_ROC(self.__currentIndex+1, numberOfDays)
            else:
                return self.__testData.get_ROC(self.__currentIndex, numberOfDays)
        except (KeyError, TypeError):
            raise ValueError("Check that numberOfDays is an integer.")

    # def __nthroot (self, N, K):
    #     # N,K = map(float,raw_input().split()) # We want Kth root of N
    #     lo = 0.0
    #     hi = N
    #     mid = (lo+hi)/2
    #     while 1:
    #         mid = (lo+hi)/2
    #         if math.fabs(mid**K-N) < 1e-9: # mid^K is really close to N, consider mid^K == N
    #             break
    #         elif mid**K < N: lo = mid
    #         else: hi = mid
    #     return mid
