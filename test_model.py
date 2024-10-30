import spacy

# Load the trained model
nlp = spacy.load("custom_ner_model")

# Test the model with sample text
test_text = "111, ABC Street, Kodambakkam , Chennai, 100000"
doc = nlp(test_text)

# Display the detected entities
print("Detected Entities:")
for ent in doc.ents:
    print(f"{ent.text} -> {ent.label_}")
