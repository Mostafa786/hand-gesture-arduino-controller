# 🖐️ Hand Gesture Arduino Controller

Control physical LEDs connected to an Arduino board using 
**real-time hand gesture detection** via your webcam — no buttons, 
no keyboard, just your fingers.

🎥 **Demo Video:** [Watch on LinkedIn](https://www.linkedin.com/posts/mostafa-mahmoud-ai_computervision-arduino-mediapipe-activity-7321765035540733952-IiJY)

---

## 💡 How It Works

1. **Webcam opens automatically** when you run the script
2. **MediaPipe** detects your hand and tracks each finger in real time
3. Each finger maps to a specific **LED on the Arduino**:
   - Finger **up** → LED **ON**
   - Finger **down** → LED **OFF**
4. Commands are sent instantly via **serial communication** (PyFirmata2)

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Computer Vision | MediaPipe, OpenCV |
| Hardware Control | Arduino, PyFirmata2, PySerial |
| Language | Python 3.9 |

---

## ⚙️ Setup & Run

### 1. Flash StandardFirmata to Arduino

Before running the code, upload **StandardFirmata** to your Arduino:

- Open **Visual Studio Code**
- Go to: `File → Examples → Firmata → StandardFirmata`
- Upload it to your board

### 2. Clone the repo
```bash
git clone https://github.com/Mostafa786/hand-gesture-arduino-controller.git
cd hand-gesture-arduino-controller
```

### 3. Activate the virtual environment
```bash
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Connect your Arduino and run
```bash
python main.py
```

> ⚠️ Make sure your Arduino is connected via USB before running.  
> The webcam opens automatically — show your hand to start controlling the LEDs.

---

## 📦 Requirements
```
opencv-python
mediapipe
pyfirmata2
pyserial
```

---

## 🔌 Hardware Required

- Arduino Uno (or compatible board)
- 5 LEDs + resistors
- Breadboard + jumper wires
- USB cable
- Webcam (built-in or external)

---

## 🚀 Future Enhancements

- [ ] Map gestures to more complex actions (servo motors, buzzers)
- [ ] Add gesture recording and playback
- [ ] Support two-hand detection
- [ ] Build a GUI for pin mapping configuration