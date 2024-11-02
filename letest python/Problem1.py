#(Q1) Write a program to print Twinkle Twinkle little star poem .
print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.''')


# (Q2)Install an external module and use it to perform an operation of your internal.
'''import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()'''
# (Q3) WAP to display an usr entered name followed by Good  Afternoon using input() function.
name = input("Enter your name: ")
print(f"Good Afternoon,{name}")
# (Q4) WAP to fill in a letter template given below with name and date.
letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Anjali").replace("<|Date|>", "27 june 1950"))
# (Q5) WAP to delete double space in a string.
name = "Anjali is a good student and"

print(name.find("  "))

# (Q6) WAP to format the following letter using escape sequence characters.
letter = "Dear Anjali,\n\t This python code is nice .\n thanks!"

print(letter)