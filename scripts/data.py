
import os
import time

def pdfarticle2corpus(fname):
    '''Extract paragraphs as documents to create a corpus from an article

    Fx uses PyPDF2 data preprocessing so that the user can simply supply a 
      downloaded pdf article or review to create a corpus for training/inference

    Returns:
      corpus (pd.DataFrame)
    '''
    from PyPDF2 import PdfFileReader
    reader = PdfFileReader(fname)
    # reader.documentInfo # get title, publisher, etc.
    # reader.getPage(0).extractText # NOTE: this does not work well
    
    
    return None

if __name__ == '__main__':
    fname = '/home/ngr/gdrive/simpletopics/data/Guptaetal20.pdf'
    
