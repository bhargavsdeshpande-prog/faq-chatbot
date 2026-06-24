import json
import string
import nltk

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')

# Load FAQ data
with open("faq_data.json", "r") as file:
    faqs = json.load(file)

questions = [faq["question"] for faq in faqs]
answers = [faq["answer"] for faq in faqs]

# Text preprocessing
def preprocess(text):
    text = text.lower()

    for p in string.punctuation:
        text = text.replace(p, " ")

    tokens = text.split()

    stop_words = set(stopwords.words('english'))

    tokens = [word for word in tokens if word not in stop_words]

    return " ".join(tokens)

# Process questions
processed_questions = [preprocess(q) for q in questions]

# TF-IDF
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)

# Response function
def get_response(user_query):
    processed_query = preprocess(user_query)

    query_vector = vectorizer.transform([processed_query])

    similarities = cosine_similarity(query_vector, faq_vectors)

    best_match_index = similarities.argmax()

    confidence = similarities[0][best_match_index]

    if confidence > 0.2:
        return answers[best_match_index]
    else:
        return "Sorry, I could not understand your question."

# Chat loop
if __name__ == "__main__":
    print("FAQ Chatbot")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        print("Chatbot:", get_response(user_input))