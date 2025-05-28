import httpx
import customtkinter
from PIL import ImageTk, Image
from io import BytesIO
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

with httpx.Client() as client:
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=9e5ec95d33b64189a7657c2e4df884b1"
    res = client.get(url)
    if res.json()["status"] == "ok":
        articles = res.json()["articles"]
    for i, article in enumerate(articles):
        title = article['title']
        image_url = article["urlToImage"]
        # print(image_url)
        card = customtkinter.CTkFrame(master=frame3, corner_radius=10)
        card.pack(fill="x", padx=8, pady=8)
        label = customtkinter.CTkLabel(master=card, text=f"{title}", padx=8, pady=8, font=("", 14))
        if image_url and str(image_url).endswith(".jpg") or str(image_url).endswith(".png") or str(image_url).endswith(".jpeg"):
            response = httpx.get(str(image_url))
            img_data = response.content
            img = Image.open(BytesIO(img_data))
        else :
            img = Image.open(r"C:\Users\faiza\OneDrive\Desktop\Python Project\news.jpg")    
    
        
        thumbnail = customtkinter.CTkImage(light_image=img,
                                           dark_image=img,
                                           size=(500, 300))
        image_label = customtkinter.CTkLabel(image=thumbnail,text="", master=card, padx=8, pady=8)
        image_label.pack(fill="x", expand=True)
        label.pack()

app.mainloop()
