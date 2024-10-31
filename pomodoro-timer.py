from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Set initial time values
pomodoroTime = 1500  # 25 minutes
breakTime = 300      # 5 minutes
timeRemaining = pomodoroTime  # Start with the Pomodoro time
isRunning = False   # Control flag to stop and start the timer

# Create the main window with ttkbootstrap theme
window = ttk.Window(themename = "cosmo")  # Try other themes like 'darkly', 'superhero'
window.geometry("400x200")
window.title("Pomodoro Timer")

# Display the time on the label
timeDisplayLabel = ttk.Label(window, text = "25:00", font=("Helvetica", 48, "bold"), bootstyle = "primary")
timeDisplayLabel.pack(pady=(20, 10))

# Update timer function
def updateTimer():
    global timeRemaining, isRunning
    if isRunning and timeRemaining > 0:
        # Display the time remaining
        minutes = int(timeRemaining / 60)
        seconds = timeRemaining % 60
        timeDisplay = f"{minutes:02}:{seconds:02}"
        timeDisplayLabel.config(text=timeDisplay)
        timeRemaining -= 1
        window.after(1000, updateTimer)  # Schedule the next countdown
    elif isRunning and timeRemaining == 0:
        # When time is up and timer is running, start the break timer
        timeDisplayLabel.config(text = "Time's up!", bootstyle = "danger")
        startBreak()  # Call break timer function

# Start the break timer
def startBreak():
    global timeRemaining, is_ruisRunningnning
    timeRemaining = breakTime
    updateBreakTimer()

# Update break timer function
def updateBreakTimer():
    global timeRemaining, isRunning
    if isRunning and timeRemaining > 0:
        minutes = int(timeRemaining / 60)
        seconds = timeRemaining % 60
        timeDisplay = f"{minutes:02}:{seconds:02}"
        timeDisplayLabel.config(text = timeDisplay, bootstyle = "info")
        timeRemaining -= 1
        window.after(1000, updateBreakTimer)
    elif isRunning and timeRemaining == 0:
        # End of break, display message
        timeDisplayLabel.config(text = "Break Over!", bootstyle = "success")

# Start the session timer
def startSession():
    global timeRemaining, isRunning
    timeRemaining = pomodoroTime
    isRunning = True  # Set running flag to True to start the timer
    timeDisplayLabel.config(bootstyle = "primary")  # Reset label style
    updateTimer()  # Start the main timer countdown

# Stop the timer
def stopTimer():
    global isRunning
    isRunning = False  # Set running flag to False to stop the timer

def resumeTimer():
    global isRunning
    isRunning = True

    if timeRemaining > breakTime:  # If remaining time is more than break time, we're in pomodoro
        updateTimer()
    else:
        updateBreakTimer()

# Add Start, Resume, and Stop buttons with ttkbootstrap styling
buttonFrame = ttk.Frame(window)
buttonFrame.pack(pady = 20)

startButton = ttk.Button(buttonFrame, text = "Start", command = startSession, bootstyle = "success-outline")
startButton.grid(row = 0, column = 0, padx = 5)

resumeButton = ttk.Button(buttonFrame, text = "Resume", command = resumeTimer, bootstyle = "info-outline")
resumeButton.grid(row = 0, column = 1, padx = 5)

stopButton = ttk.Button(buttonFrame, text = "Stop", command = stopTimer, bootstyle = "danger-outline")
stopButton.grid(row = 0, column = 2, padx = 5)

window.mainloop()