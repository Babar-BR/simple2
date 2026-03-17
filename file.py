import pyttsx3

engine = pyttsx3.init()

a = 10
b = 20
result = a + b
print("modifed the code here")

print("Result is", result)
engine.say(f"Result is {result}")
engine.runAndWait()