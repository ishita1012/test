vowels=['a','e','i','o','u']
word=input("Provide a word to search for vowels: ")
found={}
found['a'], found['e'], found['i'], found['o'], found['u']=0,0,0,0,0
for letter in word:
    if letter in vowels:
        found.setdefault(letter,0)
        found[letter]+=1            
for vowel in found:
    print(vowel," appears ",found[vowel], "time(s)")
    
