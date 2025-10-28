# Tokenize and Perform sentimetn analysis on the text using NLTK or spaCy
# Venkat, 27-10-2025
# Process input -> tokenize -> senti analyze -> save,

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, sent_tokenize

text = """
China has completed the construction of 36 hardened aircraft shelters, new administrative blocks, and a new apron at its Lhunze airbase in Tibet, about 40 kilometres north of the McMahon line - the boundary between India and China in the Arunachal Pradesh region.

The construction of the new hardened shelters at Lhunze, about 107 kilometres from the strategic town of Tawang in Arunachal Pradesh, gives China the option of forward-deploying fighter aircraft and a host of drone systems in its arsenal and reduces the response time needed for the Indian Air Force to respond to any airborne threat from its own airbases across Arunachal Pradesh and Assam.
"""

# WORD TOK
word_tokens = word_tokenize(text)
print("--- Word Tokenization ---")
print(f"Original Text: {text}")
print(f"Word Tokens: {word_tokens}")
print("-" * 30)

# Sentence Tok
sentence_tokens = sent_tokenize(text)
print("--- Sentence Tokenization ---")
print(f"Sentence Tokens: {sentence_tokens}")
print("-" * 30)

#Sentiment Analysis (using VADER)

sid = SentimentIntensityAnalyzer()

print("--- Overall Sentiment Analysis (VADER) ----")
sentiment_scores = sid.polarity_scores(text)
print(f"Sentiment Scores: {sentiment_scores}")

# Lets Interpret the scores
compound_score = sentiment_scores['compound']

if compound_score >= 0.05:
    sentiment_label = "Positive"
elif compound_score <= -0.05:
    sentiment_label = "Negative"
else:
    sentiment_label = "Neutral"

print(f"\nFinal Sentiment Label (based on Compound Score {compound_score}): {sentiment_label}")
print("-" * 30)

# Analysis by Sentence
print("--- Sentiment Analysis Per Sentence ---")
for sentence in sentence_tokens:
    sentence_scores = sid.polarity_scores(sentence)
    compound_score = sentence_scores['compound']
    
    if compound_score >= 0.05:
        label = "Positive"
    elif compound_score <= -0.05:
        label = "Negative"
    else:
        label = "Neutral"
        
    print(f"Sentence: '{sentence}'")
    print(f"  Scores: {sentence_scores} -> {label}")
