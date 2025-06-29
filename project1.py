import spacy
from heapq import nlargest

def summarize_text(text, summary_length=3):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    word_freq = {}
    for token in doc:
        if token.is_alpha and not token.is_stop:
            word = token.text.lower()
            word_freq[word] = word_freq.get(word, 0) + 1

    sentence_scores = {}
    for sent in doc.sents:
        for word in sent:
            if word.text.lower() in word_freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_freq[word.text.lower()]

    summary_sentences = nlargest(summary_length, sentence_scores, key=sentence_scores.get)
    summary = " ".join([sent.text for sent in summary_sentences])
    return summary

if _name_ == "_main_":
    long_text = """In recent years, the global conversation around climate change has intensified, driven by increasingly frequent extreme weather events, rising sea levels, and growing scientific consensus about the human impact on the environment. Governments, corporations, and individuals are being urged to take immediate and meaningful action to reduce carbon emissions and transition to more sustainable practices. Renewable energy sources such as solar, wind, and hydroelectric power are gaining traction as viable alternatives to fossil fuels, while innovations in electric vehicles and energy-efficient technologies are reshaping industries. However, the path to a greener future is fraught with challenges, including political resistance, economic constraints, and the need for widespread behavioral change. Education and awareness play a crucial role in mobilizing public support and encouraging environmentally responsible choices. At the same time, international cooperation is essential, as climate change knows no borders and requires a unified global response. The urgency of the situation has led to the emergence of youth-led climate movements, demanding accountability and long-term thinking from world leaders. As the world grapples with the consequences of decades of environmental neglect, the choices made today will determine the health and stability of the planet for generations to come.


"""
    print("Original Text:\n", long_text)
    print("\nSummary:\n", summarize_text(long_text))
