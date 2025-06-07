import tkinter as tk
from tkinter import messagebox
import openai
import os

# Set your OpenAI API key (replace 'your-api-key' with your actual key)
openai.api_key = os.getenv("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")
# Function to generate recipe
def generate_recipe():
    ingredients = input_text.get("1.0", "end").strip()
    if not ingredients:
        messagebox.showwarning("Input Error", "Please enter ingredients or cuisine type.")
        return

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert chef who creates delicious and practical recipes."},
                {"role": "user", "content": f"Generate a recipe using the following ingredients or for this cuisine: {ingredients}"}
            ],
            temperature=0.7,
            max_tokens=500
        )

        recipe = response['choices'][0]['message']['content']
        output_text.delete("1.0", "end")
        output_text.insert("1.0", recipe)

    except Exception as e:
        messagebox.showerror("API Error", f"An error occurred:\n{e}")

# GUI setup
root = tk.Tk()
root.title("AI Chef - Recipe Generator")
root.geometry("600x500")
root.config(padx=10, pady=10)

title_label = tk.Label(root, text="AI Chef 👨‍🍳", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

desc_label = tk.Label(root, text="Enter ingredients or cuisine type below:")
desc_label.pack()

input_text = tk.Text(root, height=5, width=70)
input_text.pack(pady=5)

generate_button = tk.Button(root, text="Generate Recipe", command=generate_recipe)
generate_button.pack(pady=10)

output_label = tk.Label(root, text="Generated Recipe:")
output_label.pack()

output_text = tk.Text(root, height=15, width=70)
output_text.pack(pady=5)

root.mainloop()
