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
        
    def issued(self):
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
        if status in ["Yes", "No", "Discontinued"]:
            self.availability = status
        else:
            return "Enter valid status"
    
    def display_details(self):
        disply = Lit_detail.display(self)
        return disply + "    Book Title:" + str(self.title) + "    Book Author:" + str(self.author) + "    Book Genre:" + str(self.genre) + "    Book Year:" + str(self.year) + "    Number of Pages:" + str(self.pages) + "    Copies Available:" + str(self.copies)

class Periodical(Lit_detail):
    unique_count = 0
    total_count = 0
    
    def __init__(self, periodical_name, periodical_author, periodical_category, periodical_price, periodical_code, periodical_edition, periodical_copies):
        Lit_detail.__init__(self, periodical_name, periodical_author)
        self.category = periodical_category
        self.price = periodical_price
        self.availability = "Yes"
        self.copies = periodical_copies
        self.code = periodical_code
        self.edition = periodical_edition
        Periodical.unique_count += 1
        Periodical.total_count += periodical_copies
        
    def issued(self):
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
        if status in ["Yes", "No", "Discontinued"]:
            self.availability = status
        else:
            return "Enter valid status"
        
    def display_details(self):
        disply = Lit_detail.display(self)
        return disply + "    Category:" + str(self.category) + "    Edition:" + str(self.edition) + "    Copies Available:" + str(self.copies)








    
