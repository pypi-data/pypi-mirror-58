import json
import os
import sys
import time
import unittest
from pm4py.objects.log.adapters.pandas import csv_import_adapter
from measureComputer import measureComputer
from condition.Condition import TimeInstantCondition
from state.RunTimeState import DataObjectState
from measures.base import CountMeasure, DataMeasure, aggregatedMeasure, TimeMeasure, derivedMeasure
from timeGrouper import grouper
from pm4py.objects.log.importer.xes import factory as xes_import_factory
from pm4py.objects.log.exporter.csv import factory as csv_exporter

# Creating the .csv in case is the first time we run the program
if(os.path.exists("log_in_csv.csv") == False):
    log = xes_import_factory.apply('bpi_challenge_2013_incidents.xes')
    csv_exporter.export(log, "log_in_csv.csv")

# Loading .csv in dataframe
dataframe = csv_import_adapter.import_dataframe_from_path(os.path.join("log_in_csv.csv"))

# Need to change ":" for "_" because ".query" put nervous with ":"
dataframe.columns = [column.replace(":", "_") for column in dataframe.columns]

# Data measure used
countState = DataObjectState("concept_name == 'Queued'")
countCondition = TimeInstantCondition(countState)
countMeasure = CountMeasure(countCondition)
dataMeasure = DataMeasure("lifecycle_transition", countMeasure, False)

# Time measure used 
#(fromCondition, toCondition,  timeMeasureType = 'Linear', singleInstanceAggFunction = 'SUM', firstTo = 'False', precondition = '')

countStateTimeA = DataObjectState('lifecycle_transition == "In Progress"')
countConditionTimeA = TimeInstantCondition(countStateTimeA)
countMeasureTimeA = CountMeasure(countConditionTimeA)

countStateTimeB = DataObjectState('lifecycle_transition == "Closed"')
countConditionTimeB = TimeInstantCondition(countStateTimeB)
countMeasureTimeB = CountMeasure(countConditionTimeB)

countStateTimeC = DataObjectState('lifecycle_transition == "Awaiting Assignment"')
countConditionTimeC = TimeInstantCondition(countStateTimeC)
countMeasureTimeC = CountMeasure(countConditionTimeC)


timeMeasureLinearA = TimeMeasure(countMeasureTimeA, countMeasureTimeB)
timeMeasureLinearB = TimeMeasure(countMeasureTimeB, countMeasureTimeA)
timeMeasureLinearC = TimeMeasure(countMeasureTimeA, countMeasureTimeC)

timeMeasureCyclic = TimeMeasure(countMeasureTimeA, countMeasureTimeB, 'CYCLIC', 'SUM')
timeMeasureCyclicMax = TimeMeasure(countMeasureTimeA, countMeasureTimeB, 'CYCLIC', 'MAX')
timeMeasureCyclicMin = TimeMeasure(countMeasureTimeA, countMeasureTimeB, 'CYCLIC', 'MIN')
timeMeasureCyclicAvg = TimeMeasure(countMeasureTimeA, countMeasureTimeB, 'CYCLIC', 'AVG')

#baseMeasure = measureComputer(timeMeasureLinear, dataframe)
timeGrouper = grouper('60s')
aggregatedMeasure60s = aggregatedMeasure(timeMeasureLinearA, '', 'SUM', timeGrouper)

timeGrouper2W = grouper('2W')
aggregatedMeasure2W = aggregatedMeasure(timeMeasureLinearA, '', 'SUM', timeGrouper2W)

measure_dictionary = {'ProgressCount': timeMeasureLinearA, 'ClosedCount': timeMeasureLinearB, 'AwwaitingCount': timeMeasureLinearC}

#measure_dictionary = {'ProgressCount': countMeasureTimeA, 'ClosedCount': countMeasureTimeB, 'AwwaitingCount': countMeasureTimeC}

derivedMeasure = derivedMeasure('(ProgressCount + ClosedCount) / sqrt(AwwaitingCount)', measure_dictionary)


class MyTest(unittest.TestCase):
    def testTimeMeasureCyclicSum(self):
        self.assertEqual(measureComputer(timeMeasureCyclic, dataframe).size, 4904)
    def testTimeMeasureCyclicMax(self):
        self.assertEqual(measureComputer(timeMeasureCyclicMax, dataframe).size, 4904)
    def testTimeMeasureCyclicMin(self):
        self.assertEqual(measureComputer(timeMeasureCyclicMin, dataframe).size, 4904)
    def testTimeMeasureCyclicAvg(self):
        self.assertEqual(measureComputer(timeMeasureCyclicAvg, dataframe).size, 4904)
        
    def testTimeMeasureLinearA_B(self):
        self.assertEqual(measureComputer(timeMeasureLinearA, dataframe).size, 4904)
    def testTimeMeasureLinearB_A(self):
        self.assertEqual(measureComputer(timeMeasureLinearB, dataframe).size, 6)
    def testTimeMeasureLinearA_C(self):
        self.assertEqual(measureComputer(timeMeasureLinearC, dataframe).size, 3619)
        
    def testDataMeasureFirstFalse(self):
        self.assertEqual(measureComputer(dataMeasure, dataframe).size, 4511)  
        
    def testCountMeasure(self):
        self.assertEqual(measureComputer(countMeasureTimeA, dataframe).size, 7554)
        
    def testAggregatedMesure2W(self):
        self.assertEqual(measureComputer(aggregatedMeasure2W, dataframe).size, 3)
    def testAggregatedMesure60s(self):
        self.assertEqual(measureComputer(aggregatedMeasure60s, dataframe).size, 31285)

    def testDerivatedMeasure(self):
        self.assertEqual(measureComputer(derivedMeasure, dataframe).size, 4904)

if __name__ == "__main__":
    unittest.main()

