import tkinter as tk
import time
import random

def typing_effect(canvas, text, start_x, start_y, delay=0.1):
    displayed_text = ""
    for char in text:
        displayed_text += char  # Add one character at a time
        canvas.delete("text_display")
        canvas.create_text(start_x, start_y, text=displayed_text, font=("Courier", 20), fill="black", tags="text_display")
        canvas.update()  # Update the canvas to show the new character
        time.sleep(delay)  # Pause for delay seconds between each character

def start_display():
    # Clear canvas
    canvas.delete("all")
    
    # Display "IT Discovery Day@KU KPS" with typing effect
    typing_effect(canvas, "IT Discovery Day@KU KPS", start_x=300, start_y=50, delay=0.1)
    
    # Wait for 1 second before showing the welcome message
    time.sleep(1)
    
    # Display the welcome message with typing effect
    typing_effect(canvas, "Welcome to IT Discovery Day@KU KPS!", start_x=300, start_y=100, delay=0.1)
    
    # Wait for 1 second before showing the next message
    time.sleep(1)
    
    # Display the suggestion message with typing effect
    typing_effect(canvas, "ขอแนะนำสาขาวิชา ก่อนนะ", start_x=300, start_y=150, delay=0.1)

     # Wait for 1 second before showing the next message
    time.sleep(1)
    
    # Display the suggestion message with typing effect
    typing_effect(canvas, "สาขาวิชาของเรา สาขาวิชาเทคโนโลยีสารสนเทศและการสื่อสาร ", start_x=300, start_y=150, delay=0.1)

    time.sleep(1)
    
    # Display the suggestion message with typing effect
    typing_effect(canvas, "หลักสูตร วิทยาศาสตรบัณฑิต สาขาวิชาเทคโนโลยีสารสนเทศ", start_x=300, start_y=150, delay=0.1)

     # Wait for 1 second before showing the next message
    time.sleep(1)
    
    # Display the suggestion message with typing effect
    typing_effect(canvas, "สังกัด ภาควิชาวิทยาการคำนวณและเทคโนโลยีดิจิทัล", start_x=300, start_y=150, delay=0.1)

     # Wait for 1 second before showing the next message
    time.sleep(1)
    
    # Display the suggestion message with typing effect
    typing_effect(canvas, "คณะศิลปศาสตร์และวิทยาศาสตร์ ", start_x=300, start_y=150, delay=0.1)

    time.sleep(1)
    
    # Display the suggestion message with typing effect
    typing_effect(canvas, "มหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตกำแพงแสน", start_x=300, start_y=150, delay=0.1)

     # Wait for 1 second before showing the next message
    time.sleep(1)
    
    # Display the suggestion message with typing effect
    typing_effect(canvas, "หวังว่าทุกคนที่เข้าร่วมงานในวันนี้จะมีโอกาสได้เข้ามาศึกษา ", start_x=300, start_y=150, delay=0.1)

    time.sleep(1)
    
    # Display the suggestion message with typing effect
    typing_effect(canvas, "ในรั้วมหาวิทยาลัยเกษตรศาสตร์ด้วยกันครับ ", start_x=300, start_y=150, delay=0.1)

# Create the main window
root = tk.Tk()
root.title("Display IT Discovery Day@KU KPS")

# Create a canvas to draw text
canvas = tk.Canvas(root, width=600, height=200)
canvas.pack()

# Create a button to start the display
start_button = tk.Button(root, text="Start", command=start_display)
start_button.pack()

# Run the Tkinter event loop
root.mainloop()
