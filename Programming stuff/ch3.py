#LISTS
#A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0–9, or the names of all the people in your family. You can put anything you want into a list, andthe items in your list don’t have to be related in any particular way. 
c = "a"
w = "xy123"
bicycles = ["123", 1, 2, 3, "Abcd", c, w]
print(bicycles)

#You can also use the string methods from Chapter 2 on any element in this list.
print(bicycles[6].upper())
#Python considers the first item in a list to be at position 0, not position 1.
#index -1 is used to obtain the last element of the list. The index - 2 returns the second item from the end of the list, the index - 3 returns the third item from the end, and so forth.
print(bicycles[-1])