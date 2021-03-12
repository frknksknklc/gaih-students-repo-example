"""
Create two lists. The first list should consist of odd numbers. The second list is also is even numbers.
Merge these two lists. Multiply all values in the new list by 2.
Use a loop to print data type of the all values in the new list 
"""

list1 = [1,3,5,7,9]
list2 = [2,4,6,8,10]
mergelist = list1 + list2
print(mergelist)
doublemergelist = [i*5 for i in mergelist]
print(doublemergelist)
datatypes = [print(type(item)) for item in doublemergelist]
