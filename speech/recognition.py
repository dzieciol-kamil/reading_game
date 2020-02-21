import time

import speech_recognition as sr


class Recognition:
    r = sr.Recognizer()
    m = sr.Microphone()

    def __init__(self):
        print("A moment of silence, please...")
        with self.m as source: self.r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(self.r.energy_threshold))

    def get_response(self):
        time1 = time.time()
        audio = self.listen()
        time2 = time.time()
        try:
            return self.recognize(audio, (time2 - time1))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
            return None, "Nie udało się przetworzyć.", 0
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            exit(1)

    def listen(self):
        with self.m as source: audio = self.r.listen(source)
        print("Got it! Now to recognize it...")
        return audio

    def recognize(self, audio, time):
        # recognize speech using Google Speech Recognition
        value = self.r.recognize_google(audio, language="pl-PL")
        print("You said {}".format(value))
        return "{}".format(value).lower(), None, time
