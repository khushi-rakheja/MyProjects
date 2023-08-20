from tkinter import*
from tkinter import ttk
from pip._vendor import requests


city_name="Hisar"
data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=75addc6f2dc328bbc44f353f244f8e53").json()
print(data)
def data_get():

    city=city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=75addc6f2dc328bbc44f353f244f8e53").json()
    weather_label1.config(text=data["weather"][0]["main"])
    description_label1.config(text=data["weather"][0]["description"])
    temperature_label1.config(text=data["main"]["temp"]-273.15)
    min_temperature_label1.config(text=data["main"]["temp_min"]-273.15)
    max_temperature_label1.config(text=data["main"]["temp_max"]-273.15)
    pressure_label1.config(text=data["main"]["pressure"])




root=Tk()
root.title("My Weather")
root.geometry("500x500+0+0")
root.config(bg="light grey")
name_label = Label(root,text="My Weather Forecast", font=("arial",30,"bold"),bg="light grey")
name_label.place(x=15,y=30,height=50,width=450)
place_label = Label(root,text="Enter the place:",font=("arial",10,"bold"))
place_label.place(x=15,y=120,height=30,width=130)
list_name=["Hisar","Faridabad","Gurgaon","Rohtak","Ambala","Sonipat","Panipat","Karnal","Jind","Yamunanagar","Jhajjar","Kaithal","Sirsa","Palwal","Panchkula","Kurukshetra","Fatehabad","Bahadurgarh","Narnaul","Chandigarh","Jagadhari","Bhiwani","Rewari","Mahendragarh","Delhi","Manali","Shimla","Rishikesh","Dehradun","Nainital","Haridwar","Patiala","Jalandhar","Bathinda"]

city_name=StringVar()
city=ttk.Combobox(root,text="My Weather App",values=list_name,font=("arial",10),textvariable=city_name)
city.place(x=170,y=120,height=30,width=130)



weather_label = Label(root,text="Weather Climate:", font=("arial",15,"bold"),bg="light grey")
weather_label.place(x=10,y=250,height=40,width=160)
weather_label1 = Label(root,text="", font=("arial",15,"bold"),bg="light grey")
weather_label1.place(x=200,y=250,height=40,width=160)

description_label = Label(root,text="Climate Description:", font=("arial",15,"bold"),bg="light grey")
description_label.place(x=10,y=290,height=40,width=190)
description_label1 = Label(root,text="", font=("arial",15,"bold"),bg="light grey")
description_label1.place(x=200,y=290,height=40,width=190)

temperature_label = Label(root,text="Temperature:", font=("arial",15,"bold"),bg="light grey")
temperature_label.place(x=10,y=330,height=40,width=160)
temperature_label1 = Label(root,text="", font=("arial",15,"bold"),bg="light grey")
temperature_label1.place(x=200,y=330,height=40,width=200)

min_temperature_label = Label(root,text="Min Temperature:", font=("arial",15,"bold"),bg="light grey")
min_temperature_label.place(x=10,y=370,height=40,width=180)
min_temperature_label1 = Label(root,text="", font=("arial",15,"bold"),bg="light grey")
min_temperature_label1.place(x=200,y=370,height=40,width=200)


max_temperature_label = Label(root,text="Max Temperature:", font=("arial",15,"bold"),bg="light grey")
max_temperature_label.place(x=10,y=410,height=40,width=180)
max_temperature_label1 = Label(root,text="", font=("arial",15,"bold"),bg="light grey")
max_temperature_label1.place(x=200,y=410,height=40,width=200)

pressure_label = Label(root,text="Pressure:", font=("arial",15,"bold"),bg="light grey")
pressure_label.place(x=10,y=450,height=40,width=160)
pressure_label1 = Label(root,text="", font=("arial",15,"bold"),bg="light grey")
pressure_label1.place(x=200,y=450,height=40,width=160)
submit_button=Button(root,text="Submit",font=("arial",15,"bold"),command=data_get)
submit_button.place(x=140,y=170,height=35,width=100)


root.mainloop()