# Address Parsing Model 🚀  

This project trains a custom NER model using **spaCy** to extract address components like Door Number, Street, Area, and more.  

## Features  
- Extracts the following entities:
  - **DOOR_NO**
  - **STREET**
  - **AREA**
  - **DISTRICT**
  - **PINCODE**

## Prerequisites  
Make sure you have the following installed on your system:
- **Python 3.8 or above**  
- **pip** for Python package management  

## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/address-ner.git
   cd address-ner
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
3. Verify your installation by checking the version of spaCy:
    ```bash
    python -c "import spacy; print(spacy.__version__)"

**Note:**
The training json file should have examples that are diverse, so that it can recognise wide range of address format.


## Usage
### Training the Model
1. Ensure merged_annotations.json is in the same directory as train_model.py.
2. Run the following command to train the model:
   ```bash
    python train_model.py
  
### Testing the Model
1. Make sure the custom_ner_model directory exists after training.
2. Run the test script using:
    ```bash
    python test_model.py

  #### Example Output:
    111 -> DOOR_NO  
    ABC Street -> STREET  
    Areaname -> AREA  
    Mumbai -> DISTRICT  
    100000 -> PINCODE

## Project Structure  

address-ner/

  ├── merged_annotations.json //Training data
  
  ├── train_model.py //Main training script
  
  ├── test_model.py //Model testing script
  
  ├── requirements.txt //Dependencies
  
  ├── README.md //Project documentation

└── custom_ner_model/ //Folder to store the trained model

