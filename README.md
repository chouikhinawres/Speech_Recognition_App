#Speech_Recognition_App
##Description
Speech_Recognition_App is a lightweight speech-to-text web application built with **Streamlit**.
It allows users to record audio directly from the browser and automatically transcribe speech into text using Google Speech Recognition API.
The project focuses on simplicity, portability, and fast deployment by avoiding system-level audio dependencies.

##Architecture
User (voice input) → Streamlit UI → Audio Recorder → Temporary WAV File → SpeechRecognition → Google Speech API → Text Output

- **User** — records speech directly from the browser
- **Streamlit** — web interface handling recording and display
- **Audio Recorder** (audiorecorder) — captures voice input
- **Temporary File System** — stores audio as WAV format
- **SpeechRecognition **— processes audio data
- **Google Speech API** — converts speech into text
- **Output** — displayed transcription in Streamlit UI

##Tech Stack
- Python
- Streamlit
- SpeechRecognition
- audiorecorder
- tempfile
  
##Installation

1. Clone the repository:
   git clone https://github.com/YOUR_USERNAME/Speech_Recognition_App.git

3. Install dependencies:
   pip install -r requirements.txt

4. Run the Application
   streamlit run app.py
   
#Workflow
1. User clicks Start Recording in the Streamlit interface
2. Audio is captured directly from the browser
3. Recording is stopped and exported as a WAV file
4. The system processes the audio using SpeechRecognition
5. Google Speech API converts speech into text
6. Transcription is displayed in real time on the UI
   
#Project Structure
Speech_Recognition_App/
│
├── app.py
├── requirements.txt
└── README.md

#Requirements
streamlit
SpeechRecognition
audiorecorder

## Author
Nawres Mechergui — Data Scientist & Full-Stack Developer
nawresmechergui019@gmail.com
github.com/chouikhinawres
