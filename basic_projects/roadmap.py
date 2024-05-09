name=input('Gemini:What is Your Name\nUser: ')
area=input('Gemini:Where are you right now?\nUser: ')
print("Welcome ",name,'You Are in the ',area)
place=['Hospital,Theater,School,Ground']
print(place)
move=input('Gemini:Which Place You want to go\nUser:')

if move.lower()=='hospital':
    print('Gemini:Go Straight 50m, Your left side is Hospital')
    user=input('User:')
elif move.lower()=='theater':
    print('Gemini:Turn left side walk few meters, you see the theater in Your right side')
    user=input('User:')
elif move.lower()=='school':
    print('Gemini:Turn left go straight 200m ,You cross the Theater walk ...Turn Your right side and go 40m. You reach the School')
    user=input('User:')
elif move.lower()=='ground':
    print('Gemini:Turn left go straight 200m ,You cross the Theater walk ...Turn Your right side walk 100m. You cross the school go staright your left side are the Ground')
    user=input('User:')
else:
    print('Please Choose Given Place...Not Find Your place')
print('Thanks For Using Gemini...')