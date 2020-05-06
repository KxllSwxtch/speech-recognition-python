import time
import random
import speech_recognition as sr

def read_mic_speech(recognizer, microphone):
  if not isinstance(recognizer, sr.Recognizer):
    raise TypeError('recognizer must be an instance of speech_recognition.Recognizer')
  
  if not isinstance(microphone, sr.Microphone):
    raise TypeError('microphone must be an instance of speech_recognition.Microphone')

  with microphone as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

  response = {
    'success': True,
    'error': None,
    'transcription': None
  }

  try:
    response['transcription'] = recognizer.recognize_google(audio)
  except sr.RequestError:
    response['success'] = False
    response['error'] = 'Unreachable API'
  except sr.UnknownValueError:
    response['error'] = "Input message wasn't clear"
    
  return response

if __name__ == '__main__':
  words = ['Apple', 'Mango', 'Banana', 'Apricot', 'Programming', 'Car']
  n_guesses = 3
  n_limit = 5

  correct_answer = random.choice(words)

  recognizer = sr.Recognizer()
  microphone = sr.Microphone()

  instructions = 'I am thinking of one of these words: {}\nYou have {} number of guesses'.format(words, n_guesses)
  print(instructions)
  time.sleep(3)

  for i in range(n_guesses):
    for j in range(n_limit):
      print('Guess {}. Speak!'.format(i+1))
      guess = read_mic_speech(recognizer, microphone)
      if guess['transcription']:
        break
      if not guess['success']:
        break
      print ('I didnt catch it, can you please repeat?')

    if guess['error']:
      print('ERROR: {}'.format(guess['error']))

    print('You said {}'.format(guess['transcription']))

    is_correct_guess = guess['transcription'].lower() == correct_answer.lower()
    has_more_attempts = i < n_guesses - 1

    if is_correct_guess:
      print('Correct! You Win!')
      break
    elif has_more_attempts:
      print('Incorrect, please try again...')
    else:
      print("You lost! Maybe next time...")

