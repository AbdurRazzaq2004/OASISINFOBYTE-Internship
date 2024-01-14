import tkinter as tk
import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {query}")
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, query)
    except Exception as e:
        print("Sorry, I didn't catch that. Can you please repeat?")
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, "Sorry, I didn't catch that.")

# Create the GUI window
window = tk.Tk()
window.title("Voice Assistant")

# Create the GUI elements
label = tk.Label(window, text="Speak:")
label.pack()

text_output = tk.Text(window, height=5, width=30)
text_output.pack()

button = tk.Button(window, text="Record", command=listen)
button.pack()

# Start the GUI event loop
window.mainloop()