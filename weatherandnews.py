import httpx
import customtkinter
from PIL import ImageTk, Image
from io import BytesIO
import threading
import tkinter as tk


def button_event():
    city = entry.get()
    if not city:
        label_icon.configure(image="", text='Enter a city or country name', font=("", 18), pady=10)
        label_icon.pack()
        label_weather_text.pack_forget()

    else:
        url = f"http://api.weatherapi.com/v1/current.json?key=1dd086a853a94a64ab370611230404&q={city}&aqi=no"
        with httpx.Client() as client:
            try:
                response = client.get(url)
            except Exception as e:
                label_weather_text.configure(text="There was some error loading request try again")

            if "error" not in response.json():
                icon = response.json()["current"]["condition"]["icon"]
                condition = response.json()["current"]["condition"]["text"]
                wind_speed = response.json()["current"]["wind_kph"]
                humidity = response.json()["current"]["humidity"]
                local_time = response.json()["location"]["localtime"]
                if not condition or not icon:
                    print("Enter a valid city or country")
                else:
                    if "http" not in icon:
                        icon = f"http:{icon}"
                    print(icon)
                    response = httpx.get(icon)
                    img_data = response.content
                    img = Image.open(BytesIO(img_data))
                    my_image = customtkinter.CTkImage(light_image=img,
                                                      dark_image=img,
                                                      size=(100, 100))
                    label_icon.configure(image=my_image)
                    label_icon.configure(text='')
                    label_icon.pack(fill="both", expand=False)
                    label_weather_text.configure(
                        text=f"Condition : {condition}\t\tWind speed : {wind_speed} kph\n Humidity : {humidity}\t\t Time : {local_time}")
            else:
                label_weather_text.configure(text="No matching location found.")
                label_icon.configure(image='')
        label_weather_text.pack(fill="x", expand=False)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("900x700")
app.title("Weather And News")

tabview = customtkinter.CTkTabview(app, corner_radius=10, border_width=3)
tabview.pack(fill="both", expand=True, padx=20, pady=20)

tabview.add("Weather")
tabview.add("News")
tabview.set("Weather")

weather_frame = customtkinter.CTkFrame(master=tabview.tab("Weather"), corner_radius=10)
weather_frame.pack(fill="both", expand=True, padx=20, pady=20)

frame1 = customtkinter.CTkFrame(master=weather_frame, corner_radius=10, border_width=2)
frame2 = customtkinter.CTkFrame(master=weather_frame, corner_radius=10)
disclaimer = customtkinter.CTkLabel(master=weather_frame, font=("", 14), pady=20,
                                    text="Weather Forecast is not 100% accurate its taken from an API")

frame1.pack(fill="x", expand=False, padx=20, pady=20)
disclaimer.pack(fill="none", expand=False, padx=20, pady=20)
frame2.pack(fill="x", expand=False, padx=20, pady=20)

entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Name of country or city", height=50)
entry.pack(fill="x", expand=False, padx=20, pady=20)

button = customtkinter.CTkButton(master=frame1, text="Submit", command=button_event, height=40)
button.pack(expand=False, padx=20, pady=20)

label_icon = customtkinter.CTkLabel(master=frame2, pady=10)
label_weather_text = customtkinter.CTkLabel(master=frame2, font=("", 25), pady=20)

frame3 = customtkinter.CTkScrollableFrame(master=tabview.tab("News"))
frame3.pack(expand=True, fill="both")

Sub_Img_Url = "https://images.unsplash.com/photo-1495020689067-958852a7765e?q=80&w=500&auto=format&fit=crop"

def load_news_background():
    """Starts the load_news function in a background thread to prevent freezing."""
    threading.Thread(target=load_news, daemon=True).start()

def load_news():
    try:
        with httpx.Client() as client:
            url = "https://newsapi.org/v2/everything?q=India&sortBy=publishedAt&apiKey=9e5ec95d33b64189a7657c2e4df884b1"
            res = client.get(url)
            data = res.json()
            
            if data.get("status") == "ok":
                articles = data.get("articles", [])
                print(f"Fetched {len(articles)} articles")
                for article in articles:
                    title = article.get('title', 'No Title')
                    image_url = article.get("urlToImage")
                    
                    card = customtkinter.CTkFrame(master=frame3, corner_radius=10)
                    card.pack(fill="x", padx=10, pady=10)
                    
                    try:
                        if image_url:
                            img_res = client.get(str(image_url))
                            img = Image.open(BytesIO(img_res.content))
                        else:
                            sub_img_res = client.get(Sub_Img_Url)
                           
                            img = Image.open(BytesIO(sub_img_res.content))
                    except:
                        img = Image.open(BytesIO(sub_img_res.content))

                    thumbnail = customtkinter.CTkImage(light_image=img, dark_image=img, size=(500, 300))
                    
                    image_label = customtkinter.CTkLabel(master=card, image=thumbnail, text="")
                    image_label.image = thumbnail 
                    image_label.pack(pady=10)
                    
                    label = customtkinter.CTkLabel(master=card, text=title, wraplength=600, font=("", 14, "bold"))
                    label.pack(padx=10, pady=(0, 10))
                    app.update_idletasks()
            else:
                print("API Status not OK:", data.get("message"))
    except Exception as e:
        print(f"Network error in News: {e}")

load_news_background()

app.mainloop()

