
class NonIntegerError(Exception):
    def __init__(self, usr_input):
        print("Error info:", usr_input, "is not a valid entry.")

class IncorrectDataTypeError(Exception):
    def __init__(self, usr_input):
        print("Error info:", usr_input, "has data type:", type(usr_input).__name__)

class Transaction_Operation:
    def __init__(self, quantity):
        self.quantity = quantity

    def sold(self, quan):
        try:
            if type(quan) != int:
                raise(IncorrectDataTypeError(quan))
            elif type(quan) == int and quan>=0:
                if quan <= self.quantity:
                    self.quantity -= quan
                else:
                    return "Not Enough Quantity Available"
            else:
                raise(NonIntegerError(quan))
        except IncorrectDataTypeError:
            return "Enter an integer value for quantity sold."
        except NonIntegerError:
            return "Enter a positive integer number for quantity sold."
    
    def purchase_cost(self, quan):
        try:
            if type(quan) != int:
                raise(IncorrectDataTypeError(quan))
            elif type(quan) == int and quan>=0:
                return self.price*quan
            else:
                raise(NonIntegerError(quan))
        except IncorrectDataTypeError:
            return "Enter an integer value to check purchasing cost."
        except NonIntegerError:
            return "Enter a positive integer number for checking purchasing cost."
    
    def returned(self, quan):
        try:
            if type(quan) != int:
                raise(IncorrectDataTypeError(quan))
            elif type(quan) == int and quan>=0:
                self.quantity += quan
            else:
                raise(NonIntegerError(quan))
        except IncorrectDataTypeError:
            return "Enter an integer value for returned quantity."
        except NonIntegerError:
            return "Enter a positive integer number for returned quantity."
    
    def add(self, quan):
        try:
            if type(quan) != int:
                raise(IncorrectDataTypeError(quan))
            elif type(quan) == int and quan>=0:
                self.quantity += quan
            else:
                raise(NonIntegerError(quan))
        except IncorrectDataTypeError:
            return "Enter an integer value for quantity added to Inventory."
        except NonIntegerError:
            return "Enter a positive integer number for quantity added to Inventory."
        
class Pen(Transaction_Operation):
    def __init__(self, pen_color, pen_type, pen_brand, pen_price, pen_avail_quan):
        try:
            if type(pen_avail_quan) != int:
                raise(IncorrectDataTypeError(pen_avail_quan))
            elif type(pen_avail_quan) == int and pen_avail_quan>=0:
                Transaction_Operation.__init__(self, pen_avail_quan)
                self.color = pen_color
                self.type = pen_type
                self.brand = pen_brand
                self.price = pen_price
                self.ok = True
            else:
                raise(NonIntegerError(pen_avail_quan))
        except IncorrectDataTypeError:
            print("Enter an integer value for available pen quantity.")
            self.ok = None
            return None
        except NonIntegerError:
            print("Enter a positive integer number for available pen quantity.")
            self.ok = None
            return None
                
    def validate_object(self):
        return self.ok
    
    def display_details(self):
        return "Pen Color:" + str(self.color) + "    Pen Type:" +  str(self.type) + "    Pen Brand:" + str(self.brand) + "    Pen Price:" + str(self.price)
        
class Pencil(Transaction_Operation):
    def __init__(self, pencil_color, pencil_type, pencil_thickness, pencil_brand, pencil_price, pencil_avail_quan):
        try:
            if type(pencil_avail_quan) != int:
                raise(IncorrectDataTypeError(pencil_avail_quan))
            elif type(pencil_avail_quan) == int and pencil_avail_quan>=0:
                Transaction_Operation.__init__(self, pencil_avail_quan)
                self.color = pencil_color
                self.type = pencil_type
                self.brand = pencil_brand
                self.thickness = pencil_thickness
                self.price = pencil_price
                self.ok = True
            else:
                raise(NonIntegerError(pencil_avail_quan))
        except IncorrectDataTypeError:
            print("Enter an integer value for available pencil quantity.")
            self.ok = None
            return None
        except NonIntegerError:
            print("Enter a positive integer number for available pencil quantity.")
            self.ok = None
            return None
            
    def validate_object(self):
        return self.ok
    
    def display_details(self):
        return "Pencil Color:" + str(self.color) + "    Pencil Type:" + str(self.type) + "    Pencil Thickness:" +  str(self.thickness) + "    Pencil Brand:" + str(self.brand) + "    Pencil Price:" + str(self.price)
        
class Notebook(Transaction_Operation):
    def __init__(self, notebook_size, notebook_pages, notebook_brand, notebook_price, notebook_avail_quan):
        try:
            if type(notebook_avail_quan) != int:
                raise(IncorrectDataTypeError(notebook_avail_quan))
            elif type(notebook_avail_quan) == int and notebook_avail_quan>=0:
                Transaction_Operation.__init__(self, notebook_avail_quan)
                self.size = notebook_size
                self.pages = notebook_pages
                self.brand = notebook_brand
                self.price = notebook_price
                self.ok = True
            else:
                raise(NonIntegerError(notebook_avail_quan))
        except IncorrectDataTypeError:
            print("Enter an integer value for available notebook quantity.")
            self.ok = None
            return None
        except NonIntegerError:
            print("Enter a positive integer number for available notebook quantity.")
            self.ok = None
            return None
        
    def validate_object(self):
        return self.ok
    
    def display_details(self):
        return "Page Size" + str(self.size) + "    Number of Pages:" + str(self.pages) + "    Notebook Brand:" + str(self.brand) + "    Notebook Price:" + str(self.price)       
    