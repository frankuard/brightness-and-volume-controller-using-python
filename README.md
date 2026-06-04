# ✋ Hand Gesture Controller

A real-time computer vision project that lets you control your **screen brightness** and **system volume** using hand gestures — no keyboard or mouse needed. Powered by **MediaPipe** and **OpenCV**.

---

## 🎯 Features

- 💡 **Brightness Control** — Pinch your thumb and index finger to adjust screen brightness in real time
- 🔊 **Volume Control** — Use the same gesture to control system audio volume
- 🖐️ **Real-time Hand Tracking** — Detects and tracks up to 2 hands simultaneously using MediaPipe's Hand Landmarker
- 📷 **Live Webcam Feed** — Displays annotated hand skeleton with landmark indices on screen

---

## 🧠 How It Works

1. Webcam captures live video frames
2. Frames are passed to MediaPipe's `HandLandmarker` (LIVE_STREAM mode)
3. 21 hand landmarks are detected per hand
4. The **Euclidean distance** between the **thumb tip (landmark 4)** and **index fingertip (landmark 8)** is calculated
5. That distance is mapped (interpolated) to a 0–100 range
6. The mapped value is sent to either `screen_brightness_control` or `pycaw` to adjust brightness/volume

---

## 📁 Project Structure

```
hand-gesture-controller/
│
├── models/
│   └── hand_landmarker.task       # MediaPipe Hand Landmarker model file
│
├── brightness_controller.py       # Brightness control using pinch gesture
├── volume_controller.py           # Volume control using pinch gesture
└── requirements.txt
```

---

## ⚙️ Feature Details

| Feature | Details |
|---|---|
| Landmark used | Thumb tip (4) & Index fingertip (8) |
| Min gesture distance | 30 px → 0% |
| Max gesture distance | 160 px → 100% |
| Interpolation | `numpy.interp` |
| Hands supported | Up to 2 |
| Webcam resolution | 640 × 480 |

---

## 🔄 Data Flow

```
Webcam Frame → Flip (Mirror) → RGB Convert → MediaPipe HandLandmarker
    → Landmark Detection → Distance Calculation → Interpolation
        → Brightness / Volume Control → Display Overlay
```

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
- Support for Linux volume control (`alsaaudio` / `pactl`)
- Add a HUD bar to visually display brightness/volume level
- Multi-gesture mode switcher (toggle between brightness and volume with a gesture)
- Package as a background tray application

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
