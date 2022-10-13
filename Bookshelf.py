# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 17:49:48 2022

@author: PC_RC
"""

class Book:
    def __init__(self, name, author, release_date, price):
        self.book_name = name
        self.book_author = author
        self.book_release_date = release_date
        self.book_price = price
    
    def add_book(self):
        print("Name: " + self.book_name)
        print("Author: " + str(self.book_author))
        print("Release Date: " + self.book_release_date)
        print("Price: " + self.book_price)
        
        
        
book1 = Book("Geronimo Stilton and the Phoenix of Destiny", "Elizabetta Dami", "September 2013", "₹750")
book1.add_book() 

book2 = Book("Harry Potter and the Philosopher's Stone", "J.K Rowling", "June 1977", "₹1928")
book2.add_book() 