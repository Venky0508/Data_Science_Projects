import pyttsx3
fr = pyttsx3.init()
speech = input("Say Something:")
# fr.say("You are dashing smart")
fr.say(speech)
fr.runAndWait()
