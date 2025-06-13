# 🧙‍♂️ Invisibility Cloak App

A fun, real-time **Streamlit + OpenCV** web app that lets you become *invisible* using computer vision. Inspired by Harry Potter’s cloak, powered by **color masking**, **voice activation**, and **machine learning-based color detection**.

Live Demo → 🌐 [https://invisibility-cloak.onrender.com](https://invisibility-cloak.onrender.com)  


---

## 🚀 Features

- 🎥 Real-time cloak masking using OpenCV
- ✅ Auto-detect cloak color using KMeans
- 🗣 Voice Activation: “Make me invisible!”
- 🎞 Download processed video (.mp4 or .avi)
- 🌐 Deployable via Docker on Render/Vercel
- 📸 Camera input using Streamlit's UI

---


<p align="center">
  <img src="https://raw.githubusercontent.com/your-username/invisibility-cloak-app/main/demo.gif" width="600"/>
</p>

---

## 🧠 How It Works

1. **Background Capture** – Captures initial background before applying mask
2. **Color Detection** – HSV masking filters cloak pixels
3. **Auto Cloak Color Detection** – Uses KMeans on cloak region to detect color automatically
4. **Voice Commands** – SpeechRecognition turns on invisibility
5. **Frame Replacement** – Masked pixels are replaced by background for invisibility effect

---

## 📁 Folder Structure

invisibility-cloak-app/
│
├── app/
│ ├── init.py
│ ├── cloak_logic.py # OpenCV invisibility effect
│ ├── voice_activation.py # Voice command activation
│ ├── color_detection.py # Auto color detection via KMeans
│
├── cloak_app.py # Streamlit interface
├── requirements.txt
├── Dockerfile # For deployment
├── render.yaml # Render deployment config
├── .gitignore
├── README.md


---

## 🛠️ Installation

```bash
git clone https://github.com/your-username/invisibility-cloak-app.git
cd invisibility-cloak-app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run cloak_app.py

☁️ Deploy on Render (Free)
Commit all files to GitHub (including Dockerfile, render.yaml)

Go to https://render.com

Click New > Web Service

Connect your GitHub repo

Select Docker as environment

Click Create Web Service

🧪 Dependencies
opencv-python

streamlit

numpy

speechrecognition

scikit-learn

pyaudio

Pillow

🙌 Acknowledgements
Harry Potter for the idea 🪄

OpenCV for real-time video processing

Streamlit for easy UI

KMeans for automatic cloak color detection

🧑‍💻 Author
Shashank Suryawanshi
LinkedIn | GitHub
