import speech_recognition as sr

# Setup the voice recognition
r = sr.Recognizer()

# Setup microphone for enabling speech
mic = sr.Microphone()

try: 
  with mic as source3:
    r.adjust_for_ambient_noise(source3, duration=0.5)
    audio3 = r.listen(source3)
  print(r.recognize_google(audio3))
except sr.UnknownValueError:
  print('This was hard to understand')

