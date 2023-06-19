def numbers_strip(sample:"list", n = 1, copy = False)-> "list":
# Removes maximal and minimal numbers from a list and returns changed list
   max_val = max(sample)
   min_val = min(sample)
   
   while n:
       sample.remove(max_val)
       sample.remove(min_val)
       new_sample = sample.copy()
       n -= 1
       print(new_sample)
# Так и не понял как решить эту задачу(        
numbers_strip([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n = 3)