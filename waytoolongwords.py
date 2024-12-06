# Way Too Long Words 
## Get the words into a list
wordList = []
noOfWords = int(input())
while(noOfWords!=0):
    wordList.append(input())
    noOfWords-=1
## Do Operations on words 
for word in wordList:
    if(len(word) > 10):
        print(word[0] + str(len(word)-2) + word[len(word)-1])
    else:
        print(word)
