# Real-Time Face & Eye Detection Using Haar Cascade

## 📌 Overview
This project implements **real-time face and eye detection** using OpenCV and Haar Cascade classifiers. The program captures video from a webcam and detects faces and eyes using pre-trained Haar cascade XML files.

## 🛠 Features
- **Real-time face detection** using `haarcascade_frontalface_default.xml`
- **Real-time eye detection** using `haarcascade_eye.xml`
- Uses OpenCV for image processing
- Adjustable detection parameters

## 🚀 Setup Instructions

### 🔹 Prerequisites
Ensure you have the following installed:
- Python (>=3.7)
- OpenCV library (`opencv-python`)
- Haar Cascade XML files for face and eye detection

### 🔹 Install Dependencies
Run the following command to install OpenCV:
```bash
pip install opencv-python
```

### 🔹 Clone the Repository
Use SSH (if set up):
```bash
git clone git@github.com:NurulBashar/RealTimeFaceDetectionUsingHaarCascade.git
```
Or use HTTPS:
```bash
git clone https://github.com/NurulBashar/RealTimeFaceDetectionUsingHaarCascade.git
```

### 🔹 Add Haar Cascade Files
Download the required Haar cascade XML files and place them in your project directory:
- [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
- [haarcascade_eye.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml)

## 📜 Usage
Run the script using:
```bash
python main.py
```

- The webcam will open and start detecting faces and eyes.
- Press **'q'** to exit the program.

## 📝 Code Explanation
### 🔹 Main Components:
1. **Capture Video from Webcam:**
   ```python
   cap = cv2.VideoCapture(0)
   cap.set(4, 640)  # Set width
   cap.set(4, 480)  # Set height
   ```
2. **Load Haar Cascade Files:**
   ```python
   face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
   eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
   ```
3. **Face & Eye Detection in Real-Time:**
   ```python
   faces = face_cascade.detectMultiScale(img_gray, 1.3, 2)
   for (x, y, w, h) in faces:
       cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
   ```
4. **Display Output:**
   ```python
   cv2.imshow("Face and Eye Detection", img)
   ```

## 🎯 Expected Output
The script will detect faces and eyes and highlight them using **rectangles**:
- **Face:** Red rectangle 🟥
- **Eyes:** Green rectangle 🟩

## 🔧 Troubleshooting
1. **Error: Face cascade file not loaded!**
   - Ensure the `haarcascade_frontalface_default.xml` file is in the correct directory.
   
2. **No face detected?**
   - Adjust `detectMultiScale()` parameters: `scaleFactor` and `minNeighbors`.

3. **Webcam not working?**
   - Change `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` if multiple cameras exist.

## 📜 License
This project is **open-source** and released under the MIT License.

## 📌 Acknowledgments
- **OpenCV**: [https://opencv.org](https://opencv.org)
- **Haar Cascade Classifiers**: [OpenCV GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades)

## 👨‍💻 Author
**Nurul Bashar**

