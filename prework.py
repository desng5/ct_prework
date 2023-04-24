#question_1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(username):
    print("Hello, " + username.title() + "!")
hello_name('ampowers')


#question_2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

print("Odd numbers 1 - 100:")
for x in range(1,100+1):
    if x % 2 == 1:
        print(x)


#question_3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    max = a_list[ 0 ]  
    for a in a_list:  
        if a > max:  
            max = a  
    return max  
print(max_num_in_list([-5, 0, 5, 10]))


#question_4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):

    if a_year % 4 == 0:
        print("True")
    
    elif a_year % 100 == 0:
        print("False")
    
    elif a_year % 400 == 0:
        print("True")
    
    return a_year

is_leap_year(2016)


#question_5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
  sorted_list = a_list[:]
  sorted_list.sort()
  compare_list = [sorted_list[0]]
  for num in range(sorted_list[0], len(sorted_list)):
    compare_list.append(num+1)
  if compare_list == sorted_list:
    return True
  else:
    return False