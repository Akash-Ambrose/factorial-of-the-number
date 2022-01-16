# n is used to get the user value
n = int(input("Enter a nmber to find the factorial of the number: "))
# variable (i) is used to stop the loop and used multiply with n 5*4,20*3.....
i = n-1

# if (i) is not equal to zero,The looping will start and stop when the i = 0.
while i!=0:  # if i ==0 ,The while loop will be skip and directly print the n value.
    
      n = n * i # n = 5 * 4 where n = 20 and stores the value in n,,again the continues n = 20 * 3 where n =60 ............................goes on until loop stops.
   
      i -=1 # i = i-1, is used to decrease the value of i to stop the loop
     
print ("The factorial of the given number is",n)# print the n value after the loop 
     
        
        
        
    