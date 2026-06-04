# ✋ Hand Gesture Controller

A real-time CV project that lets you control your **screen brightness** and **system volume** using hand gestures — no keyboard or mouse needed. Powered by **MediaPipe** and **OpenCV**.

---

## 🎯 Features

- 💡 **Brightness Control** — Pinch gesture to adjust screen brightness
- 🔊 **Volume Control** — Same gesture to control system audio
- 🖐️ **Real-time Hand Tracking** — Detects up to 2 hands via MediaPipe

---

## 🧠 How It Works

The webcam feed is processed by MediaPipe's `HandLandmarker` in live stream mode. The **Euclidean distance** between the **thumb tip** and **index fingertip** is calculated and mapped to a 0–100 range, which is then applied to brightness or volume in real time.

---

## 💻 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/hand-gesture-controller.git
cd hand-gesture-controller
```

### 2. Download the MediaPipe Model

Download `hand_landmarker.task` from the [MediaPipe Models page](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker) and place it inside the `models/` folder.

### 3. Install the Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Controller

**For Brightness Control:**
```bash
python brightness_controller.py
```

**For Volume Control:**
```bash
python volume_controller.py
```

Press **`q`** to quit.

---

## 📦 Requirements

```
opencv-python
mediapipe
numpy
screen-brightness-control
pycaw
comtypes
```

> ⚠️ **Note:** `pycaw` (volume control) is **Windows only**. `screen-brightness-control` works on Windows and Linux but behavior may vary by hardware.

---

## 📌 Key Learnings

- Real-time video processing with OpenCV
- Hand landmark detection using MediaPipe Tasks API (LIVE_STREAM mode)
- Gesture-based distance mapping with NumPy interpolation
- System-level hardware control (brightness & audio) from Python
- Async callback pattern with `result_callback` in MediaPipe

---

## 🔮 Future Improvements

- Add more gestures (e.g., fist to mute, open palm to maximize brightness)
- Support for Linux and other OS volume control 
- Multi-gesture mode switcher (toggle between brightness and volume with a gesture)

---

## 🛠️ Tech Stack

- Python
- OpenCV
- MediaPipe (Tasks API)
- NumPy
- screen-brightness-control
- pycaw (Windows Audio)
- comtypes

---

## 📜 License

This project is open-source and free to use.

---

## 👤 Author

**Roshan Karki**
