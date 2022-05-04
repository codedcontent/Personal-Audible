import pyttsx3
import PyPDF2
from tkinter.filedialog import *


def main():
    book = askopenfilename()
    pdf_reader = PyPDF2.PdfFileReader(book)
    pages = pdf_reader.numPages

    for num in range(1, pages):
        page = pdf_reader.getPage(num)
        text = page.extractText()
        player = pyttsx3.init()
        player.say(text)
        player.runAndWait()


if __name__ == '__main__':
    main()
