# TOXOUT - A Harmful Ingredient Detector 🧴 

## 📌 Description  
This project helps users identify harmful ingredients in **cosmetic, skincare, or food products** using **OCR (Optical Character Recognition)** and **speech recognition**. The program scans **ingredient labels** from **images, webcam captures, or voice input**, extracts the text, and cross-checks it against a predefined list of harmful chemicals.  

## 🚀 Features  
✅ **Manual Input** – Enter ingredient lists manually for checking.  
✅ **Image Upload** – Extracts text from an uploaded image using **Tesseract OCR**.  
✅ **Webcam Capture** – Takes a picture of the label and scans for harmful ingredients.  
✅ **Voice Input** – Listens to spoken ingredients and detects harmful ones.  
✅ **Preprocessing for OCR** – Applies **image enhancement** for better text extraction.  

## 🛠️ Installation  
1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/harmful-ingredient-detector.git
   cd harmful-ingredient-detector
   ```
2. **Install dependencies**  
   ```bash
   pip install opencv-python pytesseract pillow speechrecognition
   ```
3. **Download and Install Tesseract OCR**  
   - [Windows Installer](https://github.com/UB-Mannheim/tesseract/wiki)  
   - Add Tesseract to the system path:  
     ```
     C:\Program Files\Tesseract-OCR\tesseract
     ```
   - Update the script with the correct path to `tesseract.exe`.  

## 🎯 Usage  
Run the program using:  
```bash
python main.py
```
Select an input method:  
1️⃣ **Manual Input** – Type ingredients for checking.  
2️⃣ **Image Upload** – Provide an image path for analysis.  
3️⃣ **Webcam Capture** – Capture an image for scanning.  
4️⃣ **Voice Input** – Speak the ingredients for analysis.  

## 📜 Dependencies  
- **Python 3**  
- **OpenCV (`cv2`)**  
- **Tesseract OCR**  
- **Pillow**  
- **SpeechRecognition**  

## 🎯 Future Improvements  
🚀 **Mobile App Integration**  
🚀 **Database for ingredient safety levels**  
🚀 **Real-time scanning with AR**  

## 🤝 Contributing  
Feel free to open issues, fork the repo, and submit pull requests!  

---

Let me know if you want any modifications! 🚀
