from model.condition.conditionChooser import conditionChooser
import pandas as pd
from model import measureComputer
import datetime
import numpy as np

def derivedCompute(dataframe, condition, id_case, time_column):
    
    function = condition.functionExpression
    measureMap = condition.measureMap
    dataFrameComputer = pd.DataFrame()
    istime = False
    
    for key in measureMap:  
        dataFrameComputer[key] = pd.Series(measureComputer.measureComputer(measureMap[key], dataframe)['data'])
        
        if(dataFrameComputer[key].dtype == 'timedelta64[ns]'):
            dataFrameComputer[key] = dataFrameComputer[key].dt.total_seconds()
            dataFrameComputer[key] = dataFrameComputer[key].fillna(0).astype(float)
            istime = True
  
    evaluated_dataframe = dataFrameComputer.eval(function)
    evaluated_dataframe_noInfinites = evaluated_dataframe.replace([np.inf, -np.inf], 0)
    finalResult = evaluated_dataframe_noInfinites.fillna(0).astype(float)
    
    if(istime == True):
        finalResult = finalResult.apply(lambda x: datetime.timedelta(seconds = x))
    
    return finalResult

  
