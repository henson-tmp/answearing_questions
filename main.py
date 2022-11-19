from transformers import pipeline
import wikipedia
import json

tokenizer = "henryk/bert-base-multilingual-cased-finetuned-polish-squad2"
model_name = "henryk/bert-base-multilingual-cased-finetuned-polish-squad2"

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
    output = ""
    q = q.split()
    if q[0] == "kim":
        output = q[2:]
        # we always del 2 first words if q starts with "kim"
    elif q[0] == "gdzie":
        if "się" in q:
            output = q[3:]
        else:
            output = q[2:]
    elif q[0] == "ile" or q == "ilu":
        if "na" in q or "w" in q or "podczas" in q:
            output = q[4:]
        else:
            output = q[2:]
    elif q[0] == "co":
        if "że" in q or "iż" in q:
            output = q[3:]
        else:
            output = q[2:]
    elif q[0] == "kiedy":
        if "był" in q or "został" in q or "się" in q:
            output = q[3:]
        else:
            output = q[2:]
    elif q[0] == "jak":
        output = q[2:]
    elif q[0] == "kto":
        output = q[2:]

    return output

question = input("Question: ").lower()

search = get_subject(question)
print(search)
context = get_wiki_text(search)

model = pipeline("question-answering",model=model_name,tokenizer=tokenizer)

output = model({'context': context,'question': question})
print(output)






