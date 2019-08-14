class Payment():
    def __init__(self, paymentamount, taxpercentage):
        self.paymentamount=paymentamount
        self.taxamount=paymentamount*taxpercentage
    
    def __str__(self):
        self.paymentamount=round(self.paymentamount,2)
        self.taxamount=round(self.taxamount, 2)
        response="Amount                        : " + str(self.paymentamount) + " $" + '\n' + "Tax                           : " + str(self.taxamount) + " $" +'\n' + "The total amount with tax     : "  + str(self.paymentamount+self.taxamount) + " $"
        return response

    def __str__(self):
        self.paymentamount=round(self.paymentamount,2)
        response="Payment Amount: " + str(self.paymentamount) 
        return response