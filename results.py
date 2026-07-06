import customtkinter as ctk
from tkinter import ttk

from database import DatabaseManager


class Results:

    def __init__(self, parent):

        self.db = DatabaseManager()

        self.window = ctk.CTkToplevel(parent)
        self.window.title("Quiz Results")
        self.window.geometry("900x600")
        self.window.resizable(False, False)
        self.window.grab_set()

        self.build_ui()
        self.load_results()

    # =====================================

    def build_ui(self):

        title = ctk.CTkLabel(
            self.window,
            text="QUIZ RESULTS",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(pady=20)

        # ---------------- Table Frame ----------------

        table_frame = ctk.CTkFrame(self.window)

        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = (
            "Student",
            "Quiz",
            "Score",
            "Percentage"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=15
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=180)

        self.tree.pack(fill="both", expand=True)

        # ---------------- Buttons ----------------

        button_frame = ctk.CTkFrame(
            self.window,
            fg_color="transparent"
        )

        button_frame.pack(pady=15)

        refresh_btn = ctk.CTkButton(
            button_frame,
            text="Refresh",
            width=180,
            command=self.load_results
        )

        refresh_btn.grid(row=0, column=0, padx=10)

        back_btn = ctk.CTkButton(
            button_frame,
            text="Back",
            width=180,
            fg_color="red",
            hover_color="#B91C1C",
            command=self.window.destroy
        )

        back_btn.grid(row=0, column=1, padx=10)

    # =====================================

    def load_results(self):

        # Clear old rows
        for row in self.tree.get_children():
            self.tree.delete(row)

        results = self.db.get_results()

        for result in results:

            self.tree.insert(
                "",
                "end",
                values=(
                    result[0],
                    result[1],
                    result[2],
                    f"{result[3]:.2f}%"
                )
            )