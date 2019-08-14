class Menu():
    def __init__(self, menuitemnum, menuitemname, menuitemprice):
        self.menuitemnum=menuitemnum
        self.menuitemname=menuitemname
        self.menuitemprice=menuitemprice

    def getMenuItemNumber(self):
        return self.menuitemnum

    def getMenuItemName(self):
        return self.menuitemname
    
    def getMenuItemPrice(self):
        return self.menuitemprice
    
    def __str__(self):
        return self.menuitemname