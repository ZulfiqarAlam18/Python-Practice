#String => Set of characters , they could be of one character , one word or multiple words(complelte para)

name = "Zulfiqar Alam"
bio = "I am student of software Engineer muet jamshoro"

#lenght of any string
print(len(name))

#Concatination

print(name+bio)

#indexing in String 

print(name[1]) #output u
print(bio[0])  

#slicing : Accessing some part of String
print(name[1:4]) 
print (name[:4])
print (name[4:])
print (name[2:len(name)])

# negative indexing in python along with slicing
fruit = "Umbrella"
print(fruit[-2:-1])