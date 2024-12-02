import tkinter as tk
from PIL import Image, ImageTk

# Eltérések az első és a második pályán
level1_differences = [
    (565, 520),
    (520, 310),
    (170, 145),
    (90, 210),
    (10, 145),
    (285, 425),
    (145, 180),
]
level2_differences = [
    (114, 34),
    (87, 102),
    (155, 106),
    (92, 205),
    (85, 360),
    (170, 275),
    (223, 140),
    (320, 88),
    (308, 149),
    (340, 200),
    (233, 250),
    (270, 240),
    (340, 315),
    (280, 370),
]

# Globális változók
found_differences = []
current_differences = []
image1_path = ""
image2_path = ""

# Ellenőrző funkció (kattintásra)
def check_difference(event):
    global found_differences
    x, y = event.x, event.y
    for diff_x, diff_y in current_differences:
        if (diff_x - 20 <= x <= diff_x + 20) and (diff_y - 20 <= y <= diff_y + 20):
            if (diff_x, diff_y) not in found_differences:
                found_differences.append((diff_x, diff_y))
                canvas.create_oval(diff_x - 15, diff_y - 15, diff_x + 15, diff_y + 15, outline="red", width=3)
                update_message(f"Talált különbségek: {len(found_differences)}/{len(current_differences)}")
                break

    if len(found_differences) == len(current_differences):
        end_game()

# Üzenet frissítése
def update_message(text):
    message_label.config(text=text)

# Játék vége
def end_game():
    for widget in root.winfo_children():
        widget.destroy()

    # Gratuláló üzenet
    tk.Label(root, text="Gratulálok, megtaláltad az összes különbséget!", font=("Arial", 20), fg="black").pack(pady=50)

    # Vissza a pályaválasztó menübe
    tk.Button(root, text="Vissza a játékokhoz", font=("Arial", 14), command=open_second_menu).pack(pady=20)

# Pálya indítása
def start_level(level):
    global found_differences, current_differences, image1_path, image2_path, canvas, message_label

    if level == 1:
        #https://github.com/Frichetten/Image-Difference-Finder
        image1_path = "Image1.jpg"
        image2_path = "Image2.jpg"
        current_differences = level1_differences
    elif level == 2:
        #https://en.wikipedia.org/wiki/Spot_the_difference
        image1_path = "Image1_1.jpg"
        image2_path = "Image1_2.jpg"
        current_differences = level2_differences

    found_differences = []

    for widget in root.winfo_children():
        widget.destroy()

    root.title(f"Különbségkereső játék - {level}. pálya")

    try:
        image1 = Image.open(image1_path)
        image2 = Image.open(image2_path)
    except Exception as e:
        tk.Label(root, text=f"Hiba a képek betöltésekor: {e}", fg="red").pack()
        return

    tk_image1 = ImageTk.PhotoImage(image1)
    tk_image2 = ImageTk.PhotoImage(image2)

    canvas = tk.Canvas(root, width=tk_image1.width() * 2, height=tk_image1.height())
    canvas.pack()

    canvas.create_image(0, 0, anchor=tk.NW, image=tk_image1)
    canvas.create_image(tk_image1.width(), 0, anchor=tk.NW, image=tk_image2)

    canvas.bind("<Button-1>", check_difference)

    message_label = tk.Label(root, text="Keresd meg az összes különbséget!", font=("Arial", 14), fg="black")
    message_label.pack(pady=10)

    canvas.image1 = tk_image1
    canvas.image2 = tk_image2

# Második menü
def open_second_menu():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Válassz egy pályát!", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="1. pálya", font=("Arial", 14), command=lambda: start_level(1)).pack(pady=10)
    tk.Button(root, text="2. pálya", font=("Arial", 14), command=lambda: start_level(2)).pack(pady=10)
    tk.Button(root, text="Kilépés", font=("Arial", 14), command=root.quit).pack(pady=10)

# Főmenü
root = tk.Tk()
root.title("Játék")

tk.Label(root, text="Üdvözöllek a játékban!", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Játék", font=("Arial", 14), command=open_second_menu).pack(pady=10)

root.mainloop()