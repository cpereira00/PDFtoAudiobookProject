import PyPDF2
import pyttsx3
import sys


def words_per_minute():

    WPM = int(input(
        f"How many words per minute(WPM) do you want the PDF to be read at (recommended 160-200): "))
    speaker.setProperty('rate', WPM)


def replay():

    choice = input("Would you like to read more pages? Yes or No: ").lower()
    return choice == 'yes'


print('Welcome to your personal PDF to AudioBook Converter! \n')


# replace "Proposal" with any PDF, and make sure pdf is within project folder OR provide full file path
try:
    engine = open(str(sys.argv[1]), 'rb')
except:
    print("Invalid file name")
    exit()


reader = PyPDF2.PdfFileReader(engine)
page_count = reader.numPages
print(f'The number of pages is: {page_count-1}')

speaker = pyttsx3.init()

while True:
    print(f"If you want the entire PDF to be read, type 'entire'. Otherwise type 'other' for more options and 'leave' to terminate.")
    pagesToRead = input('Your Choice: ').lower()

    if pagesToRead == 'entire':

        words_per_minute()

        for num in range(0, page_count):
            page = reader.getPage(num)
            words = page.extractText()
            speaker.say(words)
            speaker.runAndWait()

    elif pagesToRead == 'other':

        print('\n*If you want only 1 page to be read, enter that page. '
              '\n*If you want a range of pages to be read, enter the first page number followed by a space then the last page number.')

        try:
            inp = list(map(int, input('Your Choice: ').split()))

            if inp[0] < 0 or inp[1] > page_count:
                print(
                    "Sorry, these pages don't exist as they are not within the book.")
                continue

            words_per_minute()

            for num in range(inp[0], inp[1]+1):
                page = reader.getPage(num)
                words = page.extractText()
                speaker.say(words)
                speaker.runAndWait()
        except:

            page = reader.getPage(inp[0])
            words = page.extractText()
            speaker.say(words)
            speaker.runAndWait()

    elif pagesToRead == 'leave':
        break

    else:
        print('Oops, invalid input, try again. \n')
        continue

    if not replay():
        break

    print('Program Terminating, have a nice day!')
