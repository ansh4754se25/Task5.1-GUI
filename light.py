import tkinter as tk
from gpiozero import LED

# Set up the three LEDs using their BCM GPIO pin numbers.
leds = {
    "Living Room": LED(14),
    "Bathroom": LED(15),
    "Closet": LED(18),
}

def select_room(room):
    """Turn on the selected room's LED and turn the others off."""
    for name, led in leds.items():
        if name == room:
            led.on()   # Turn on the LED for the selected room.
        else:
            led.off()  # Turn off the LEDs for the other rooms.

def close_app():
    """Turn off and release the LEDs, then close the window."""
    for led in leds.values():
        led.off()    # Make sure every light is off before exiting.
        led.close()  # Release the GPIO pin.
    root.destroy()   # Close the Tkinter window.

# Create the main application window.
root = tk.Tk()
root.title("Room Lights")             # Set the window title.
root.geometry("320x240")              # Set the window size.
root.resizable(False, False)          # Prevent resizing the window.

# Add a heading above the room choices.
tk.Label(
    root,
    text="Select a room light",
    font=("Arial", 16)
).pack(pady=15)

# Store the currently selected room for the radio buttons.
selected_room = tk.StringVar(value="")

# Add one radio button for each room.
for room in leds:
    tk.Radiobutton(
        root,
        text=room,                     # Text shown beside the radio button.
        variable=selected_room,        # Shared variable for the room choices.
        value=room,                    # Value set when this room is selected.
        command=lambda name=room: select_room(name),  # Update the LEDs.
        font=("Arial", 12)
    ).pack(anchor="w", padx=70, pady=4)

# Add a button to turn off the LEDs and close the application.
tk.Button(
    root,
    text="Exit",
    command=close_app
).pack(pady=18)

# Start the GUI event loop so the window stays open and responds to clicks.
root.mainloop()