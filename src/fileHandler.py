from pdf2jpg import pdf2jpg
from extractText import extractText
from textProcessor import text_processor
from textToGraph import draw_graph
import re


def handleFile(file):
    if file.name.split('.')[-1] == 'pdf':
        images = pdf2jpg(file.read())
        print("PDF to JPG :: Done")

        text = extractText(images)
        print("JPG to TXT :: Done")

        clean_text = re.sub(r'[^\w\s]', ' ', text)
        print("Text formatting :: Done")

        processed_text = text_processor(clean_text.lower())
        print("Text processing :: Done")

        graph = draw_graph(processed_text)
    
    return graph