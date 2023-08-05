from PPINot4Py import timeGrouper, dataframeImporter
from PPINot4Py.computer import measureComputer
from PPINot4Py import computer
from PPINot4Py.state import DataObjectState
from PPINot4Py.condition import Condition
from PPINot4Py.measures import base

def auxiliarLinearTimeMeasure(fromCondition, ToCondition, firstTo = False, precondition = '' ):
    
    countStateTimeA = DataObjectState.DataObjectState(fromCondition)
    countConditionTimeA = Condition.TimeInstantCondition(countStateTimeA)
    countMeasureTimeA = base.CountMeasure(countConditionTimeA)
        
    countStateTimeC = DataObjectState.DataObjectState(ToCondition)
    countConditionTimeC = Condition.TimeInstantCondition(countStateTimeC)
    countMeasureTimeC = base.CountMeasure(countConditionTimeC)
        
    timeMeasureLinearA = base.TimeMeasure(countMeasureTimeA, countMeasureTimeC)
    
    return timeMeasureLinearA