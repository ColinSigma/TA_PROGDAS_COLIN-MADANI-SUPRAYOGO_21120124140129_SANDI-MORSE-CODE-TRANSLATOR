# import library tkinter untuk membuat GUI dan messagebox untuk menampilkan pesan pop-up
import tkinter as tk
from tkinter import messagebox

# fungsi untuk mengubah teks menjadi kode Morse
def morse_it(string, morse_dict):
    # konversi teks menjadi huruf kapital
    string = string.upper()
    morse_code = []  # list untuk menyimpan kode Morse
    for x in string:
        # jika karakter ada dalam kamus Morse, tambahkan kode Morse ke hasil
        if x in morse_dict.keys():
            morse_code.append(morse_dict[x])
        # jika karakter adalah spasi, tambahkan spasi ke hasil
        elif x == " ":
            morse_code.append(" ")
        # jika karakter tidak ada dalam kamus, tampilkan pesan peringatan
        else:
            messagebox.showwarning("Warning", f"The {x} key doesn't exist in the dictionary!")
    
    # gabungkan kode Morse dengan " | " sebagai pemisah
    return " | ".join(morse_code)

# fungsi untuk menangani event tombol "Translate"
def convert_to_morse():
    # ambil teks input dari user
    input_text = entry.get()
    # jika input kosong, tampilkan pesan peringatan
    if not input_text.strip():
        messagebox.showwarning("Warning!!", "Input cannot be empty!")
        return
    
    # konversi teks menjadi kode Morse menggunakan fungsi morse_it
    translated_text = morse_it(input_text, morse_dict)
    # tampilkan hasilnya pada jendela baru
    display_result(translated_text)

# fungsi untuk menampilkan hasil terjemahan di jendela baru
def display_result(translated_text):
    # tentukan lebar jendela berdasarkan panjang teks hasil
    base_width = 400  # Lebar dasar jendela
    char_width = 8    # Lebar tambahan per karakter
    calculated_width = min(base_width + len(translated_text) * char_width, 1000)  # Maksimum lebar 1000
    calculated_height = 300  # Tinggi tetap

    # buat jendela baru untuk menampilkan hasil
    result_window = tk.Toplevel(root)
    result_window.title("Translated Result")
    result_window.geometry(f"{calculated_width}x{calculated_height}")
    result_window.configure(bg="#FEFBEA")

    # label untuk judul hasil
    tk.Label(
        result_window, 
        text="Translated Morse Code:", 
        font=("Cascadia Code", 14, "bold"),
        bg="#FEFBEA"
    ).pack(pady=10)

    # label untuk menampilkan kode Morse dengan wrapping teks
    result_label = tk.Label(
        result_window, 
        text=translated_text, 
        wraplength=1000,
        bg="#ffffff",
        fg="#333333",
        font=("Cascadia Code", 12),
        relief="solid",
        padx=10,
        pady=10
    )
    result_label.pack(pady=10)

    # tombol untuk menutup jendela hasil
    close_button = tk.Button(
        result_window, 
        text="Close", 
        command=result_window.destroy,
        bg="#FAFAFA",
        fg="black",
        font=("Cascadia Code", 12),
        relief="groove"
    )
    close_button.pack(pady=20)

# inisialisasi GUI utama
root = tk.Tk()
root.title("Morse Code Translator Program")  # Judul program
root.geometry("500x200")  # Ukuran jendela utama
root.configure(bg="#FEFBEA")  # Warna latar belakang

# kamus Morse Code
morse_dict = { 
  'A':'.-', 
  'B':'-...', 
  'C':'-.-.', 
  'D':'-..', 
  'E':'.', 
  'F':'..-.', 
  'G':'--.', 
  'H':'....', 
  'I':'..', 
  'J':'.---', 
  'K':'-.-', 
  'L':'.-..', 
  'M':'--', 
  'N':'-.', 
  'O':'---', 
  'P':'.--.', 
  'Q':'--.-', 
  'R':'.-.', 
  'S':'...', 
  'T':'-', 
  'U':'..-', 
  'V':'...-', 
  'W':'.--', 
  'X':'-..-', 
  'Y':'-.--', 
  'Z':'--..', 
  '1':'.----', 
  '2':'..---', 
  '3':'...--', 
  '4':'....-', 
  '5':'.....', 
  '6':'-....', 
  '7':'--...', 
  '8':'---..', 
  '9':'----.', 
  '0':'-----', 
  ', ':'--..--', 
  '.':'.-.-.-', 
  '?':'..--..', 
  '/':'-..-.', 
  '-':'-....-', 
  '(':'-.--.', 
  ')':'-.--.-', 
  '!':'-.-.--'
}

# label untuk instruksi input
tk.Label(
    root, 
    text="Enter text to translate to Morse Code:", 
    font=("Cascadia Code", 12, "bold"),
    bg="#FEFBEA"
).pack(pady=10)

# lnput teks dari user
entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=5)

# tombol untuk mengonversi teks ke kode Morse
convert_button = tk.Button(
    root, 
    text="Translate", 
    command=convert_to_morse, 
    bg="#FAFAFA", 
    fg="Black", 
    font=("Cascadia Code", 12),
    relief="groove"
)
convert_button.pack(pady=15)

# Jalankan GUI utama
root.mainloop()