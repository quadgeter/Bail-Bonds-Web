import string


class Inmate:
    firstName: string
    lastName: string
    idNum: string
    courtDate: string
    bondAmount: float
    bondPaid: float
    charges: string
    contact: string
    
    def __init__(self):
        self.firstName = "firstName"
        self.lastName = "lastName"
        self.idNum = "ID"
        self.courtDate = "date"
        self.bondAmount = 0
        self.bondPaid = 0
        self.charges = "charges"
        self.contactName = "contactName"
        self.contactPhone = "contactPhone"
    
    def __init__(self, firstName='John', lastName='Doe', idNum="00000", courtDate='00/00/0000', bondAmount=0, bondPaid = 0, charges='', contactName="name", contactPhone="(980)-428-1459"):
        self.firstName = firstName
        self.lastName = lastName
        self.idNum = idNum
        self.courtDate = courtDate
        self.bondAmount = bondAmount
        self.bondPaid = bondPaid
        self.charges = charges
        self.contactName = contactName
        self.contactPhone = contactPhone
    
    def setFirstName(self, firstName):
        self.firstName = firstName
         
    def setLastName(self, lastName):
        self.lastName = lastName
        
    def setIdNum(self, idNum):
        self.idNum = idNum
        
    def setCourtDate(self, courtDate):
        self.courtDate = courtDate
    
    def setBondAmount(self, bondAmount):
        self.bondAmount = bondAmount
        
    def setBondPaid(self, bondPaid):
        self.bondPaid = bondPaid
    
    def setCharges(self, charges):
        self.charges = charges
        
    def setContactName(self, contactName):
        self.contactName = contactName
        
    def setContactPhone(self, contactPhone):
        self.contactPhone = contactPhone
        
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def getIdNum(self):
        return self.idNum
    
    def getCourtDate(self):
        return self.courtDate
    
    def getBondAmount(self):
        return self.bondAmount
    
    def getBondPaid(self):
        return self.bondPaid
    
    def getCharges(self):
        return self.charges
    
    def getContactName(self):
        return self.contactName
    
    def getContactPhone(self):
        return self.contactPhone
    
    def toString(self):
        return self.getFirstName() + ', ' + self.getLastName() + ', ' + self.getCourtDate() + ', $' + f'{self.getBondAmount():.2f}' + ', $' + f'{self.getBondPaid():.2f}' + ', ' + self.getCharges()
    
