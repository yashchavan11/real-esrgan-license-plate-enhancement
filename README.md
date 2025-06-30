# 🚗🔍 License Plate Image Enhancement with Real-ESRGAN

This project fine-tunes the **Real-ESRGAN** model to enhance low-quality Indian vehicle license plate images.  
It addresses real-world issues like blurriness, compression artifacts, and low resolution — improving readability and recognition for applications like traffic enforcement, toll collection, and vehicle tracking.

---

## 📌 Overview

- ✅ Fine-tuned [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) on a custom dataset of Indian license plates.
- ✅ Removes noise, restores details, and upscales low-quality plates.
- ✅ Published a paper on this work in IJIRT.

---

## 🧩 Features

- Super-resolution and artifact removal for license plate images.
- Uses Real-ESRGAN `x4plus` architecture.
- Simple to run with Python.
- Ready for integration into a web app (Flask or Streamlit).

---

## 🚀 Getting Started

Follow these steps to run this project on your own machine.

---

###  Clone this repo
```bash
git clone https://github.com/yashchavan11/real-esrgan-license-plate-enhancement.git
cd real-esrgan-license-plate-enhancement

### Create and activate a virtual environment
```bash
# Create virtual environment
python -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Or activate on Windows
venv\Scripts\activate

### Install dependencies
pip install -r requirements.txt

### Add input images
```bash
inputs/test_plate1.jpg
inputs/test_plate2.png

### Run inference
```bash
python inference.py
Enhanced results will be saved automatically in the results/ folder.

🖥️ Optional: Make a Web App
You can wrap this in a simple Flask or Streamlit app to create a user-friendly front-end:

Upload image

Click enhance

Download the result

📚 Paper
📄 “A Survey on Image Quality Enhancement using RealESRGAN: A Comprehensive Review of Datasets and
Approaches”
https://ijirt.org/publishedpaper/IJIRT176026_PAPER.pdf
Published in the International Journal for Innovative Research in Technology (IJIRT).

👨‍💻 Author
Yash Chavan
📧 yashgchavan7@gmail.com

✨ Acknowledgements
xinntao/Real-ESRGAN
XPixelGroup/BasicSR

⭐ If you find this useful, please star this repo!

Curious mind. Practical builder. Never stop learning.
