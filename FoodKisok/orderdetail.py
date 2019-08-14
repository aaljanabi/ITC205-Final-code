from menu import Menu

class OrderDetail():
    def __init__(self, menu, quantity):
        self.menu=menu
        self.quantity=quantity
        #self.items=[]

    def getMenuItem(self):
        return self.menu
    
    def getQuantity(self):
        return self.quantity
    
    """ def addItem(self, i):
        self.items.append(i)
    
    def getItemByNumber(self, number):
        reqItem=None
        for i in self.items:
            if i.itemnum==number:
                reqItem=i
                break
        return reqItem """