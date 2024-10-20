import spacy
load_model = spacy.load('en_core_web_sm')

def text_processor(text):
    doc = load_model(text)
    lemmatized_text = [token.lemma_ for token in doc]
    stopwordFreeText = " ".join([ word if load_model.vocab[word].is_stop == False else "" for word in lemmatized_text])
    return stopwordFreeText
