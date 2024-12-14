import tkinter as tk
from tkinter import messagebox
import threading

class WritingAppWithTwist:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Writing App with a Twist")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")  # Dark background
        self.timer_duration = 5  # Default timer in seconds
        self.timer = self.timer_duration
        self.typing = False

        self.create_ui()
        self.reset_timer()

        self.root.mainloop()

    def create_ui(self):
        # Header Label
        header = tk.Label(
            self.root, text="Writing App with a Twist", font=("Helvetica", 24, "bold"),
            bg="#34495e", fg="white", pady=10
        )
        header.pack(fill=tk.X)

        # Text Box
        self.text_box = tk.Text(
            self.root, wrap=tk.WORD, font=("Courier New", 14), undo=True,
            bg="#ecf0f1", fg="#2c3e50", insertbackground="#2c3e50"
        )
        self.text_box.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        self.text_box.bind("<Key>", self.reset_timer)

        # Settings Frame
        self.settings_frame = tk.Frame(self.root, bg="#2c3e50")
        self.settings_frame.pack(fill=tk.X, padx=20, pady=10)

        self.timer_label = tk.Label(
            self.settings_frame, text="Timer Duration (sec):", font=("Helvetica", 12),
            bg="#2c3e50", fg="white"
        )
        self.timer_label.pack(side=tk.LEFT, padx=5)

        self.timer_entry = tk.Entry(
            self.settings_frame, width=5, font=("Helvetica", 12),
            bg="#bdc3c7", fg="#2c3e50", justify="center"
        )
        self.timer_entry.insert(0, str(self.timer_duration))
        self.timer_entry.pack(side=tk.LEFT, padx=5)

        self.apply_button = tk.Button(
            self.settings_frame, text="Apply", font=("Helvetica", 12),
            bg="#1abc9c", fg="white", activebackground="#16a085",
            command=self.update_timer
        )
        self.apply_button.pack(side=tk.LEFT, padx=5)

    def update_timer(self):
        try:
            new_timer = int(self.timer_entry.get())
            if new_timer > 0:
                self.timer_duration = new_timer
                self.reset_timer()
            else:
                messagebox.showerror("Invalid Input", "Timer duration must be a positive number.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

    def reset_timer(self, event=None):
        self.typing = True
        self.timer = self.timer_duration
        if not hasattr(self, 'timer_thread') or not self.timer_thread.is_alive():
            self.timer_thread = threading.Thread(target=self.countdown, daemon=True)
            self.timer_thread.start()

    def countdown(self):
        while self.timer > 0:
            self.timer -= 1
            self.update_title()
            self.root.update()
            self.root.after(1000)
            if not self.typing:
                break
        if self.timer == 0:
            self.delete_text()

    def update_title(self):
        self.root.title(f"Writing App with a Twist - {self.timer}s Remaining")

    def delete_text(self):
        self.text_box.delete("1.0", tk.END)
        self.root.title("Writing App with a Twist - Draft Deleted!")
        messagebox.showinfo("Time's Up!", "You stopped typing. Your draft has been deleted.")
        self.reset_timer()

if __name__ == "__main__":
    WritingAppWithTwist()
