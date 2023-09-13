

import tkinter as tk
import subprocess
import signal

root = tk.Tk()
root.title("Gesture controlled user interface")

heading_label = tk.Label(root, text="Gesture-Based Interface Control", font=("Arial", 24, "bold"))
heading_label.pack(pady=20)

process = None

def run_program(program_file):
    global process
    process = subprocess.Popen(['python', program_file])

def stop_program():
    global process
    if process:
        process.send_signal(signal.SIGTERM)
        process = None

# Card 1
frame1 = tk.Frame(root, padx=10, pady=10)
frame1.pack(side=tk.LEFT)

image1 = tk.PhotoImage(file="C:\major project\Media\eye.png")
# Resize the image to a smaller size
small_image1 = image1.subsample(2, 2)
label1 = tk.Label(frame1, image=small_image1)
label1.pack()

button1 = tk.Button(frame1, text="Run eye cursor", command=lambda: run_program("eyecursor.py"),bg="#03fca1")
button1.pack()

button1_stop = tk.Button(frame1, text="Stop eye cursor", command=stop_program,bg="#fc035e")
button1_stop.pack()

# Card 2
frame2 = tk.Frame(root, padx=10, pady=10)
frame2.pack(side=tk.LEFT)

image2 = tk.PhotoImage(file="C:\major project\Media\hand.png")
# Resize the image to a smaller size
small_image2 = image2.subsample(2, 2)
label2 = tk.Label(frame2, image=small_image2)
label2.pack()

button2 = tk.Button(frame2, text="Run hand gesture cursor", command=lambda: run_program("handgesturemouse.py"),bg="#03fca1")
button2.pack()

button2_stop = tk.Button(frame2, text="Stop hand gesture cursor", command=stop_program,bg="#fc035e")
button2_stop.pack()

# Card 3
frame3 = tk.Frame(root, padx=10, pady=10)
frame3.pack(side=tk.LEFT)

image3 = tk.PhotoImage(file="C:\major project\Media\joy.png")
# Resize the image to a smaller size
small_image3 = image3.subsample(2, 2)
label3 = tk.Label(frame3, image=small_image3)
label3.pack()

button3 = tk.Button(frame3, text="play game", command=lambda: run_program("subway.py"),bg="#03fca1")
button3.pack()

button3_stop = tk.Button(frame3, text="Stop game", command=stop_program,bg="#fc035e")
button3_stop.pack()

root.mainloop()
