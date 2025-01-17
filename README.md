![Attendify Cover](attendify-cover.png)

# Machine Learning | Face Recognition Smart Attendance Model

**Attendify**, a machine learning-based smart attendance model, aims to address the challenges of traditional attendance marking, such as human errors, time consumption, and the additional workload.

---

### **Submitted by:**
**Name:** Princess Jasmin S. Panilagao <br>
**Registration Number:** 481457 <br>
**Course:** Creative Computing Year 3

---

## 📋 **Table of Contents**
1. [Features](#features)
2. [System Architecture](#system-architecture)
3. [Technology Stack](#technology-stack)
4. [Dataset](#dataset)
5. [Model Details](#model-details)
6. [Model Walkthrough](#model-walkthrough)

---

## 🤖 **Features**  
- Face recognition-based attendance marking
- Integration with the KNN machine learning model
- User-friendly GUI for seamless operation
- Real-time attendance record with accurate timestamps
- Support for multiple entries

---

## 🧩 **System Architecture**
1. **Data Registration:** Users' names and images are captured and stored for training.
2. **Face Recognition:** The KNN algorithm identifies faces based on stored data.
3. **Attendance Logging:** Attendance data is logged in real-time, saved in a CSV file, and displayed in a web app
4. **GUI Integration:** A user-friendly interface that makes interacting with the model clear and efficient.

---

## 🛠 **Technology Stack**
- **Programming Language:** Python
- **Frameworks/Libraries:**
  - Face recognition: OpenCV, scikit-learn  
  - GUI Development: Tkinter, Streamlit  
  - Data Management: Pandas, Pickle, CSV  
  - Visualization: Matplotlib  
  - Windows Automation: win32com.client  
  - Utilities: time, datetime  
- **Machine Learning Model:** K-Nearest Neighbors (KNN)

---

## 📊 **Dataset**
- **Source:** Name and face captures provided by users during data collection.
- **Preprocessing:** Images are resized, normalized, and cropped to a uniform size of 50x50 pixels.
- **Features:** Facial embeddings extracted using Histogram of Oriented Gradients (HOG) and OpenCV.

---

## 🧠 **Model Details**
- **Algorithm:** K-Nearest Neighbors (KNN)
- **Feature Extraction:** HOG (Histogram of Oriented Gradients)
- **Training Process:** Images of registered users are converted into numerical data (embeddings) and stored. These embeddings are used to identify faces during attendance marking.
- **Performance**: Designed for accurate and quick face recognition during live attendance tracking.

---

## 💻 **Model Walkthrough**
Check out the full video walkthrough of Attendify [here](https://youtu.be/QLbzEteVN7M)
