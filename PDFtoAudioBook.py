import PyPDF2
import pyttsx3

#replace "Proposal" with any PDF
engine = open('Proposal.pdf', 'rb')
reader = PyPDF2.PdfFileReader(engine)
page_count = reader.numPages
print(f'number of pages is: {page_count-1}')

speaker = pyttsx3.init()
speaker.setProperty('rate', 180)


print(f" Type 'entire' if you want the entire pdf to be read. Otherwise type the page number you want read")
pagesToRead = input('Your Choice: ')

if pagesToRead == 'entire':

    for num in range(0, page_count):
        page = reader.getPage(num)
        words = page.extractText()
        speaker.say(words)
        speaker.runAndWait()

elif int(pagesToRead) >= page_count:
    raise Exception("Sorry that page number is not within the book, program terminating!")

else:
    page = reader.getPage(int(pagesToRead))
    words = page.extractText()
    speaker.say(words)
    speaker.runAndWait()
