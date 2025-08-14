# YouTube Gesture Controller

Control YouTube playback **hands-free** using real-time **hand gesture recognition** with OpenCV and MediaPipe.  
This project uses your webcam to detect gestures and maps them to YouTube player actions like play, pause, skip, and volume control.

---

## Features
- ✋ Real-time **hand tracking** with [MediaPipe](https://developers.google.com/mediapipe)
  Gesture-based controls for YouTube:
  -   **Pause / Play**
  -   **Skip Next**
  -   **Rewind**
  -   **Volume Up / Down**
- 🖥️ Works on any computer with a webcam
- ⚡ Built with **Python + OpenCV**

---

## Installation & Setup

## Clone the Repository
    git clone https://github.com/sakshik1712/YouTube-Gesture-Controller.git
    cd YouTube-Gesture-Controller
    python -m venv venv
    source venv/bin/activate   # On Linux/Mac
    venv\Scripts\activate      # On Windows
    pip install -r requirements.txt
    python main.py
    
## Install them manually if needed:
    pip install opencv-python mediapipe pyautogui

## Requirements

- Python 3.8+
- OpenCV
- MediaPipe
- PyAutoGUI (for simulating key presses)


## Future Improvements 
- Add gesture calibration for better accuracy
- Support custom gesture mappings
- Create a simple GUI for gesture setup
- Optimize for lower CPU usage

License
- This project is licensed under the MIT License

Author
- Developed by Sakshi K
- Passionate about AI, Computer Vision, and building real-time interactive apps.
