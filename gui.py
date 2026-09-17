
# Import Tkinter for creating the graphical user interface
import tkinter as tk

# Import LED from gpiozero to control the Raspberry Pi GPIO pins
from gpiozero import LED

# Define the GPIO pins connected to each LED
living_room = LED(14)
bathroom = LED(15)
closet = LED(18)


# Function to turn an individual LED ON or OFF
def toggle_led(led, button):
    # Check if the LED is currently ON
    if led.is_lit:
        # Turn the LED OFF
        led.off()

        # Change the button text and color to show OFF
        button.config(text="OFF", bg="red")
    else:
        # Turn the LED ON
        led.on()

        # Change the button text and color to show ON
        button.config(text="ON", bg="green")


# Function to turn all LEDs ON
def all_on():
    # Turn each LED ON
    living_room.on()
    bathroom.on()
    closet.on()

    # Update all buttons to show ON
    living_button.config(text="ON", bg="green")
    bathroom_button.config(text="ON", bg="green")
    closet_button.config(text="ON", bg="green")


# Function to turn all LEDs OFF
def all_off():
    # Turn each LED OFF
    living_room.off()
    bathroom.off()
    closet.off()

    # Update all buttons to show OFF
    living_button.config(text="OFF", bg="red")
    bathroom_button.config(text="OFF", bg="red")
    closet_button.config(text="OFF", bg="red")


# Function to safely close the program
def close_program():
    # Turn all LEDs OFF before closing
    living_room.off()
    bathroom.off()
    closet.off()

    # Close the Tkinter window
    root.destroy()


# Create the main Tkinter window
root = tk.Tk()

# Set the title of the window
root.title("Home LED Control")

# Set the window size
root.geometry("500x500")

# Set the background color
root.configure(bg="#222222")


# Create the main title
title = tk.Label(
    root,
    text="HOME LIGHT CONTROL",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#222222"
)

# Display the title with some space above and below
title.pack(pady=25)


# Create the Living Room label
living_label = tk.Label(
    root,
    text="Living Room  -  GPIO 14",
    font=("Arial", 16),
    fg="white",
    bg="#222222"
)

# Display the Living Room label
living_label.pack(pady=5)


# Create the Living Room ON/OFF button
living_button = tk.Button(
    root,
    text="OFF",
    font=("Arial", 16, "bold"),
    width=12,
    bg="red",
    fg="white",

    # Call toggle_led when the button is clicked
    command=lambda: toggle_led(living_room, living_button)
)

# Display the Living Room button
living_button.pack(pady=10)


# Create the Bathroom label
bathroom_label = tk.Label(
    root,
    text="Bathroom  -  GPIO 15",
    font=("Arial", 16),
    fg="white",
    bg="#222222"
)

# Display the Bathroom label
bathroom_label.pack(pady=5)


# Create the Bathroom ON/OFF button
bathroom_button = tk.Button(
    root,
    text="OFF",
    font=("Arial", 16, "bold"),
    width=12,
    bg="red",
    fg="white",

    # Call toggle_led when the button is clicked
    command=lambda: toggle_led(bathroom, bathroom_button)
)

# Display the Bathroom button
bathroom_button.pack(pady=10)


# Create the Closet label
closet_label = tk.Label(
    root,
    text="Closet  -  GPIO 18",
    font=("Arial", 16),
    fg="white",
    bg="#222222"
)

# Display the Closet label
closet_label.pack(pady=5)


# Create the Closet ON/OFF button
closet_button = tk.Button(
    root,
    text="OFF",
    font=("Arial", 16, "bold"),
    width=12,
    bg="red",
    fg="white",

    # Call toggle_led when the button is clicked
    command=lambda: toggle_led(closet, closet_button)
)

# Display the Closet button
closet_button.pack(pady=10)


# Create a frame to hold the ALL ON and ALL OFF buttons
frame = tk.Frame(root, bg="#222222")

# Display the frame
frame.pack(pady=25)


# Create the ALL ON button
all_on_button = tk.Button(
    frame,
    text="ALL ON",
    font=("Arial", 14, "bold"),
    width=10,
    bg="blue",
    fg="white",

    # Call all_on when the button is clicked
    command=all_on
)

# Place the ALL ON button on the left side
all_on_button.pack(side="left", padx=10)


# Create the ALL OFF button
all_off_button = tk.Button(
    frame,
    text="ALL OFF",
    font=("Arial", 14, "bold"),
    width=10,
    bg="gray",
    fg="white",

    # Call all_off when the button is clicked
    command=all_off
)

# Place the ALL OFF button on the left side
all_off_button.pack(side="left", padx=10)


# Make sure the LEDs are turned OFF when the user closes the window
root.protocol("WM_DELETE_WINDOW", close_program)

# Start the Tkinter event loop
root.mainloop()


