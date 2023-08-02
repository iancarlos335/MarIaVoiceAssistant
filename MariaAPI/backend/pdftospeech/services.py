import PyPDF2
import pdfplumber
import pyttsx3


def encode(filepath):
    pdf_reader = PyPDF2.PdfReader(filepath)
    pages = len(pdf_reader.pages)
    speaker = pyttsx3.init()
    file_text = ""
    with pdfplumber.open(filepath) as pdf:
        for i in range(0, pages):
            page = pdf_reader.pages[i]
            text = page.extract_text()
            file_text += text

    speaker.save_to_file(file_text, f'public/static/audios/audio_transcribed.mp3')
    speaker.runAndWait()