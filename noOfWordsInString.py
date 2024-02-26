
def count(String):
    """"For Counting no. of words in a String"""
    words = String.split()
    return len(words)


String  = input("Enter your Para:")
print(count(String))