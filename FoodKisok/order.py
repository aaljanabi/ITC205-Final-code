from menu import Menu
from orderdetail import OrderDetail
from payment import Payment

class Order():
    def __init__(self):
        self.orderdetails=[]

    def addOrderItems(self, orderdetail):
        self.orderdetails.append(orderdetail)

    def calcTotal(self):
        total=0.0
        for o in self.orderdetails:
            total += o.getMenuItem().menuitemprice * o.quantity
        payment=Payment(total,0.1 )
        return payment

    