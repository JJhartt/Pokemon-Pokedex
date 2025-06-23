import tkinter as tk
import requests
from io import BytesIO
from PIL import Image,ImageTk

base_url = "https://pokeapi.co/api/v2/"
pokemon = ""
pokeinfo = ""

def get_input():
    user_text = txt.get().capitalize()
    print(f"You entered: {user_text}")
    get_pokemon_info(user_text)

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    responce = requests.get(url)
    
    if responce.status_code == 200:
        pokemon_data = responce.json()
        resultant_label.config(text=f"{name} Selected!")
        displayStats(pokemon_data,name)

    else:
        print(f"Failed to retrive data {responce.status_code}")
        resultant_label.config(text=f"{name} doesn't exist, try again!")


def displayStats(pokedata,name):

    total = 0

    sprite_url = pokedata['sprites']['front_default']
    urlResponce = requests.get(sprite_url)

    if len(pokedata['types']) > 1:
        name_label.config(text=f"{name} is {pokedata['types'][0]['type']['name']} {pokedata['types'][1]['type']['name']} type pokemon.")
    else:
        name_label.config(text=f"{name} is {pokedata['types'][0]['type']['name']} type pokemon.")

    hp_label.config(text=f"HP: {pokedata['stats'][0]['base_stat']}")
    attack_label.config(text=f"Attack: {pokedata['stats'][1]['base_stat']}")
    defense_label.config(text=f"Defense: {pokedata['stats'][2]['base_stat']}")
    sp_attack_label.config(text=f"Special Attack: {pokedata['stats'][3]['base_stat']}")
    sp_defence_label.config(text=f"Special Defense: {pokedata['stats'][4]['base_stat']}")
    speed_label.config(text=f"Speed: {pokedata['stats'][5]['base_stat']}")

    image = Image.open(BytesIO(urlResponce.content))
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

    for i in range(0,6):
        total += pokedata['stats'][i]['base_stat']
    stattotal.config(text=f"Stat Total: {total}")

window = tk.Tk()
window.geometry("500x500")
window.title("PokeDex")
resultant_label = tk.Label(text="Enter a Pokemon")


stats_frame = tk.Frame(window)
name_label = tk.Label(stats_frame, text="", font=('Arial', 14, 'bold'))
hp_label = tk.Label(stats_frame, text="")
attack_label = tk.Label(stats_frame, text="")
sp_attack_label = tk.Label(stats_frame, text="")
defense_label = tk.Label(stats_frame, text="")
sp_defence_label = tk.Label(stats_frame, text="")
speed_label = tk.Label(stats_frame, text="")
stattotal = tk.Label(stats_frame, text="")
image_label = tk.Label(stats_frame, text="")

title = tk.Label(window,font=('Arial',18),text="PokeDex API!")
txt = tk.Entry(window, width=40)
btn = tk.Button(window, text="Find", command=get_input)

title.pack()
resultant_label.pack()
txt.pack()
btn.pack()
stats_frame.pack()
name_label.pack()
hp_label.pack()
attack_label.pack()
defense_label.pack()
sp_attack_label.pack()
sp_defence_label.pack()
speed_label.pack()
stattotal.pack()
image_label.pack()
window.mainloop()