import customtkinter as ctk
from tkinter import messagebox

from create_quiz import CreateQuiz
from database import DatabaseManager
from theme import *


class Home:

    def __init__(self):

        # ---------------- Window ----------------
        self.root = ctk.CTk()
        self.root.title("Quiz Management System")
        self.root.geometry("1000x700")
        self.root.configure(fg_color=BACKGROUND)
        self.root.resizable(True, True)

        # ---------------- Database ----------------
        self.db = DatabaseManager()

        # ---------------- Build UI ----------------
        self.create_header()
        self.create_body()

    # ==========================================================
    # Header
    # ==========================================================

    def create_header(self):

        header = ctk.CTkFrame(
            self.root,
            fg_color=PRIMARY,
            corner_radius=0,
            height=120
        )
        header.pack(fill="x")

        title = ctk.CTkLabel(
            header,
            text="🎓 QUIZ MANAGEMENT SYSTEM",
            font=TITLE_FONT,
            text_color="white"
        )
        title.pack(pady=(25, 5))

        subtitle = ctk.CTkLabel(
            header,
            text="Learn • Create • Test • Improve",
            font=SUBTITLE_FONT,
            text_color="white"
        )
        subtitle.pack()

    # ==========================================================
    # Body
    # ==========================================================

    def create_body(self):

        body = ctk.CTkFrame(
            self.root,
            fg_color=BACKGROUND
        )
        body.pack(fill="both", expand=True)

        self.card = ctk.CTkFrame(
            body,
            width=760,
            height=430,
            fg_color="white",
            corner_radius=20
        )

        self.card.pack(pady=30)
        self.card.pack_propagate(False)

        # Welcome
        welcome = ctk.CTkLabel(
            self.card,
            text="Welcome!",
            font=("Segoe UI", 28, "bold"),
            text_color=TEXT
        )
        welcome.pack(pady=(25, 5))

        description = ctk.CTkLabel(
            self.card,
            text="Create your own quizzes or attempt existing quizzes.",
            font=("Segoe UI", 14),
            text_color="gray40"
        )
        description.pack(pady=(0, 20))

        # ---------------- Name ----------------

        name_label = ctk.CTkLabel(
            self.card,
            text="Enter Your Name",
            font=LABEL_FONT,
            text_color=TEXT
        )
        name_label.pack()

        self.name_entry = ctk.CTkEntry(
            self.card,
            width=420,
            height=40,
            placeholder_text="Type your name..."
        )
        self.name_entry.pack(pady=(5, 20))

        # ---------------- Quiz ----------------

        quiz_label = ctk.CTkLabel(
            self.card,
            text="Select Quiz",
            font=LABEL_FONT,
            text_color=TEXT
        )
        quiz_label.pack()

        self.quiz_combo = ctk.CTkComboBox(
            self.card,
            width=420,
            height=40,
            values=["Loading..."]
        )
        self.quiz_combo.pack(pady=(5, 25))

        # Load quiz names
        self.load_quizzes()

        # ---------------- Buttons ----------------

        button_frame = ctk.CTkFrame(
            self.card,
            fg_color="transparent"
        )
        button_frame.pack()

        start_btn = ctk.CTkButton(
            button_frame,
            text="Start Quiz",
            width=170,
            height=42,
            fg_color=PRIMARY,
            command=self.start_quiz
        )
        start_btn.grid(row=0, column=0, padx=10, pady=10)

        create_btn = ctk.CTkButton(
            button_frame,
            text="Create Quiz",
            width=170,
            height=42,
            fg_color="#10B981",
            hover_color="#059669",
            command=self.create_quiz
        )
        create_btn.grid(row=0, column=1, padx=10, pady=10)

        result_btn = ctk.CTkButton(
            button_frame,
            text="View Results",
            width=170,
            height=42,
            fg_color="#F59E0B",
            hover_color="#D97706",
            command=self.view_results
        )
        result_btn.grid(row=1, column=0, padx=10, pady=10)

        exit_btn = ctk.CTkButton(
            button_frame,
            text="Exit",
            width=170,
            height=42,
            fg_color="#EF4444",
            hover_color="#DC2626",
            command=self.root.destroy
        )
        exit_btn.grid(row=1, column=1, padx=10, pady=10)

    # ==========================================================
    # Functions
    # ==========================================================

    def load_quizzes(self):

        try:
            quizzes = self.db.get_all_quizzes()

            if quizzes:
                quiz_names = [quiz[0] for quiz in quizzes]
                self.quiz_combo.configure(values=quiz_names)
                self.quiz_combo.set(quiz_names[0])
            else:
                self.quiz_combo.configure(values=["No Quiz Available"])
                self.quiz_combo.set("No Quiz Available")

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def start_quiz(self):
        print("Button Clicked")

        name = self.name_entry.get().strip()

        if name == "":
            messagebox.showerror(
                "Error",
                "Please enter your name."
            )
            return

        quiz_name = self.quiz_combo.get()

        from take_quiz import TakeQuiz

        TakeQuiz(
            self.root,
            name,
            quiz_name
        )

        TakeQuiz(
            self.root,
            name,
            quiz_name
        )

    def create_quiz(self):
        from create_quiz import CreateQuiz
        CreateQuiz(self.root, self.load_quizzes)

    def view_results(self):

     from results import Results

     Results(self.root)
    # ==========================================================
    # Run
    # ==========================================================

    def run(self):
        self.root.mainloop()