# 📰🌦️ Weather and News Desktop Application

This is a desktop GUI application developed using **Python** and **CustomTkinter** that provides users with **real-time weather updates** and **top news headlines**. It integrates APIs to fetch and display live weather and news data in a minimal, modern interface.

---

## ✨ Features

### 🌦️ **Weather Forecast**

* Get current weather conditions for any **city or country**.
* Fetches data from **WeatherAPI**.
* Displays:

  * Weather condition
  * Wind speed
  * Humidity
  * Local time
  * Weather icons
* Error handling for invalid or blank input.
* Real-time response display.

### 📰 **Top News Headlines**

* Automatically fetches **India's latest news headlines**.
* Uses **NewsAPI** for top trending news.
* Displays:

  * News title
  * Thumbnail image (from API or fallback)
* Scrollable list of news cards.

### 💡 **Other Highlights**

* **Modern UI** using `customtkinter`
* Responsive frames with tabbed navigation
* Weather disclaimer included

---

## 📦 Tech Stack

| Component      | Library / Tool                                                    |
| -------------- | ----------------------------------------------------------------- |
| UI Framework   | [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter) |
| HTTP Requests  | [`httpx`](https://www.python-httpx.org/)                          |
| Image Handling | `PIL (Pillow)`                                                    |
| Weather API    | [WeatherAPI.com](https://www.weatherapi.com/)                     |
| News API       | [NewsAPI.org](https://newsapi.org/)                               |

---

## 📸 Screenshots

> *(You can add screenshots here)*
> Example:
> ![App Screenshot](screenshot.png)

---

## 🛠️ Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/weather-news-app.git
   cd weather-news-app
   ```

2. **Install dependencies**

   ```bash
   pip install customtkinter httpx pillow
   ```

3. **Update API Keys**

   * Replace the API keys in the script:

     * `WeatherAPI`: Replace `key=1dd086a853a94a64ab370611230404`
     * `NewsAPI`: Replace `apiKey=9e5ec95d33b64189a7657c2e4df884b1`

4. **Run the app**

   ```bash
   python app.py
   ```

---

## 📂 Folder Structure (Optional)

```
weather-news-app/
├── app.py
├── README.md
├── news.jpg      # Fallback image for news cards
├── requirements.txt
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

