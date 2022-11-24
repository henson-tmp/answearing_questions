import yaml
from transformers import pipeline
import wikipedia
import spacy

with open("../config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
tokenizer = config["tokenizer"]
model_name = config["model_name"]
nlp = spacy.load(config["lang_model"])

def get_wiki_text(name):
    wikipedia.set_lang("pl")
    prop_article = wikipedia.search(name)[0]
    try:
        article = wikipedia.page(prop_article)
    except wikipedia.exceptions.DisambiguationError as e:
        article = wikipedia.page(e.options) #if there name may refer to more than one articles pick the first one
        print(e.options)
    print("Article title ",article.title)
    return article.content

def get_subject(q):
    doc = nlp(q)

    return " ".join([token.text for token in doc if token.pos_ in ["PROPN"]])

def main_loop():
    while True:
        question = input("Question: ")

        search = get_subject(question)
        print(search)
        context = get_wiki_text(search)

        model = pipeline("question-answering",model=model_name,tokenizer=tokenizer)

        output = model({'context': context,'question': question})
        print(output)

main_loop()

if __name__ == "__main__":
    main_loop()






