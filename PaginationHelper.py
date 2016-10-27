# TODO: complete this class
from math import ceil
class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  
  def __init__(self, collection, items_per_page):
            self.collection = collection
            self.items_per_page = items_per_page
           
              
  # returns the number of items within the entire collection
  def item_count(self):
      return len(self.collection)

      
  
  # returns the number of pages
  def page_count(self):
        return ceil(len(self.collection)/(self.items_per_page*1.0))
      
	
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
      lst = []
      if page_index >= ceil(len(self.collection)/(self.items_per_page*1.0)):
          return -1
      else:
          

          lst = [self.collection[i:i + self.items_per_page] for i in range(0, len(self.collection), self.items_per_page)]
          #a = list(zip(*[iter(self.collection)] * self.items_per_page))
          return (len(lst[page_index]))
          
      
      
  
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
      if item_index >=len(self.collection) :
          return -1
      if item_index < 0:
          return -1
      else:
          if int(item_index/(self.items_per_page*1.0)) != item_index/(self.items_per_page*1.0) :
              return ceil(item_index/(self.items_per_page*1.0))-1
          else:
              return ceil(item_index/(self.items_per_page*1.0))
  
