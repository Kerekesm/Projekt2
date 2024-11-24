import tkinter as tk
from PIL import Image, ImageTk

# Itt add meg a különbségek pozícióit (x, y koordináták a képen belül)
# Ezeket te határozhatod meg!
differences = [
    (565, 520),  # Példa különbség koordinátái
    (520, 310),
    (170, 145),
    (90, 210),
    (10, 145),
    (285, 425),
]
found_differences = []

# Képek elérési útvonala
image1_path = "c:/Image1.jpg"  # Az első kép
image2_path = "c:/Image2.jpg"  # A második kép

# Ellenőrző funkció (kattintásra)
def check_difference(event):
    global found_differences
    x, y = event.x, event.y
    for diff_x, diff_y in differences:
        # Ellenőrzi, hogy a kattintás közel van-e a különbséghez
        if (diff_x - 20 <= x <= diff_x + 20) and (diff_y - 20 <= y <= diff_y + 20):
            if (diff_x, diff_y) not in found_differences:
                found_differences.append((diff_x, diff_y))
                # Piros kör rajzolása a megtalált különbségnél
                canvas.create_oval(diff_x - 15, diff_y - 15, diff_x + 15, diff_y + 15, outline="red", width=3)
                update_message(f"Talált különbségek: {len(found_differences)}/{len(differences)}")
                break

    # Ha az összes különbség megvan
    if len(found_differences) == len(differences):
        update_message("Gratulálok, megtaláltad az összes különbséget!")

# Üzenet frissítése
def update_message(text):
    message_label.config(text=text)

# Tkinter ablak beállítása
root = tk.Tk()
root.title("Különbségkereső játék")

# Képek betöltése
try:
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
except Exception as e:
    print(f"Hiba a képek betöltésekor: {e}")
    exit()

tk_image1 = ImageTk.PhotoImage(image1)
tk_image2 = ImageTk.PhotoImage(image2)

# Vászon (Canvas) létrehozása
canvas = tk.Canvas(root, width=tk_image1.width() * 2, height=tk_image1.height())
canvas.pack()

# Képek megjelenítése egymás mellett
canvas.create_image(0, 0, anchor=tk.NW, image=tk_image1)
canvas.create_image(tk_image1.width(), 0, anchor=tk.NW, image=tk_image2)

# Kattintás esemény kezelése
canvas.bind("<Button-1>", check_difference)

# Üzenetkijelző szöveg
message_label = tk.Label(root, text="Keresd meg az összes különbséget!", font=("Arial", 14), fg="black")
message_label.pack(pady=10)

# Tkinter ablak futtatása
root.mainloop()
