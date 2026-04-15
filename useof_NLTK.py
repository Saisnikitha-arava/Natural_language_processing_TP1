!pip install nltk spacy
import nltk
import spacy
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
!python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")
text = "Natural Language Processing is a part of Artificial Intelligence."
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
print("Tokens:", tokens)
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("Filtered Tokens:", filtered_tokens)
pos_tags = nltk.pos_tag(tokens)
print("POS Tags:", pos_tags)
doc = nlp(text)
print("\nspaCy Tokens and POS Tags:")
for token in doc:
 print(token.text, "->", token.pos_)
