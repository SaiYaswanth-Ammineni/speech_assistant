from speech_recognition import Microphone,Recognizer,RequestError,UnknownValueError
from googlesearch import search

r=Recognizer()
def record_audio():
    with Microphone() as source:

        audio = r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except UnknownValueError:
            print('sorry,i did not get you')
        # Unknownvale value error occurs if speech recognition is not able to understand audio
        except RequestError:
            print('speech service is not good')
        #Request error occurs if there is problem in speech recognition module
        return voice_data

def respond(voice_data):
    if 'print' in voice_data:
        print('what you what to print')
        stat =record_audio()
        print('you said '+stat)
    if 'links' in voice_data:
        print('what you want to search for')
        query = record_audio()
        for l in search(query, tld='co.in',num=5,stop=5,pause=2.0):
            print(l)

    if 'exit' in voice_data:
        print('exit')
        exit()
a=1
while a:
    a=0

    print('what you want to do ')
    print('if print what you said, say print')
    print('if search for links for what you said say links')
    print('if you want to exit say exit')
    voice_data=record_audio()
    respond(voice_data)
    a=int(input('if you want to try again enter 1,else 0\n a:'))