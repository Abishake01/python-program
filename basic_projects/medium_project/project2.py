#Story madlibs Generator
with open('story.txt','r') as f:
    story=f.read()

#words=[]
words=set()
start_of_word=-1
target_start='<'
target_end='>'

for i, char in enumerate(story):
    if char==target_start:
        start_of_word=i
    if char==target_end and start_of_word!=-1:
        word=story[start_of_word:i+1]
        words.add(word)#words.append(word)--> It give a duplicate value
        start_of_word=-1
answers={}

for word in words:
    answer=input('Enter a Word For '+word+': ')
    answers[word]=answer
    
for word in words:
    story=story.replace(word,answers[word])
    
print(story)