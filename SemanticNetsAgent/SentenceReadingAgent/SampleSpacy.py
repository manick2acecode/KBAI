import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

# Example sentence
sentence_2 = "David and Lucy walk one mile to go to school every day at 8:00AM when there is no snow."

# Process the sentence with SpaCy
doc = nlp(sentence_2)

# Function to find the answer to a question
def answer_question(question):
    if question == "Who does Lucy go to school with?":
        for token in doc:
            if token.text == "Lucy":
                # Find conjunctions (cc) or conjuncts (conj)
                for child in token.children:
                    if child.dep_ == "cc" or child.dep_ == "conj":
                        return f"Lucy goes to school with {child.text}."
    elif question == "Where do David and Lucy go?":
        for token in doc:
            if token.lemma_ == "go" and token.dep_ == "xcomp":
                for child in token.children:
                    if child.dep_ == "prep":
                        for obj in child.children:
                            if obj.dep_ == "pobj":
                                return f"David and Lucy go to {obj.text}."
    elif question == "How far do David and Lucy walk?":
        for token in doc:
            if token.lemma_ == "walk":
                for child in token.children:
                    if child.dep_ == "nummod" or child.dep_ == "npadvmod":
                        return f"David and Lucy walk {child.text} {child.head.text}."
    elif question == "How do David and Lucy get to school?":
        for token in doc:
            if token.lemma_ == "walk":
                return f"David and Lucy get to school by {token.lemma_}ing."
    elif question == "At what time do David and Lucy walk to school?":
        for token in doc:
            if token.dep_ == "prep" and token.head.lemma_ == "walk":
                for child in token.children:
                    if child.dep_ == "pobj" and child.ent_type_ == "TIME":
                        return f"David and Lucy walk to school at {child.text}."
    return "Sorry, I don't know the answer to that question."

# Questions
questions = [
    "Who does Lucy go to school with?",
    "Where do David and Lucy go?",
    "How far do David and Lucy walk?",
    "How do David and Lucy get to school?",
    "At what time do David and Lucy walk to school?"
]

# Answer the questions
for question in questions:
    answer = answer_question(question)
    print(question)
    print(answer)
    print()
