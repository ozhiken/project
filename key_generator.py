import random  
import string  
 
def WithoutRepeat(length):  
    letters = string.ascii_uppercase 
    result1 = ''.join((random.sample(letters, length)))   
    print(" Random generated string without repetition: ", result1)  
  
WithoutRepeat(26)  