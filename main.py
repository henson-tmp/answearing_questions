from transformers import pipeline
import wikipedia
import json


def get_wiki_text(name):
    wikipedia.set_lang("pl")
    prop_article = wikipedia.search(name)[0]
    try:
        article = wikipedia.page(prop_article)
    except wikipedia.exceptions.DisambiguationError as e:
        article = wikipedia.page(e.options) #if there name may refer to more than one articles pick the first one
    return article.content



question = input("Question: (About Obama)")
context = get_wiki_text("Obama")


model = pipeline(
    "question-answering",
    model="henryk/bert-base-multilingual-cased-finetuned-polish-squad2",
    tokenizer="henryk/bert-base-multilingual-cased-finetuned-polish-squad2"
)
output = model({'context': context,'question': question})
print(output)






