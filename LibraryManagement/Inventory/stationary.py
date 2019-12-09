class Transaction_Operation:
    def __init__(self, quantity):
        self.quantity = quantity

    def sold(self, quan):
        if quan <= self.quantity:
            self.quantity -= quan
        else:
            return "Not Enough Quantity Available"
    
    def purchase_cost(self, quan):
        return self.price*quan
    
    def returned(self, quan):
        self.quantity += quan
    
    def add(self, quan):
        self.quantity += quan
        
class Pen(Transaction_Operation):
    def __init__(self, pen_color, pen_type, pen_brand, pen_price, pen_avail_quan):
        Transaction_Operation.__init__(self, pen_avail_quan)
        self.color = pen_color
        self.type = pen_type
        self.brand = pen_brand
        self.price = pen_price
             
    def display_details(self):
        return "Pen Color:" + str(self.color) + "    Pen Type:" +  str(self.type) + "    Pen Brand:" + str(self.brand) + "    Pen Price:" + str(self.price)
        
class Pencil(Transaction_Operation):
    def __init__(self, pencil_color, pencil_type, pencil_thickness, pencil_brand, pencil_price, pencil_avail_quan):
        Transaction_Operation.__init__(self, pencil_avail_quan)
        self.color = pencil_color
        self.type = pencil_type
        self.brand = pencil_brand
        self.thickness = pencil_thickness
        self.price = pencil_price
            
    def display_details(self):
        return "Pencil Color:" + str(self.color) + "    Pencil Type:" + str(self.type) + "    Pencil Thickness:" +  str(self.thickness) + "    Pencil Brand:" + str(self.brand) + "    Pencil Price:" + str(self.price)
        
class Notebook(Transaction_Operation):
    def __init__(self, notebook_size, notebook_pages, notebook_brand, notebook_price, notebook_avail_quan):
        Transaction_Operation.__init__(self, notebook_avail_quan)
        self.size = notebook_size
        self.pages = notebook_pages
        self.brand = notebook_brand
        self.price = notebook_price
        
    def display_details(self):
        return "Page Size" + str(self.size) + "    Number of Pages:" + str(self.pages) + "    Notebook Brand:" + str(self.brand) + "    Notebook Price:" + str(self.price)       
    