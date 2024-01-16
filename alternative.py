
#********pseudo code********
#This program will read 2 strings and change the and make each alternate letter
#into upper case 
# The program will first read the string and check the length of string
# Than for loop is used to manage the iteration of string length
# if condition is used in the loop body to check if index of string%2 is equal to zero
# than cahnge the letter of that into lower case
# if condtion is false than elif wil performed and it will change the same index letter 
# into upper case 
# After mainpulation code will join the string and print the results on screen
# program have two blocks for each string ,both perform same function
# one is used to change the letter of string and 2nd will change the word of string



# intialize the string
string = "Hello World"
#create empty list to store the results
new_str = []
# len function is used to check length of string to iterate the loop
check = len(string)
# for loop will iterate according to the number of string length
for i in range(check):
    
    # if will check is index of string is equal to zero , if condition true control will
    #enter into body
    if (i+1)%2 == 0:
        
        #the letter on index of i variable will change into lower case by usin lowe function
        # and append will appaend that letter into list
         new_str.append(string[i].lower())
    
    #elif will exectute if index of string%2 not equal to zero
    elif (i+1)%2 != 0:
        #the letter on index of i variable will change into upper case by using upper function
        # and append will appaend that letter into list
        new_str.append(string[i].upper())
        
        
# join fuction is used to join the letter of list
join = " ".join(new_str)
#print function will display the final results 
print(join)


# intialize the list 
my_string = ["i", "am", "learning", "to", "code"]

#for loop will iterate according to the word in list and enumerate function will help to catch the index 
# #and line variable will access the words of list
for i, line in enumerate(my_string):
    
    #if will check is index of string is equal to zero , if condition true control will
    #enter into body
    if (i+1)%2 == 0:
        #the letter on index of i variable will change into upper case by usin upper function
        # and append will appaend that letter into list
        my_string[i]=line.upper()
        
    elif (i+1)%2 !=0:
        #the letter on index of i variable will change into lower case by usin lower function
        # and append will appaend that letter into list
        my_string[i]=line.lower()
  
# join fuction is used to join the letter of list      
join_stirng = " ".join(my_string)

#print function will display the final results 
print(join_stirng)