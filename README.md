# 🌦️ Weather and News Desktop Application

A sleek, multithreaded desktop GUI application built with **Python** and **CustomTkinter**. This app provides real-time weather updates and the latest news headlines for India in a single, responsive dashboard.

---

## 📸 Screenshots

| Weather Dashboard | News Feed |
| :---: | :---: |
| <img src="weather_ss.png" width="400" alt="Home"> | <img src="news_ss.png" width="400" alt="Weather Tab "> | <img src="news_ss.png" width="400" alt="News Tab"> |

---

## 🚀 Features

1. **Real-time Weather:** Fetches temperature, wind speed, humidity, and local time via [WeatherAPI](https://www.weatherapi.com/).
2. **Latest News:** Displays 100+ current headlines from India using [NewsAPI](https://newsapi.org/).
3. **Asynchronous Loading:** Uses Python's `threading` library to fetch news data in the background, ensuring the UI never freezes.
4. **Dynamic Content:** Automatically handles image fetching from the web with fallback thumbnail support.
5. **Modern UI:** Built with CustomTkinter for a native, dark-themed experience.

---

## 💻 Installation & Setup

### For Developers (Run from Source)

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/FaizanSayed404/Weather-News-Application.git
   cd Weather-News-Application

2. **Set up Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Run the App:**
   ```bash
   python weatherandnews.py

 ### For Users (Standalone Binary)
 
 1. **Download the Binary:**
     Visit the Releases section and download the weatherandnews file.

 2. **Grant Execution Permissions:**
    ```Bash
    chmod +x weatherandnews
    Launch the Application:
    
3. **Launch the Application:**
   ```Bash
   ./weatherandnews

---

## 🛠️ Built With

1. **CustomTkinter:** Used for creating the modern, responsive UI components.
2. **HTTPX:** A high-performance HTTP client used for all API requests.
3. **Pillow (PIL):** Handles image processing and resizing for news thumbnails.
4. **Threading:** Manages non-blocking background tasks to keep the UI smooth.

---

## 👤 Author  

   **Faizan Sayed**
