import customtkinter as ctk

# Настройка темы
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

def check_letters():
    target = "алмаз"
    word = entry.get()  # Берем текст из поля ввода
    result_text = ""
    
    for letter in word:
        if letter in target:
            result_text += f"{letter}: YES\n"
        else:
            result_text += f"{letter}: NO\n"
            
    result_label.configure(text=result_text) # Выводим результат на экран

# Создание окна
app = ctk.CTk()
app.title("Проверка букв")
app.geometry("300x400")

# Элементы интерфейса
label = ctk.CTkLabel(app, text="Введите слово:")
label.pack(pady=10)

entry = ctk.CTkEntry(app, placeholder_text="Писать сюда...")
entry.pack(pady=10)

button = ctk.CTkButton(app, text="Проверить", command=check_letters)
button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", justify="left")
result_label.pack(pady=20)

app.mainloop()
