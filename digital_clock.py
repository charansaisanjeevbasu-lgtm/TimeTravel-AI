import tkinter as tk
from tkinter import font
from datetime import datetime
import pytz

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock - Multiple Time Zones")
        self.root.geometry("800x400")
        self.root.configure(bg="#1a1a1a")
        
        # Define time zones to display
        self.time_zones = [
            ("New York (EST)", "America/New_York"),
            ("London (GMT)", "Europe/London"),
            ("Tokyo (JST)", "Asia/Tokyo"),
            ("Sydney (AEDT)", "Australia/Sydney"),
            ("Dubai (GST)", "Asia/Dubai"),
            ("Los Angeles (PST)", "America/Los_Angeles"),
        ]
        
        # Create main frame
        main_frame = tk.Frame(root, bg="#1a1a1a")
        main_frame.pack(pady=20)
        
        # Title
        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        title_label = tk.Label(main_frame, text="Digital Clock - Multiple Time Zones", 
                               font=title_font, fg="#00ff00", bg="#1a1a1a")
        title_label.pack(pady=10)
        
        # Create clock frames for each timezone
        self.clock_labels = {}
        clock_frame = tk.Frame(main_frame, bg="#1a1a1a")
        clock_frame.pack()
        
        for i, (city, tz) in enumerate(self.time_zones):
            # Create a frame for each timezone
            frame = tk.Frame(clock_frame, bg="#2a2a2a", relief=tk.RIDGE, bd=2)
            frame.grid(row=i//3, column=i%3, padx=10, pady=10)
            
            # City name
            city_font = font.Font(family="Helvetica", size=12, weight="bold")
            city_label = tk.Label(frame, text=city, font=city_font, 
                                 fg="#00ff00", bg="#2a2a2a")
            city_label.pack(pady=5)
            
            # Time display
            time_font = font.Font(family="Courier", size=18, weight="bold")
            time_label = tk.Label(frame, text="00:00:00", font=time_font, 
                                 fg="#00ffff", bg="#2a2a2a")
            time_label.pack(pady=10, padx=20)
            
            self.clock_labels[tz] = time_label
        
        # Update time
        self.update_time()
    
    def update_time(self):
        """Update the time for all time zones"""
        for tz, label in self.clock_labels.items():
            # Get current time in specific timezone
            timezone = pytz.timezone(tz)
            time_now = datetime.now(timezone)
            time_string = time_now.strftime("%H:%M:%S")
            label.config(text=time_string)
        
        # Schedule next update (every 1000ms)
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()
