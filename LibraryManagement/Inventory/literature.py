
class StatusUpdateError(Exception):
    def __init__(self, status):
        print("Error info:", status, "is not a valid status. Enter either Yes, No or Discontinued")

class NonIntegerError(Exception):
    def __init__(self, usr_input):
        print("Error info:", usr_input, "is not a valid entry.")

class IncorrectDataTypeError(Exception):
    def __init__(self, usr_input):
        print("Error info:", usr_input, "has data type:", type(usr_input).__name__)

class Lit_detail:
    def __init__(self, lit_name, lit_author):
        self.title = lit_name
        self.author = lit_author
    
    def display(self):
        return "Title:" + str(self.title) + "    Author:" + str(self.author)
        
class Book(Lit_detail):     
    unique_count = 0
    total_count = 0
    
    def __init__(self, book_name, book_author, book_genre, book_price, book_pages, book_code, book_year, book_copies):
        try:
            if type(book_copies) != int:
                raise(IncorrectDataTypeError(book_copies))
            elif (type(book_copies) == int) and (book_copies>0):
                Lit_detail.__init__(self, book_name, book_author)
                self.genre = book_genre
                self.price = book_price
                self.pages = book_pages
                self.availability = "Yes"
                self.copies = book_copies
                self.code = book_code
                self.year = book_year
                Book.unique_count += 1
                Book.total_count += book_copies
                self.ok = True
            else:
                raise(NonIntegerError(book_copies))
        except IncorrectDataTypeError:
            print("Enter an integer value for book copies.")
            self.ok = None
            return None
        except NonIntegerError:
            print("Enter a positive integer number for book copies.")
            self.ok = None
            return None
                
    def validate_object(self):
        return self.ok
    
    def issued(self):
        if type(self.copies) == int and self.copies>=0:
            if self.availability != "Discontinued":
                if self.copies > 0:
                    self.copies -= 1
                    if self.copies == 0:
                        self.availability = "No"
                else:
                    return "Book not available in library"
                
            else:
                return "Book is discontinued"
        
    def returned(self):
        if type(self.copies) == int and self.copies>=0:
            if self.copies == 0:
                self.availability = "Yes"
            self.copies += 1

        
    def get_status(self):
        if self.availability == "Yes":
            return "Available"
        elif self.availability == "No":
            return "Not Available"
        else:
            return "Discontinued"
        
    def update_status(self, status):
        try:
            if status in ["Yes", "No", "Discontinued"]:
                self.availability = status
            else:
                raise(StatusUpdateError(status))
        except StatusUpdateError:
            return "Book Status Not Updated"
    
    def display_details(self):
        disply = Lit_detail.display(self)
        return disply + "    Book Title:" + str(self.title) + "    Book Author:" + str(self.author) + "    Book Genre:" + str(self.genre) + "    Book Year:" + str(self.year) + "    Number of Pages:" + str(self.pages) + "    Copies Available:" + str(self.copies)

class Periodical(Lit_detail):
    unique_count = 0
    total_count = 0
    
    def __init__(self, periodical_name, periodical_author, periodical_category, periodical_price, periodical_code, periodical_edition, periodical_copies):
        try:
            if type(periodical_copies) != int:
                raise(IncorrectDataTypeError(periodical_copies))
            elif type(periodical_copies) == int and periodical_copies>0:
                Lit_detail.__init__(self, periodical_name, periodical_author)
                self.category = periodical_category
                self.price = periodical_price
                self.availability = "Yes"
                self.copies = periodical_copies
                self.code = periodical_code
                self.edition = periodical_edition
                Periodical.unique_count += 1
                Periodical.total_count += periodical_copies
                self.ok = True
            else:
                raise(NonIntegerError(periodical_copies))
        except IncorrectDataTypeError:
            print("Enter an integer value for periodical copies.")
            self.ok = None
            return None
        except NonIntegerError:
            print("Enter a positive integer number for periodical copies.")
            self.ok = None
            return None
        
    def validate_object(self):
        return self.ok
    
    def issued(self):
        if type(self.copies) == int and self.copies>=0:
            if self.availability != "Discontinued":
                if self.copies > 0:
                    self.copies -= 1
                    if self.copies == 0:
                        self.availability = "No"
                else:
                    return "Periodical not available in Library"
            else:
                return "Periodical is discontinued"
            
    def returned(self):
        if type(self.copies) == int and self.copies>=0:
            if self.copies == 0:
                self.availability = "Yes"
            self.copies += 1

        
    def get_status(self):
        if self.availability == "Yes":
            return "Available"
        elif self.availability == "No":
            return "Not Available"
        else:
            return "Discontinued"

    def update_status(self, status):
        try:
            if status in ["Yes", "No", "Discontinued"]:
                self.availability = status
            else:
                raise(StatusUpdateError(status))
        except StatusUpdateError:
            return "Periodical Status Not Updated"
            
    def display_details(self):
        disply = Lit_detail.display(self)
        return disply + "    Category:" + str(self.category) + "    Edition:" + str(self.edition) + "    Copies Available:" + str(self.copies)








    
