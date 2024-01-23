import tkinter as tk
from tkinter import messagebox
import requests as rs

def on_button_click():
    # Hole den Stadtnamen aus dem Entry-Widget
    city = city_entry.get()
    
    api_key = '4244f04564a9554dbb3be9531725e17b'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&exclude=current&lang=de'
    response = rs.get(url)

    # Überprüfe den HTTP-Statuscode
    if response.status_code == 200:
        data = response.json()

        # Extrahiere die wichtigsten Daten
        temperatur = data['main']['temp']
        luftfeuchtigkeit = data['main']['humidity']
        wetterbeschreibung = data['weather'][0]['description']
        windgeschwindigkeit = data['wind']['speed']

        # Aktualisiere das Label mit den Wetterdaten
        result_label.config(text=f'City: {city} \nTemperatur: {temperatur}°C\nLuftfeuchtigkeit: {luftfeuchtigkeit}%\nWetter: {wetterbeschreibung}\nWindgeschwindigkeit: {windgeschwindigkeit} m/s')
    else:
        result_label.config(text=f"Fehler bei der Anfrage. Statuscode: {response.status_code}")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Meine Python Wetter GUI")

# Label hinzufügen
label = tk.Label(root, text="Gib den Namen deiner Stadt ein und klicke den Button, um die Wetterdaten abzurufen.")
label.pack(pady=10)

# Entry-Widget für die Stadt
city_entry = tk.Entry(root, width=30,)
city_entry.pack(pady=10)

# Ergebnislabel hinzufügen
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Button hinzufügen
button = tk.Button(root, text="Wetter abrufen", command=on_button_click)
button.pack(pady=10)

# Hauptloop starten
root.mainloop()
