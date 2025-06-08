# AI Voice Replication

[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Last Updated](https://img.shields.io/github/last-commit/anshulraj10/ai-voice-replication)](https://github.com/anshulraj10/ai-voice-replication)

A **Flask-based web application** for realistic **voice cloning** using **OpenVoice v1 and v2**. Users can either upload audio or record their voice in-browser, input custom text, select expressive voice styles or accents, and generate natural-sounding cloned audio.

---

## Features

- Upload audio files **or** use your **microphone** to record directly.
- **OpenVoice v1**: voice cloning with *style* options:  
  `default`, `friendly`, `cheerful`, `excited`, `sad`, `angry`, `terrified`, `shouting`, `whispering`
- **OpenVoice v2**: accent-aware voice cloning:  
  `American`, `British`, `Indian`, `Australian`, `Default`
- Real-time **audio generation** and **download/playback** support
- Fully **client-server integrated** with Flask and JS (recorder.js)

---

## Project Structure

```
.
├── app.py                   # Flask entry point
├── routes.py                # Routing logic
├── requirements.txt         # Dependencies
├── style.css                # Optional styling overrides
├── templates/
│   └── index.html           # Web UI
├── static/
│   ├── recorder.js          # Microphone recorder logic
│   ├── uploads/             # Uploaded audio storage
│   └── outputs/             # Generated audio storage
├── services/                # Core voice generation services
│   ├── audio_processing.py
│   ├── openvoice_v1.py
│   └── openvoice_v2.py
├── openvoice/               # Model-related scripts
└── checkpoints/             # Downloaded model weights
    ├── v1/
    │   ├── base_speakers/
    │   └── converter/
    └── v2/
        ├── base_speakers/
        └── converter/
```

---

## Installation

### 1. Clone and Setup Environment
```bash
git clone https://github.com/anshulraj10/ai-voice-replication.git
cd ai-voice-replication
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Download Checkpoints
- **OpenVoice v1**: [checkpoints_1226.zip](https://myshell-public-repo-host.s3.amazonaws.com/openvoice/checkpoints_1226.zip)
- **OpenVoice v2**: [checkpoints_v2_0417.zip](https://myshell-public-repo-host.s3.amazonaws.com/openvoice/checkpoints_v2_0417.zip)

Extract into `checkpoints/` as follows:
```
checkpoints/
├── v1/
│   ├── base_speakers/
│   └── converter/
└── v2/
    ├── base_speakers/
    └── converter/
```

### 4. Run the App
```bash
python app.py
```
Then open your browser at: [http://localhost:5000](http://localhost:5000)

---

## Usage Instructions

1. **Enter the text** to clone.
2. **Upload or record** your voice.
3. **Choose model version**:
   - **V1**: pick a style.
   - **V2**: pick an accent.
4. Adjust **speech speed** if needed.
5. Click **"Generate Voice"** to create output.
6. Listen or **download the generated audio**.

---

## Model Details

- **OpenVoice v1** – [GitHub](https://github.com/myshell-ai/OpenVoice)
  - Supports expressive **style-based cloning**
- **OpenVoice v2** – [GitHub](https://github.com/myshell-ai/OpenVoice)
  - Adds **accent conditioning** and improved quality

Both models run **locally**, ensuring privacy and low latency.

---

## Key Technologies

- **Flask** — backend server
- **JavaScript (MediaRecorder API)** — for audio recording
- **FFmpeg + Librosa + Torchaudio** — audio processing
- **Torch** — for model inference
- **dotenv** — secret management

---

## Contribution Guidelines

We welcome contributions! To contribute:

1. Fork this repo
2. Create a new branch (`feature/your-feature`)
3. Commit your changes with clear messages
4. Open a pull request with a description

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Credits & Acknowledgements

Created by [Anshul Raj](https://anshulraj.com)  
Voice cloning powered by [MyShell OpenVoice](https://github.com/myshell-ai/OpenVoice)

---