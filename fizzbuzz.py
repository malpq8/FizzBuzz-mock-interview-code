#Python program that prints the numbers from 1 to 100.
#For multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
#For numbers which are multiples of both three and five print “FizzBuzz

for fizzbuzz in range(100):  
  
    
    if fizzbuzz % 3 == 0:  
        print("Fizz")                                          
        continue
  
    
    elif fizzbuzz % 5 == 0:      
        print("Buzz")                                          
        continue
  
    #multiple of both 5 and 3
    elif fizzbuzz % 15 == 0:          
        print("FizzBuzz")                                      
        continue
  
   
    print(fizzbuzz) 
