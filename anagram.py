# Two words said tobe anagrams if they have same letters

def anagram(s1,s2):
    """"Fucntion to check if two words are anagrams or not"""
    word1 = sorted(s1);
    word2 = sorted(s2);
    return word1.lower()==word2.lower()
    

print(anagram("silent","listen"))