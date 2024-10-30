Custom NER Model for Address Parsing Using spaCy 

This project demonstrates how to train a custom Named Entity Recognition (NER) model using the spaCy library to extract address components from structured text. The NER model identifies specific entities such as Door Number, Street, Area, District, and Pincode from addresses.

Features
Custom NER Labels: The model detects five types of entities:
DOOR_NO – Identifies the door number.
STREET – Extracts the street name.
AREA – Recognizes the area or locality.
DISTRICT – Captures the district or city name.
PINCODE – Detects postal codes.
JSON-Based Training Data: Uses structured data in JSON format for training.
Model Storage and Reloading: After training, the model is saved and reloaded for testing.
Dataset
The training dataset used is provided in the merged_annotations.json file. Below is an example entry from the dataset:

json
Copy code
{
  "text": "121, Baker street, Broadway, Chennai- 600001",
  "entities": [
    {"start": 0, "end": 3, "label": "DOOR_NO"},
    {"start": 5, "end": 16, "label": "STREET"},
    {"start": 18, "end": 25, "label": "AREA"},
    {"start": 27, "end": 34, "label": "DISTRICT"},
    {"start": 36, "end": 42, "label": "PINCODE"}
  ]
}
Prerequisites
Make sure you have the following installed on your system:

Python 3.8 or above
pip for Python package management
Installation
Follow these steps to install the necessary dependencies:

Clone the repository:

bash
Copy code
git clone https://github.com/your-username/address-ner.git
cd address-ner
Install the required libraries:

bash
Copy code
pip install -r requirements.txt
Verify your installation by checking the version of spaCy:

bash
Copy code
python -c "import spacy; print(spacy.__version__)"
Requirements
The required Python packages are:

makefile
Copy code
spacy==3.5.0  # Adjust based on your installed version
Usage
Training the Model
Prepare your data: Ensure merged_annotations.json is placed in the same directory as your script.
Run the training script: This script loads the JSON file, processes the data, trains the model, and saves it to disk.
bash
Copy code
python train_model.py
Testing the Model
After training, the model is saved in the custom_ner_model/ directory. You can test the model with the following command:

bash
Copy code
python test_model.py
Example output:

Copy code
111 DOOR_NO
ABC Street STREET
Areaname AREA
Mumbai DISTRICT
100000 PINCODE
Project Structure
bash
Copy code
address-ner/
│
├── merged_annotations.json  # Training data
├── train_model.py           # Main training script
├── test_model.py            # Model testing script
├── requirements.txt         # Dependencies
├── README.md                # Project documentation
└── custom_ner_model/        # Folder to store the trained model
Train and Test Scripts
train_model.py:

Reads JSON data.
Converts it to spaCy's training format.
Trains the NER model.
Saves the model to custom_ner_model/.
test_model.py:

Loads the trained model.
Runs it on sample text to identify address entities.
Example Code Usage
train_model.py:

python
Copy code
import spacy
import json
from spacy.training import Example
import random

with open("merged_annotations.json", 'r') as f:
    data = json.load(f)

TRAIN_DATA = [(item['text'], {"entities": [(ent['start'], ent['end'], ent['label']) for ent in item['entities']]}) for item in data]

nlp = spacy.blank("en")
ner = nlp.add_pipe("ner")

for label in ["DOOR_NO", "STREET", "AREA", "DISTRICT", "PINCODE"]:
    ner.add_label(label)

optimizer = nlp.begin_training()

for epoch in range(20):
    random.shuffle(TRAIN_DATA)
    losses = {}
    for text, annotations in TRAIN_DATA:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], drop=0.5, losses=losses)
    print(f"Epoch {epoch + 1}, Loss: {losses}")

nlp.to_disk("custom_ner_model")
How to Contribute
Fork the repository.
Create a new branch for your feature or bug fix:
bash
Copy code
git checkout -b feature-name
Commit your changes:
bash
Copy code
git commit -m "Add feature name"
Push to your branch:
bash
Copy code
git push origin feature-name
Open a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
Your Name – GitHub Profile

