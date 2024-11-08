from tkinter import *
import time

# ---------------------------------Constants----------------------
PINK = "#ff1685"
PURPLE = "#b916ff"
BLUE = "#9216ff"
ORANGE = "#ff7c27"
YELLOW = "#ffe736"

# Create the main window (root)
root = Tk()
root.title("Exercise Video")
root.config(padx=100, pady=50, bg=YELLOW)

frame = Frame(root, bd=5, relief="solid", highlightbackground=PURPLE, highlightcolor=PURPLE)
frame.grid(row=0, column=0)

# Create a canvas
canvas = Canvas(root, width=500, height=480, bg=ORANGE)
canvas.grid(row=0, column=0, columnspan=2)  # Place canvas on the grid

# --------------------- Pictures ------------------------------------------------------
# Load images
double_tap_img = PhotoImage(file=r"C:\Users\ruffd\Documents\TESD-1800\final_project\images\double_tap.png", width=448,
                            height=569)
elbow_knee_img = PhotoImage(file=r"C:\Users\ruffd\Documents\TESD-1800\final_project\images\elbow_knee.png", width=448,
                            height=569)
flutter_img = PhotoImage(file=r"C:\Users\ruffd\Documents\TESD-1800\final_project\images\flutter.png", width=448,
                         height=569)
knee_roll_in_img = PhotoImage(file=r"C:\Users\ruffd\Documents\TESD-1800\final_project\images\knee_roll_in.png",
                              width=448, height=569)
single_leg_img = PhotoImage(file=r"C:\Users\ruffd\Documents\TESD-1800\final_project\images\single_leg.png", width=448,
                            height=569)
single_tap_img = PhotoImage(file=r"C:\Users\ruffd\Documents\TESD-1800\final_project\images\single_tap.png", width=448,
                            height=569)

# Create image objects on canvas and store the image ID
image_on_canvas = canvas.create_image(250, 200, image=single_tap_img)  # Initially display single_tap_img


# --------------------------------Timer--------------------------------------------

# TimerApp Class to handle the countdown timer
class TimerApp:
    def __init__(self, root):
        self.root = root 
        self.root.title("Timer App")

        self.time_left = 240  # Set initial time for the countdown (in seconds)

        # Create a label to display the time
        self.time_label = Label(self.root, text="Time Remaining: 04:00", bg=PINK, font=("Arial", 24))
        self.time_label.grid(row=1, column=0, columnspan=2)  # Place the timer label on the grid

        # Create a button to start the countdown
        self.start_button = Button(self.root, text="Start Timer", bg=BLUE, command=self.start_timer, width=20)
        self.start_button.grid(row=2, column=0, columnspan=2)

    def start_timer(self):
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            time_str = f"{mins:02}:{secs:02}"
            self.time_label.config(text=f"Time Remaining: {time_str}")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)  # Schedule this method to run after 1 second

            # Switch images based on time_left
            if self.time_left == 200:
                canvas.itemconfig(image_on_canvas, image=single_leg_img)
            elif self.time_left == 160:
                canvas.itemconfig(image_on_canvas, image=elbow_knee_img)
            elif self.time_left == 120:
                canvas.itemconfig(image_on_canvas, image=flutter_img)
            elif self.time_left == 80:
                canvas.itemconfig(image_on_canvas, image=double_tap_img)
            elif self.time_left == 40:
                canvas.itemconfig(image_on_canvas, image=knee_roll_in_img)



        else:
            self.time_label.config(text="Time's Up!")



# Create an instance of TimerApp
app = TimerApp(root)

# Start the Tkinter event loop
root.mainloop()

#
#