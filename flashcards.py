#!/usr/bin/python3 -OO
'''
Display flashcards from PDF definitions file
'''
import sys, os, logging
from glob import glob
from PyPDF2 import PdfFileReader

logging.basicConfig(level=logging.DEBUG if __debug__ else logging.INFO)

def flashcards(front_first=False, front_time=1, rear_time=3, fileglob=None):
    '''
    Read in all files and display flashcards from the contents.

    Files must be in a specific format, with a bolded word or phrase,
    followed by a colon, followed by the definition.

    For example:

    Negligence: Negligence is found where a duty is owed to the plaintiff,
    that duty has been breached, and the plaintiff has as a result suffered
    damages.

    From the above, in its default configuration, flashcards will show
    the definition of negligence for 3 seconds, then the word Negligence
    for 1 second. Then the program will end. It will combine any number
    of files into one list, and display each word-definition pair randomly.
    '''
    pages = []
    for filename in glob(os.path.expanduser(fileglob)):
        infile = PdfFileReader(filename)
        for page in range(infile.getNumPages()):
            pages.append(infile.getPage(page).extractText())
    logging.debug('%d pages found.', len(pages))
    for page in pages:
        print(repr(page))

if __name__ == '__main__':
    flashcards(*sys.argv[1:])
