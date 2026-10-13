import tkinter as tk 
import RPi.GPIO as GPIO 
 
# ---------------- GPIO SETUP ---------------- 
 
# GPIO pins connected to each room's LED 
LIVING_ROOM_PIN = 14 
BATHROOM_PIN = 15 
CLOSET_PIN = 18 
 
# Use BCM GPIO numbering 
GPIO.setmode(GPIO.BCM) 
 
# Configure all LED pins as outputs 
GPIO.setup(LIVING_ROOM_PIN, GPIO.OUT) 
GPIO.setup(BATHROOM_PIN, GPIO.OUT) 
GPIO.setup(CLOSET_PIN, GPIO.OUT) 
 
# Create separate PWM controllers for each LED 
# 1000 Hz provides smooth brightness control 
living_room_pwm = GPIO.PWM(LIVING_ROOM_PIN, 1000) 
bathroom_pwm = GPIO.PWM(BATHROOM_PIN, 1000) 
closet_pwm = GPIO.PWM(CLOSET_PIN, 1000) 
 
# Start all LEDs at 0% brightness 
living_room_pwm.start(0) 
bathroom_pwm.start(0) 
closet_pwm.start(0) 
 
 
# ---------------- FUNCTIONS ---------------- 
 
def change_living_room(value): 
    """Change the brightness of the living room light.""" 
    brightness = float(value) 
    living_room_pwm.ChangeDutyCycle(brightness) 
 
 
def change_bathroom(value): 
    """Change the brightness of the bathroom light.""" 
    brightness = float(value) 
    bathroom_pwm.ChangeDutyCycle(brightness) 
 
 
def change_closet(value): 
    """Change the brightness of the closet light.""" 
    brightness = float(value) 
    closet_pwm.ChangeDutyCycle(brightness) 
 
 
def turn_off_all(): 
    """Turn all three lights off.""" 
    living_room_slider.set(0) 
    bathroom_slider.set(0) 
    closet_slider.set(0) 
 
 
def cleanup(): 
    """Stop PWM, clean up GPIO and close the application.""" 
    living_room_pwm.stop() 
    bathroom_pwm.stop() 
    closet_pwm.stop() 
 
    GPIO.cleanup() 
    window.destroy() 
 
 
# ---------------- GUI SETUP ---------------- 
 
window = tk.Tk() 
window.title("Home Light Control") 
window.geometry("500x520") 
 
 
# ---------------- TITLE ---------------- 
 
title = tk.Label( 
    window, 
    text="Home Light Control", 
    font=("Arial", 20, "bold") 
) 
title.pack(pady=15) 
 
 
# ---------------- LIVING ROOM ---------------- 
 
living_room_label = tk.Label( 
    window, 
    text="Living Room", 
    font=("Arial", 14, "bold") 
) 
living_room_label.pack() 
 
living_room_slider = tk.Scale( 
    window, 
    from_=0, 
    to=100, 
    orient=tk.HORIZONTAL, 
    length=350, 
    label="Intensity", 
    command=change_living_room 
) 
living_room_slider.pack(pady=10) 
 
 
# ---------------- BATHROOM ---------------- 
 
bathroom_label = tk.Label( 
    window, 
    text="Bathroom", 
    font=("Arial", 14, "bold") 
) 
bathroom_label.pack() 
 
bathroom_slider = tk.Scale( 
    window, 
    from_=0, 
    to=100, 
    orient=tk.HORIZONTAL, 
    length=350, 
    label="Intensity", 
    command=change_bathroom 
) 
bathroom_slider.pack(pady=10) 
 
 
# ---------------- CLOSET ---------------- 
 
closet_label = tk.Label( 
    window, 
    text="Closet", 
    font=("Arial", 14, "bold") 
) 
closet_label.pack() 
 
closet_slider = tk.Scale( 
    window, 
    from_=0, 
    to=100, 
    orient=tk.HORIZONTAL, 
    length=350, 
    label="Intensity", 
    command=change_closet 
) 
closet_slider.pack(pady=10) 
 
 
# ---------------- BUTTONS ---------------- 
 
off_button = tk.Button( 
    window, 
    text="TURN OFF ALL", 
    width=20, 
    command=turn_off_all 
) 
off_button.pack(pady=15) 
 
 
exit_button = tk.Button( 
    window, 
    text="EXIT", 
    width=20, 
    command=cleanup 
) 
exit_button.pack(pady=5) 
 
 
# Clean up GPIO when the window is closed 
window.protocol("WM_DELETE_WINDOW", cleanup) 
 
# Start the GUI 
window.mainloop()        
