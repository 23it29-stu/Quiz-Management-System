import customtkinter as ctk
from tkinter import messagebox
import time

from database import DatabaseManager


class TakeQuiz:

    def __init__(self, parent, student_name, quiz_name):

        # -----------------------------
        # Parent Window
        # -----------------------------

        self.parent = parent
        self.student_name = student_name
        self.quiz_name = quiz_name

        # -----------------------------
        # Database
        # -----------------------------

        self.db = DatabaseManager()

        # -----------------------------
        # Get Quiz Details
        # -----------------------------

        quiz = self.db.get_quiz_details(quiz_name)

        if quiz is None:

            messagebox.showerror(
                "Error",
                "Quiz not found."
            )

            return

        self.quiz_id = quiz[0]
        self.quiz_name = quiz[1]
        self.category = quiz[2]
        self.description = quiz[3]
        self.difficulty = quiz[4]
        self.time_limit = quiz[5]
        self.pass_percentage = quiz[6]
        self.total_questions = quiz[7]

        if self.time_limit is None:
            self.time_limit = 5

        if self.pass_percentage is None:
            self.pass_percentage = 40

        # -----------------------------
        # Load Questions
        # -----------------------------

        self.questions = self.db.get_questions(
            self.quiz_name
        )

        if len(self.questions) == 0:

            messagebox.showerror(
                "Error",
                "This quiz has no questions."
            )

            return

        # -----------------------------
        # Variables
        # -----------------------------

        self.current_question = 0

        self.option_var = ctk.StringVar()

        self.selected_answers = {}

        self.score = 0

        self.timer_running = True

        self.remaining_seconds = int(
            self.time_limit
        ) * 60

        self.start_time = time.time()

        # -----------------------------
        # Quiz Window
        # -----------------------------

        self.window = ctk.CTkToplevel(parent)

        self.window.title("Take Quiz")

        self.window.geometry("1100x720")

        self.window.resizable(True, True)

        self.window.grab_set()

        self.window.protocol(
            "WM_DELETE_WINDOW",
            self.on_window_close
        )

        # -----------------------------
        # Build UI
        # -----------------------------

        self.build_ui()

        self.load_question()

        self.update_timer()
        # ======================================================
    # BUILD USER INTERFACE
    # ======================================================

    def build_ui(self):

        # ---------------- Header ----------------

        header = ctk.CTkFrame(
            self.window,
            height=90,
            corner_radius=0
        )

        header.pack(fill="x")

        title = ctk.CTkLabel(
            header,
            text=self.quiz_name,
            font=("Segoe UI", 28, "bold")
        )

        title.pack(pady=(10, 5))

        info = ctk.CTkFrame(
            header,
            fg_color="transparent"
        )

        info.pack(fill="x", padx=25)

        self.student_label = ctk.CTkLabel(
            info,
            text=f"Student : {self.student_name}",
            font=("Segoe UI",16)
        )

        self.student_label.pack(side="left")

        self.timer_label = ctk.CTkLabel(
            info,
            text="Time Left : 00:00",
            font=("Segoe UI",16,"bold"),
            text_color="red"
        )

        self.timer_label.pack(side="right")

        # ---------------- Body ----------------

        body = ctk.CTkFrame(
            self.window,
            fg_color="transparent"
        )

        body.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

        self.progress_label = ctk.CTkLabel(
            body,
            text="",
            font=("Segoe UI",18,"bold")
        )

        self.progress_label.pack(anchor="w")

        self.question_label = ctk.CTkLabel(
            body,
            text="",
            wraplength=900,
            justify="left",
            font=("Segoe UI",24,"bold")
        )

        self.question_label.pack(
            anchor="w",
            pady=20
        )
                # ---------------- Options ----------------

        self.rb1 = ctk.CTkRadioButton(
            body,
            text="",
            variable=self.option_var,
            value=""
        )

        self.rb1.pack(anchor="w", pady=8)

        self.rb2 = ctk.CTkRadioButton(
            body,
            text="",
            variable=self.option_var,
            value=""
        )

        self.rb2.pack(anchor="w", pady=8)

        self.rb3 = ctk.CTkRadioButton(
            body,
            text="",
            variable=self.option_var,
            value=""
        )

        self.rb3.pack(anchor="w", pady=8)

        self.rb4 = ctk.CTkRadioButton(
            body,
            text="",
            variable=self.option_var,
            value=""
        )

        self.rb4.pack(anchor="w", pady=8)

        # ---------------- Bottom Buttons ----------------

        bottom = ctk.CTkFrame(
            self.window,
            fg_color="transparent"
        )

        bottom.pack(
            fill="x",
            pady=20
        )

        self.previous_btn = ctk.CTkButton(
            bottom,
            text="⬅ Previous",
            width=180,
            command=self.previous_question
        )

        self.previous_btn.pack(
            side="left",
            padx=30
        )

        self.next_btn = ctk.CTkButton(
            bottom,
            text="Next ➜",
            width=180,
            command=self.next_question
        )

        self.next_btn.pack(
            side="right",
            padx=30
        )

        self.submit_btn = ctk.CTkButton(
            bottom,
            text="✅ Submit Quiz",
            width=180,
            fg_color="green",
            command=self.finish_quiz
        )

        self.submit_btn.pack_forget()
        # ======================================================
    # LOAD QUESTION
    # ======================================================

    def load_question(self):

        q = self.questions[self.current_question]

        self.progress_label.configure(
            text=f"Question {self.current_question + 1} of {len(self.questions)}"
        )

        self.question_label.configure(
            text=q[0]
        )

        # Set radio button text & values
        self.rb1.configure(
            text=q[1],
            value=q[1]
        )

        self.rb2.configure(
            text=q[2],
            value=q[2]
        )

        self.rb3.configure(
            text=q[3],
            value=q[3]
        )

        self.rb4.configure(
            text=q[4],
            value=q[4]
        )

        # Restore previous answer if available
        if self.current_question in self.selected_answers:

            self.option_var.set(
                self.selected_answers[self.current_question]
            )

        else:

            self.option_var.set("")

        # Previous button
        if self.current_question == 0:

            self.previous_btn.configure(
                state="disabled"
            )

        else:

            self.previous_btn.configure(
                state="normal"
            )

        # Last question
        if self.current_question == len(self.questions) - 1:

            self.next_btn.pack_forget()

            self.submit_btn.pack(
                side="right",
                padx=30
            )

        else:

            self.submit_btn.pack_forget()

            self.next_btn.pack(
                side="right",
                padx=30
            )
        # ======================================================
    # NEXT QUESTION
    # ======================================================

    def next_question(self):

        # Save answer if selected
        self.selected_answers[self.current_question] = self.option_var.get()

        # Move ahead even if nothing selected
        if self.current_question < len(self.questions) - 1:

            self.current_question += 1

            self.load_question()
        # ======================================================
    # PREVIOUS QUESTION
    # ======================================================

    def previous_question(self):

        # Save current answer
        self.selected_answers[self.current_question] = self.option_var.get()

        if self.current_question > 0:

            self.current_question -= 1

            self.load_question()
        # ======================================================
    # TIMER
    # ======================================================

    def update_timer(self):

        if not self.timer_running:
            return

        minutes = self.remaining_seconds // 60

        seconds = self.remaining_seconds % 60

        self.timer_label.configure(
            text=f"Time Left : {minutes:02}:{seconds:02}"
        )

        if self.remaining_seconds <= 0:

            self.timer_running = False

            messagebox.showinfo(
                "Time Up",
                "Time is over.\nYour quiz has been submitted automatically."
            )

            self.finish_quiz()

            return

        self.remaining_seconds -= 1

        self.window.after(
            1000,
            self.update_timer
        )
        # ======================================================
    # WINDOW CLOSE
    # ======================================================

    def on_window_close(self):

        if messagebox.askyesno(
            "Exit Quiz",
            "Do you want to submit the quiz before exiting?"
        ):

            self.finish_quiz()

        else:

            self.timer_running = False

            self.window.destroy()
        # ======================================================
    # FINISH QUIZ
    # ======================================================

    def finish_quiz(self):

        # Stop timer
        if not self.timer_running:
            return

        self.timer_running = False

        # Save current answer
        self.selected_answers[self.current_question] = self.option_var.get()

        # -------------------------------
        # Calculate Score
        # -------------------------------

        self.score = 0
        skipped = 0
        wrong = 0

        self.review_data = []

        for i, q in enumerate(self.questions):

            question = q[0]
            option1 = q[1]
            option2 = q[2]
            option3 = q[3]
            option4 = q[4]
            correct = str(q[5]).strip().lower()

            if correct == "option a":
                correct_answer = q[1]

            elif correct == "option b":
                correct_answer = q[2]

            elif correct == "option c":
                correct_answer = q[3]

            elif correct == "option d":
                correct_answer = q[4]

            else:
                correct_answer = q[5]

            user_answer = str(
                self.selected_answers.get(i, "")
            ).strip()

            if user_answer == "":
                skipped += 1

            elif user_answer == correct_answer:
                self.score += 1

            else:
                wrong += 1

            self.review_data.append({

                "question": question,

                "option1": option1,

                "option2": option2,

                "option3": option3,

                "option4": option4,

                "correct": correct_answer,

                "user": user_answer

            })

        total_questions = len(self.questions)

        percentage = round(
            (self.score / total_questions) * 100,
            2
        )

        status = "PASS"

        if percentage < self.pass_percentage:
            status = "FAIL"

        # -------------------------------
        # Time Taken
        # -------------------------------

        total_seconds = int(
            time.time() - self.start_time
        )

        minutes = total_seconds // 60
        seconds = total_seconds % 60

        time_taken = f"{minutes} min {seconds} sec"

        # -------------------------------
        # Save Result
        # -------------------------------

        self.db.save_result(

            self.student_name,

            self.quiz_id,

            self.score,

            percentage,

            status,

            time_taken

        )

        # Close Quiz Window

        self.window.destroy()

        # Show Result Window

        self.show_result_window(

            total_questions,

            skipped,

            wrong,

            percentage,

            status,

            time_taken

        )
        # ======================================================
    # RESULT WINDOW
    # ======================================================

    def show_result_window(

        self,

        total_questions,

        skipped,

        wrong,

        percentage,

        status,

        time_taken

    ):

        result = ctk.CTkToplevel(self.parent)

        result.title("Quiz Result")

        result.geometry("600x650")

        result.grab_set()

        heading = ctk.CTkLabel(

            result,

            text="🎉 QUIZ COMPLETED",

            font=("Segoe UI",30,"bold")

        )

        heading.pack(pady=20)
        ctk.CTkLabel(

            result,

            text=f"Student : {self.student_name}",

            font=("Segoe UI",18)

        ).pack(pady=5)

        ctk.CTkLabel(

            result,

            text=f"Quiz : {self.quiz_name}",

            font=("Segoe UI",18)

        ).pack(pady=5)

        ctk.CTkLabel(

            result,

            text=f"Total Questions : {total_questions}",

            font=("Segoe UI",18)

        ).pack(pady=5)

        ctk.CTkLabel(

            result,

            text=f"Correct Answers : {self.score}",

            font=("Segoe UI",18)

        ).pack(pady=5)

        ctk.CTkLabel(

            result,

            text=f"Wrong Answers : {wrong}",

            font=("Segoe UI",18)

        ).pack(pady=5)

        ctk.CTkLabel(

            result,

            text=f"Skipped Questions : {skipped}",

            font=("Segoe UI",18)

        ).pack(pady=5)

        ctk.CTkLabel(

            result,

            text=f"Percentage : {percentage}%",

            font=("Segoe UI",18)

        ).pack(pady=5)

        color = "green"

        if status == "FAIL":
            color = "red"

        ctk.CTkLabel(

            result,

            text=f"Status : {status}",

            text_color=color,

            font=("Segoe UI",24,"bold")

        ).pack(pady=10)

        ctk.CTkLabel(

            result,

            text=f"Time Taken : {time_taken}",

            font=("Segoe UI",18)

        ).pack(pady=5)
        button_frame = ctk.CTkFrame(

            result,

            fg_color="transparent"

        )

        button_frame.pack(pady=30)

        ctk.CTkButton(

            button_frame,

            text="Review Answers",

            width=180,

            command=self.review_answers

        ).grid(row=0,column=0,padx=15)

        ctk.CTkButton(

            button_frame,

            text="Close",

            width=180,

            command=result.destroy

        ).grid(row=0,column=1,padx=15)
        # ======================================================
    # REVIEW ANSWERS
    # ======================================================

    def review_answers(self):

        review = ctk.CTkToplevel(self.parent)

        review.title("Review Answers")

        review.geometry("950x700")

        review.grab_set()

        heading = ctk.CTkLabel(
            review,
            text="Review Your Answers",
            font=("Segoe UI", 28, "bold")
        )

        heading.pack(pady=15)

        # Scrollable Frame

        scroll = ctk.CTkScrollableFrame(
            review,
            width=900,
            height=580
        )

        scroll.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        for i, q in enumerate(self.review_data):

            card = ctk.CTkFrame(
                scroll,
                corner_radius=12
            )

            card.pack(
                fill="x",
                padx=10,
                pady=10
            )

            # Question Number

            ctk.CTkLabel(
                card,
                text=f"Question {i+1}",
                font=("Segoe UI",18,"bold")
            ).pack(anchor="w", padx=15, pady=(10,5))

            # Question

            ctk.CTkLabel(
                card,
                text=q["question"],
                wraplength=800,
                justify="left",
                font=("Segoe UI",17)
            ).pack(anchor="w", padx=15)

            # Options

            ctk.CTkLabel(
                card,
                text="A. " + q["option1"]
            ).pack(anchor="w", padx=30)

            ctk.CTkLabel(
                card,
                text="B. " + q["option2"]
            ).pack(anchor="w", padx=30)

            ctk.CTkLabel(
                card,
                text="C. " + q["option3"]
            ).pack(anchor="w", padx=30)

            ctk.CTkLabel(
                card,
                text="D. " + q["option4"]
            ).pack(anchor="w", padx=30)

            user = q["user"]

            if user == "":
                user = "Not Attempted"

            ctk.CTkLabel(
                card,
                text="Your Answer : " + user,
                font=("Segoe UI",16,"bold")
            ).pack(anchor="w", padx=15, pady=(10,0))

            ctk.CTkLabel(
                card,
                text="Correct Answer : " + q["correct"],
                font=("Segoe UI",16,"bold")
            ).pack(anchor="w", padx=15)

            # Result

            if user == "Not Attempted":

                status = "⚪ Not Attempted"
                color = "gray"

            elif user == q["correct"]:

                status = "✅ Correct"
                color = "green"

            else:

                status = "❌ Incorrect"
                color = "red"

            ctk.CTkLabel(
                card,
                text=status,
                text_color=color,
                font=("Segoe UI",17,"bold")
            ).pack(anchor="w", padx=15, pady=(5,10))
        # ======================================================
    # CLOSE DATABASE
    # ======================================================

    def __del__(self):

        try:
            self.db.close()

        except:
            pass