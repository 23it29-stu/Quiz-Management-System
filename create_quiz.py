import customtkinter as ctk
from tkinter import messagebox
from database import DatabaseManager


class CreateQuiz:

    def __init__(self, parent, refresh_callback):

        self.parent = parent
        self.refresh_callback = refresh_callback

        self.db = DatabaseManager()

        self.questions = []

        self.window = ctk.CTkToplevel(parent)
        self.window.title("Create Quiz")
        self.window.geometry("850x650")
        self.window.resizable(True, True)
        self.window.grab_set()

        self.build_ui()

    # =======================================================
    # BUILD UI
    # =======================================================

    def build_ui(self):

        title = ctk.CTkLabel(
            self.window,
            text="CREATE NEW QUIZ",
            font=("Segoe UI", 26, "bold")
        )
        title.pack(pady=10)

        main = ctk.CTkFrame(
            self.window,
            fg_color="transparent"
        )

        main.pack(padx=15, pady=5)

        main.grid_columnconfigure(0, weight=1)
        main.grid_columnconfigure(1, weight=1)

        # ===================================================
        # QUIZ NAME
        # ===================================================

        ctk.CTkLabel(
            main,
            text="Quiz Name"
        ).grid(row=0, column=0, sticky="w", pady=(5,2))

        self.quiz_name = ctk.CTkEntry(
            main,
            width=260
        )

        self.quiz_name.grid(
            row=1,
            column=0,
            padx=10
        )

        # ===================================================
        # CATEGORY
        # ===================================================

        ctk.CTkLabel(
            main,
            text="Category"
        ).grid(row=0, column=1, sticky="w", pady=(5,2))

        self.category = ctk.CTkEntry(
            main,
            width=260
        )

        self.category.grid(
            row=1,
            column=1,
            padx=10
        )

        # ===================================================
        # DESCRIPTION
        # ===================================================

        ctk.CTkLabel(
            main,
            text="Description"
        ).grid(row=2, column=0, sticky="w", pady=(10,2))

        self.description = ctk.CTkEntry(
            main,
            width=260
        )

        self.description.grid(
            row=3,
            column=0,
            padx=10
        )

        # ===================================================
        # DIFFICULTY
        # ===================================================

        ctk.CTkLabel(
            main,
            text="Difficulty"
        ).grid(row=2, column=1, sticky="w", pady=(10,2))

        self.difficulty = ctk.CTkComboBox(
            main,
            values=[
                "Easy",
                "Medium",
                "Hard"
            ],
            width=260
        )

        self.difficulty.set("Easy")

        self.difficulty.grid(
            row=3,
            column=1,
            padx=10
        )

        # ===================================================
        # TIME LIMIT
        # ===================================================

        ctk.CTkLabel(
            main,
            text="Time Limit (Minutes)"
        ).grid(row=4, column=0, sticky="w", pady=(10,2))

        self.time_limit = ctk.CTkComboBox(
            main,
            values=[
                "5",
                "10",
                "15",
                "20",
                "30",
                "45",
                "60"
            ],
            width=260
        )

        self.time_limit.set("10")

        self.time_limit.grid(
            row=5,
            column=0,
            padx=10
        )

        # ===================================================
        # PASSING PERCENTAGE
        # ===================================================

        ctk.CTkLabel(
            main,
            text="Passing Percentage"
        ).grid(row=4, column=1, sticky="w", pady=(10,2))

        self.pass_percentage = ctk.CTkEntry(
            main,
            width=260,
            placeholder_text="40"
        )

        self.pass_percentage.grid(
            row=5,
            column=1,
            padx=10
        )

        self.pass_percentage.insert(0, "40")
                # ===================================================
        # QUESTION
        # ===================================================

        ctk.CTkLabel(
            main,
            text="Question"
        ).grid(
            row=6,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(15, 3)
        )

        self.question = ctk.CTkEntry(
            main,
            width=560
        )

        self.question.grid(
            row=7,
            column=0,
            columnspan=2,
            padx=10,
            pady=(0, 8)
        )

        # ===================================================
        # OPTION A
        # ===================================================

        ctk.CTkLabel(
            main,
            text="Option A"
        ).grid(
            row=8,
            column=0,
            sticky="w",
            pady=(8,2)
        )

        self.option1 = ctk.CTkEntry(
            main,
            width=260
        )

        self.option1.grid(
            row=9,
            column=0,
            padx=10
        )

        # ===================================================
        # OPTION B
        # ===================================================

        ctk.CTkLabel(
            main,
            text="Option B"
        ).grid(
            row=8,
            column=1,
            sticky="w",
            pady=(8,2)
        )

        self.option2 = ctk.CTkEntry(
            main,
            width=260
        )

        self.option2.grid(
            row=9,
            column=1,
            padx=10
        )

        # ===================================================
        # OPTION C
        # ===================================================

        ctk.CTkLabel(
            main,
            text="Option C"
        ).grid(
            row=10,
            column=0,
            sticky="w",
            pady=(8,2)
        )

        self.option3 = ctk.CTkEntry(
            main,
            width=260
        )

        self.option3.grid(
            row=11,
            column=0,
            padx=10
        )

        # ===================================================
        # OPTION D
        # ===================================================

        ctk.CTkLabel(
            main,
            text="Option D"
        ).grid(
            row=10,
            column=1,
            sticky="w",
            pady=(8,2)
        )

        self.option4 = ctk.CTkEntry(
            main,
            width=260
        )

        self.option4.grid(
            row=11,
            column=1,
            padx=10
        )

        # ===================================================
        # CORRECT ANSWER
        # ===================================================

        ctk.CTkLabel(
            main,
            text="Correct Answer"
        ).grid(
            row=12,
            column=0,
            sticky="w",
            pady=(10,2)
        )

        self.correct = ctk.CTkComboBox(
            main,
            values=[
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            width=260
        )

        self.correct.set("Option A")

        self.correct.grid(
            row=13,
            column=0,
            padx=10,
            sticky="w"
        )

        # ===================================================
        # QUESTION COUNTER
        # ===================================================

        self.counter = ctk.CTkLabel(
            main,
            text="Questions Added : 0",
            font=("Segoe UI", 15, "bold")
        )

        self.counter.grid(
            row=14,
            column=0,
            columnspan=2,
            pady=10
        )

        # ===================================================
        # BUTTONS
        # ===================================================

        button_frame = ctk.CTkFrame(
            self.window,
            fg_color="transparent"
        )

        button_frame.pack(pady=(5,15))

        add_btn = ctk.CTkButton(
            button_frame,
            text="Add Question",
            width=170,
            command=self.add_question
        )

        add_btn.grid(
            row=0,
            column=0,
            padx=8
        )

        save_btn = ctk.CTkButton(
            button_frame,
            text="Save Quiz",
            width=170,
            fg_color="#16A34A",
            hover_color="#15803D",
            command=self.save_quiz
        )

        save_btn.grid(
            row=0,
            column=1,
            padx=8
        )

        back_btn = ctk.CTkButton(
            button_frame,
            text="Back",
            width=170,
            fg_color="#DC2626",
            hover_color="#B91C1C",
            command=self.window.destroy
        )

        back_btn.grid(
            row=0,
            column=2,
            padx=8
        )
            # =======================================================
    # ADD QUESTION
    # =======================================================

    def add_question(self):

        question = self.question.get().strip()

        option1 = self.option1.get().strip()

        option2 = self.option2.get().strip()

        option3 = self.option3.get().strip()

        option4 = self.option4.get().strip()

        correct = self.correct.get()

        # ================= Validation =================

        if question == "":
            messagebox.showerror(
                "Error",
                "Please enter a question."
            )
            return

        if option1 == "" or option2 == "" or option3 == "" or option4 == "":
            messagebox.showerror(
                "Error",
                "Please fill all four options."
            )
            return

        # ================= Store Question =================

        self.questions.append({

            "question": question,

            "option1": option1,

            "option2": option2,

            "option3": option3,

            "option4": option4,

            "correct": correct

        })

        # ================= Update Counter =================

        self.counter.configure(
            text=f"Questions Added : {len(self.questions)}"
        )

        # ================= Clear Fields =================

        self.question.delete(0, "end")

        self.option1.delete(0, "end")

        self.option2.delete(0, "end")

        self.option3.delete(0, "end")

        self.option4.delete(0, "end")

        self.correct.set("Option A")

        # ================= Success Message =================

        messagebox.showinfo(
            "Success",
            "Question added successfully!"
        )
        # ======================================================
    # SAVE QUIZ
    # ======================================================

    def save_quiz(self):

        quiz_name = self.quiz_name.get().strip()
        category = self.category.get().strip()
        description = self.description.get().strip()
        difficulty = self.difficulty.get()
        time_limit = self.time_limit.get()
        passing_percentage = self.pass_percentage.get().strip()

        # ================= Validation =================

        if quiz_name == "" or category == "":
            messagebox.showerror(
                "Error",
                "Quiz Name and Category are required."
            )
            return

        if description == "":
            description = "No Description"

        if passing_percentage == "":
            passing_percentage = 40

        try:
            passing_percentage = int(passing_percentage)
        except:
            messagebox.showerror(
                "Error",
                "Passing Percentage must be a number."
            )
            return

        if len(self.questions) == 0:
            messagebox.showerror(
                "Error",
                "Please add at least one question."
            )
            return

        total_questions = len(self.questions)

        try:

            # ================= Save Quiz =================

            quiz_id = self.db.add_quiz(
                quiz_name,
                category,
                description,
                difficulty,
                int(time_limit),
                passing_percentage,
                total_questions
            )

            # ================= Save Questions =================

            for q in self.questions:

                self.db.add_question(
                    quiz_id,
                    q["question"],
                    q["option1"],
                    q["option2"],
                    q["option3"],
                    q["option4"],
                    q["correct"]
                )

            messagebox.showinfo(
                "Success",
                "Quiz Created Successfully!"
            )

            # Refresh Home Screen Dropdown
            self.refresh_callback()

            # Close Window
            self.window.destroy()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )