from menu import Menu
from orderdetail import OrderDetail
from order import Order
from payment import Payment

def main():

    selection1=Menu(1,'Grilled Salmon', 11.20)
    selection2=Menu(2,'Frensh Fries', 5.00) 
    selection3 =Menu(3,'Coke', 2.00) 
    

    orderdetail1=OrderDetail(selection1,1)
    orderdetail2=OrderDetail(selection2,2)
    orderdetail3=OrderDetail(selection3,1)

    order = Order()
    order.addOrderItems(orderdetail1)
    order.addOrderItems(orderdetail2)
    order.addOrderItems(orderdetail3)

    payment =order.calcTotal()
    print(payment)

main()