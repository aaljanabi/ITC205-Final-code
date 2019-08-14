import unittest
from menu import Menu
from orderdetail import OrderDetail
from order import Order
from payment import Payment


class MenuTest(unittest.TestCase):
    def setUp(self):
        self.menu=Menu(1,'new meal', 12.95)

    def test_menuString(self):
        self.assertEqual(str(self.menu),self.menu.menuitemname)

    def test_getMenuPrice(self):
        self.assertEqual(str(self.menu.getMenuItemPrice()), '12.95')

    def test_getMenuItemNumber(self):
        self.assertEqual(str(self.menu.getMenuItemNumber()),'1')



class OrderdetailTest(unittest.TestCase):
    def setUp(self):
        self.menu=Menu(2,'salad', 2.75)
        self.quantity=2 
        self.orderdetail=OrderDetail(self.menu, self.quantity)

    def test_getMenuItem(self):
        self.menu = self.orderdetail.getMenuItem()
        self.assertEqual(str(self.menu),'salad')  

    def test_geMenutItemPriceFromOrderItem(self):
        self.menu = self.orderdetail.getMenuItem()
        self.assertEqual(self.menu.getMenuItemPrice(), 2.75)

    def test_getQuantity(self):
        self.assertEqual(self.orderdetail.getQuantity(),2)


#not passed
class OrderTest(unittest.TestCase):

    def setUp(self):
       self.o=Order()
       self.menuitem1=Menu(3,'cheese stick', 2.10)
       self.menuitem2=Menu(42,'dessert', 10.00)

       self.orderitem1=OrderDetail(self.menuitem1,1)
       self.orderitem2=OrderDetail(self.menuitem2,3)
       #self.orderitem3=OrderDetail(self.menuitem3,2)

       
       self.o.addOrderItems(self.orderitem1)
       self.o.addOrderItems(self.orderitem2)
       #self.o.addOrderItems(self.orderitem3)


    #not passed
    def test_CalculateTotal(self):
        payment=self.o.calcTotal()
        self.assertEqual(str(payment), 'Payment Amount: 32.1')
   