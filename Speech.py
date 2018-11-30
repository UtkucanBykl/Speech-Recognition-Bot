import speech_recognition as sr

class Speech():

    def __init__(self, file = ""):
        self.r = sr.Recognizer()
        self._file = file

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, value):
        self._file = value


    def to_text(self):
        harvard = sr.AudioFile(self._file)
        print(self.file + "******" * 100)
        with harvard as source:
            audio = self.r.record(source)
            print(audio)
        return self.r.recognize_google(audio, language="tr_TR")
