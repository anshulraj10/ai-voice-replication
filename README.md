# AI Voice Replication

This project is a web-based application that allows users to generate synthetic voice using the **OpenVoice** model family (V1 and V2).

Users can upload a reference audio sample or record directly from their microphone, input custom text, select voice model options, and synthesize new audio that clones the reference voice.

---

## Features

- Upload your own reference audio (.wav/.mp3)
- Record audio directly from your microphone (browser-based)
- Input any custom text to generate speech
- Choose between OpenVoice V1 or V2 models:
  - **V1**: Style control (friendly, excited, whispering, etc.)
  - **V2**: Dialect/accent control (American, British, Indian, Australian)
- Play the generated audio in-browser
- Download the generated audio file locally

---

## Tech Stack

- **Flask** — backend web server (Python)
- **HTML/CSS + Bootstrap 5** — frontend
- **JavaScript** — handling microphone recording and client-side interactions
- **OpenVoice (V1/V2)** — text-to-speech models
- **PyTorch** — model loading and inference

---

## Installation & Running Locally

1. Download and unzip checkpoints
    - Download the checkpoints folder from the following location:
        ```
        https://drive.google.com/file/d/1QOghqfNwTkQ_C-9E5PgtHE08o4DXTLii/view?usp=drive_link
        ```
    - Unzip the folder at the root directory of the app
2. Install dependencies:
    ```
    pip install git+https://github.com/myshell-ai/MeloTTS.git
    python -m unidic download
    pip install -r requirements.txt
    ```
3. Run the Flask app:
    ```
    python app.py
    ```
4. Open your browser and navigate to:
    ```
    http://localhost:5000
    ```