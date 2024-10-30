import spacy
import json
from spacy.training import Example
import random

# Load the annotated data from the JSON file
with open("merged_annotations.json", 'r') as f:
    data = json.load(f)

# Prepare the data for training
TRAIN_DATA = [
    (item['text'], {"entities": [(ent['start'], ent['end'], ent['label']) for ent in item['entities']]})
    for item in data
]

# Create a blank English model
nlp = spacy.blank("en")

# Add the NER component to the pipeline
ner = nlp.add_pipe("ner")

# Add custom labels to the NER component
for label in ["DOOR_NO", "STREET", "AREA", "DISTRICT", "PINCODE"]:
    ner.add_label(label)

# Start the training process
optimizer = nlp.begin_training()

# Train the model
for epoch in range(20):  # Adjust epochs if needed
    random.shuffle(TRAIN_DATA)
    losses = {}
    
    for text, annotations in TRAIN_DATA:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], drop=0.5, losses=losses)

    print(f"Epoch {epoch + 1}, Loss: {losses}")

# Save the trained model
nlp.to_disk("custom_ner_model")
print("Model training completed and saved to 'custom_ner_model' directory.")
