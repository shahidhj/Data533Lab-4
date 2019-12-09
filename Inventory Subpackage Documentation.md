# DATA533-LibraryManagement
## Inventory Subpackage Documentation


__INVENTORY SUB-PACKAGE__:

__LITERATURE MODULE__:

__LIT DETAIL__ class is the base class for the literature module.

__LIT ATTRIBUTES__:
Title: Title of the literature.
Author :Author of the literature

__LIT METHODS__:
Display: Display the corresponding attributes of the LIT class.

BOOK CLASS:

__BOOK CLASS ATTRIBUTES__:
Unique Count:Counts the total number of unique books.
Total Counts:Counts all the copies of all the books.

__BOOK ATTRIBUTES__:
Book Name: Title of the book 
Book Author: Author of the book
Book Genre: Genre of the book
Book Price: Cost of book
Book Pages: Number of pages in book
Book Code: Unique code for each book
Book Year: Publication year of book
Book Copies: Number of copies of book with library

__BOOK METHODS__:
issued(): keeps a track of number of copies of a book issued to members
returned(): keeps a track of number of copies of book returned to library
get_status(): gives status of book: “Available”, “Not Available”, “Discontinued”
update_status(): updates status of the book
display_details(): displays details of a book like its title, author, genre, price, pages and copies available

__PERIODICAL CLASS ATTRIBUTES__:
Unique Counts:Counts to total number of unique periodicals
Total Counts:Counts all the copies of all the periodsicals.

__PERIODICAL ATTRIBUTES__:
Periodical Name: Title of the Periodical 
Periodical Author: Author of the Periodical
Periodical Category: category of the Periodical
Periodical Price: Cost of Periodical
Periodical Code: Unique code for each Periodical
Periodical Edition: Edition of Periodical (YYYY_MM)
Periodical Copies: Number of copies of Periodical with library


__PERIODICAL METHODS__:
issued(): keeps a track of number of copies of a Periodical issued to members
returned(): keeps a track of number of copies of Periodical returned to library
get_status(): gives status of Periodical: “Available”, “Not Available”, “Discontinued”
update_status(): updates status of the Periodical
display_details(): displays details of a Periodical like its title, author, category, edition and copies available

__STATIONARY MODULE__:

Transaction Operation is the base class for PEN,PENCIL and NOTEBOOK classes.
__Transaction Opearation __:

__TRANSACTION OPERATION ATTRIBUTES__:
Quantity:Quantity of either Pen,pencil or notebook.

__TRANSACTION OPERATION METHODS__:
Sold: Number of items sold for either pen,pencil or notebook.
Purchase cost: Shows the cost of the item chose that is of a pen,pencil or notebook.
Returned : When the product is returned , a value is added back to the inventory
Add :To stock up the inventory.

__PEN ATTRIBUTES__:
Pen Color: Color of pen, eg. “blue”, “black”
Pen Type: Type of pen, eg. “gel”, “ball”
Pen Brand: Pen manufacturer company
Pen Price: Cost of each pen

__PEN METHODS__:
display_details(): prints information on various attributes of pen like color, type, brand and price

__PENCIL ATTRIBUTES__:
Pencil Color: Color of Pencil, eg. “blue”, “black”
Pencil Type: Type of Pencil, eg. “HB”, “HB6”
Pencil Thickness: Pencil lead thickness
Pencil Brand: Pencil manufacturer company
Pencil Price: Cost of each Pencil

PENCIL METHODS:
display_details(): prints information on various attributes of Pencil like color, type, thickness, brand and price

__NOTEBOOK ATTRIBUTES__:
Notebook Size: Size of page of notebook
Notebook Pages: Number of pages in notebook
Notebook Brand: Notebook manufacturer company
Notebook Price: Cost of each Notebook

__NOTEBOOK METHODS__:
display_details(): prints information on various attributes of Notebook like page size, number of pages,  brand and price



