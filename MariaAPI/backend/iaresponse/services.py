import pdfplumber
import pyttsx3
import PyPDF2
import pydub
import boto3
from pydub import playback

pdfReader = PyPDF2.PdfReader("C:\\Users\\ianca\\Downloads\\Ética e Legislação em Tecnologia Notas de Aula.pdf")
pages = len(pdfReader.pages)
speaker = pyttsx3.init()
fileText = ""
with pdfplumber.open('C:\\Users\\ianca\\Downloads\\Ética e Legislação em Tecnologia Notas de Aula.pdf') as pdf:
    for i in range(0, pages):
        page = pdfReader.pages[i]
        text = page.extract_text()
        fileText += "\n" + text

# polly = boto3.client('polly', region_name="us-west-2")
# response = polly.synthesize_speech(
#     Text=fileText,
#     OutputFormat='mp3',
#     VoiceId='Salli',
#     Engine='neural')
#
# with open("response.mp3", 'wb') as f:
#     f.write(response['AudioStream'].read())

sound = pydub.AudioSegment.from_file('response.mp3',
                                     format="mp3")
playback.play(sound)
