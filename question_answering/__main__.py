import yaml
from transformers import pipeline
import wikipedia
import spacy

with open("../config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

QA_MODEL = pipeline(
    "question-answering",
    model=config["model_name"],
    tokenizer=config["tokenizer"])
POS_MODEL = spacy.load(config["lang_model"])
wikipedia.set_lang(config["lang"])


def get_wiki_text(name: str) -> str:
    prop_article = wikipedia.search(name)[0]
    try:
        article = wikipedia.page(prop_article)
    except wikipedia.exceptions.DisambiguationError as e:
        # if there name may refer to more than one articles pick the first one
        article = wikipedia.page(e.options)
        print(e.options)
    print("Article title ", article.title)
    return article.content


def get_subject(question: str) -> str:
    """Extracts a proper name from input text"""
    doc = POS_MODEL(question)
    return " ".join([token.text for token in doc if token.pos_ in ["PROPN"]])


def main():
    while True:
        question = input("Question: ")

        search = get_subject(question)
        context = get_wiki_text(search)

        output = QA_MODEL({'context': context, 'question': question})
        print(output)


if __name__ == "__main__":
    main()
