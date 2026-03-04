def salesAnalysis():
    value = 0
    day = 0
    myfile = open('Sales.txt','r')
    for line in myfile:
        value = value + float(line)
        day = day + 1
    PeriodAverage = value/day

    value = round(value,2)
    PeriodAverage = round(PeriodAverage,2)
    print('The total sales over the' + str(day), 'days was ' +str(value))
    print('The average daily sales was ' + str(PeriodAverage))
salesAnalysis()
    
