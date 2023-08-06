from model.measures.base import CountMeasure, DataMeasure, TimeMeasure, aggregatedMeasure, derivedMeasure
from model.computers.countComputer import countCompute
from model.computers.dataComputer import dataCompute
from model.computers.timeComputerGeneric import timeCompute
from model.computers.aggregatedComputer import aggregatedCompute
from model.computers.derivedComputer import derivedCompute

def measureComputer(measure, dataframe, id_case = 'case_concept_name', time_column = 'time_timestamp'):

    # Need to change ":" for "_" because ".query" put nervous with ":"
    dataframe.columns = [column.replace(":", "_") for column in dataframe.columns]

    # Evaluation wich kind of measure is
    if(type(measure) == CountMeasure):
        computer = countCompute(dataframe,measure, id_case)
    if(type(measure) == DataMeasure):
        computer = dataCompute(dataframe,measure, id_case)
    if(type(measure) == TimeMeasure):
        computer = timeCompute(dataframe,measure, id_case, time_column)
    if(type(measure) == aggregatedMeasure):
        computer = aggregatedCompute(dataframe, measure, id_case, time_column)
    if(type(measure) == derivedMeasure):
        computer = derivedCompute(dataframe, measure, id_case, time_column)
    return computer



