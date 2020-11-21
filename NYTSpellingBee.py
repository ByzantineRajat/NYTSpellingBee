import os
validWords = []
candidateWords = []


letterList = input("Enter the 7 letters of the puzzle starting with the center letter : ")
centerLetter = letterList[0]


f = open("/Users/rajatgururaj/Documents/words_alpha.txt", "r") # Download words_alpha.txt (The English Dictionary) and set the correct path in your system
lines = f.read().splitlines()



for i in lines:
    if len(i) >= 4 :
        validWords.append(i)

# print("Number of Valid words are : " + str(len(validWords)))


for word in validWords :
    match = 0
    if centerLetter in word:
        for letter in word :
            if (letter == letterList[0]) or (letter == letterList[1]) or (letter == letterList[2]) or (letter == letterList[3]) or (letter == letterList[4]) or (letter == letterList[5]) or (letter == letterList[6]):
               match +=1
                
    if match == len(word):
        candidateWords.append(word)


print("the number of potential words is : " + str(len(candidateWords)))
print (candidateWords)

            




