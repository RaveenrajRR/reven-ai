from typing import Self

import customtkinter as ctk
import threading
import math

# ----------------------------
# CustomTkinter Settings
# ----------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def show_listening_window():
    def run():
        app = ctk.CTk()
        app.title("AI Assistant")

        WIDTH = 500
        HEIGHT = 250

        # ----------------------------
        # Center Window
        # ----------------------------
        screen_width = app.winfo_screenwidth()
        screen_height = app.winfo_screenheight()

        x = (screen_width - WIDTH) // 2
        y = (screen_height - HEIGHT) // 2

        app.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
        app.resizable(False, False)
        app.overrideredirect(True)
        app.attributes("-topmost", True)

        # ----------------------------
        # Main Frame
        # ----------------------------
        frame = ctk.CTkFrame(
            app,
            fg_color="#101010",
            corner_radius=25,
            border_width=2,
            border_color="#00BFFF"
        )
        frame.pack(fill="both", expand=True, padx=5, pady=5)

        # ----------------------------
        # Version Label
        # ----------------------------
        version_label = ctk.CTkLabel(
            frame,
            text="v0",
            font=("Arial", 10),
            text_color="#FDFBFB"
        )

        version_label.place(
            relx=0.97,
            rely=0.94,
            anchor="se"
        )

        # ----------------------------
        # Canvas
        # ----------------------------
        Self.title("AI Assistant")
        canvas = ctk.CTkCanvas(
            frame,
            bg="#101010",
            highlightthickness=0
        )
        canvas.pack(fill="both", expand=True)

        angle = 0

        def animate():
            nonlocal angle

            canvas.delete("all")

            canvas.update_idletasks()

            canvas_width = canvas.winfo_width()
            canvas_height = canvas.winfo_height()

            center_x = canvas_width // 2
            center_y = canvas_height // 2

            # ----------------------------
            # Wave Settings
            # ----------------------------
            wave_count = 31
            spacing = 10
            bar_width = 8

            total_width = (wave_count - 1) * spacing + bar_width
            start_x = center_x - total_width // 2

            for i in range(wave_count):

                # Symmetric smooth animation
                distance = abs(i - wave_count / 2)

                amplitude = max(20, 75 - distance * 3)

                height = (
                    18
                    + abs(
                        math.sin(angle * 0.18 + i * 0.45)
                    ) * amplitude
                )

                # Neon gradient
                if i < wave_count // 3:
                    color = "#00FFFF"
                elif i < 2 * wave_count // 3:
                    color = "#00BFFF"
                else:
                    color = "#0080FF"

                x1 = start_x + i * spacing
                y1 = center_y - height / 2
                x2 = x1 + bar_width
                y2 = center_y + height / 2

                canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=color,
                    outline=""
                )

            angle += 4

            app.after(16, animate)

        animate()

        app.after(4000, app.destroy)

        app.mainloop()

    threading.Thread(target=run, daemon=True).start()


# ----------------------------
# Test
# ----------------------------
if __name__ == "__main__":
    show_listening_window()

    while True:
        pass