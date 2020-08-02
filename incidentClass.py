from datetime import datetime
class incident:
    
    def __init__(self, startDate,endDate):
        self.startDate = startDate
        self.endDate = endDate
        self.incident = incident

    def getDiff(self):
        date1 = self.startDate
        date2 = self.endDate
        
        date1Aux = datetime.strptime(date1, '%m/%d/%y %H:%M:%S')
        date2Aux = datetime.strptime(date2, '%m/%d/%y %H:%M:%S')
        if date1Aux > date2Aux:
          result = date1Aux - date2Aux
        else:
          return 0
        return result


 
        
