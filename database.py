import mysql.connector
from tkinter import messagebox


class DatabaseManager:

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="quiz_user",
                password="Quiz@123",
                database="quiz_management"
            )

            self.cursor = self.connection.cursor()

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    # ======================================================
    # QUIZ METHODS
    # ======================================================

    def get_all_quizzes(self):

        sql = "SELECT quiz_name FROM quiz ORDER BY quiz_name"

        self.cursor.execute(sql)

        return self.cursor.fetchall()

    def get_quiz_details(self, quiz_name):

        sql = """
        SELECT
        quiz_id,
        quiz_name,
        category,
        description,
        difficulty,
        time_limit,
        passing_percentage,
        total_questions

        FROM quiz

        WHERE quiz_name=%s
        """

        self.cursor.execute(sql, (quiz_name,))

        return self.cursor.fetchone()

    def add_quiz(
            self,
            quiz_name,
            category,
            description,
            difficulty,
            time_limit,
            passing_percentage,
            total_questions):

        sql = """
        INSERT INTO quiz
        (
            quiz_name,
            category,
            description,
            difficulty,
            time_limit,
            passing_percentage,
            total_questions
        )

        VALUES(%s,%s,%s,%s,%s,%s,%s)
        """

        self.cursor.execute(sql, (

            quiz_name,
            category,
            description,
            difficulty,
            time_limit,
            passing_percentage,
            total_questions

        ))

        self.connection.commit()

        return self.cursor.lastrowid

    # ======================================================
    # QUESTION METHODS
    # ======================================================

    def add_question(
            self,
            quiz_id,
            question,
            option1,
            option2,
            option3,
            option4,
            correct_answer):

        sql = """
        INSERT INTO questions
        (
            quiz_id,
            question,
            option1,
            option2,
            option3,
            option4,
            correct_answer
        )

        VALUES(%s,%s,%s,%s,%s,%s,%s)
        """

        self.cursor.execute(sql, (

            quiz_id,
            question,
            option1,
            option2,
            option3,
            option4,
            correct_answer

        ))

        self.connection.commit()

    def get_questions(self, quiz_name):

        sql = """
        SELECT

        q.question,
        q.option1,
        q.option2,
        q.option3,
        q.option4,
        q.correct_answer,
        quiz.quiz_id

        FROM questions q

        JOIN quiz

        ON q.quiz_id=quiz.quiz_id

        WHERE quiz.quiz_name=%s
        """

        self.cursor.execute(sql, (quiz_name,))

        return self.cursor.fetchall()

    # ======================================================
    # RESULT METHODS
    # ======================================================

    def save_result(
            self,
            student_name,
            quiz_id,
            score,
            percentage,
            status,
            time_taken):

        sql = """
        INSERT INTO results
        (
            student_name,
            quiz_id,
            score,
            percentage,
            status,
            time_taken
        )

        VALUES(%s,%s,%s,%s,%s,%s)
        """

        self.cursor.execute(sql, (

            student_name,
            quiz_id,
            score,
            percentage,
            status,
            time_taken

        ))

        self.connection.commit()

    def get_results(self):

        sql = """
        SELECT

        results.student_name,
        quiz.quiz_name,
        results.score,
        results.percentage,
        results.status,
        results.time_taken,
        results.attempt_datetime

        FROM results

        JOIN quiz

        ON results.quiz_id=quiz.quiz_id

        ORDER BY results.attempt_datetime DESC
        """

        self.cursor.execute(sql)

        return self.cursor.fetchall()

    def get_attempt_history(self, student_name):

        sql = """
        SELECT

        quiz.quiz_name,
        results.score,
        results.percentage,
        results.status,
        results.time_taken,
        results.attempt_datetime

        FROM results

        JOIN quiz

        ON results.quiz_id=quiz.quiz_id

        WHERE results.student_name=%s

        ORDER BY results.attempt_datetime DESC
        """

        self.cursor.execute(sql, (student_name,))

        return self.cursor.fetchall()

    # ======================================================
    # SEARCH
    # ======================================================

    def search_quiz(self, keyword):

        sql = """
        SELECT quiz_name

        FROM quiz

        WHERE quiz_name LIKE %s

        ORDER BY quiz_name
        """

        self.cursor.execute(sql, ("%" + keyword + "%",))

        return self.cursor.fetchall()

    def get_categories(self):

        sql = """
        SELECT DISTINCT category

        FROM quiz

        ORDER BY category
        """

        self.cursor.execute(sql)

        return self.cursor.fetchall()

    def get_quiz_by_category(self, category):

        sql = """
        SELECT quiz_name

        FROM quiz

        WHERE category=%s

        ORDER BY quiz_name
        """

        self.cursor.execute(sql, (category,))

        return self.cursor.fetchall()

    # ======================================================
    # EXPORT
    # ======================================================

    def export_results(self):

        sql = """
        SELECT

        results.student_name,
        quiz.quiz_name,
        results.score,
        results.percentage,
        results.status,
        results.time_taken,
        results.attempt_datetime

        FROM results

        JOIN quiz

        ON results.quiz_id=quiz.quiz_id

        ORDER BY results.attempt_datetime DESC
        """

        self.cursor.execute(sql)

        return self.cursor.fetchall()

    # ======================================================
    # DASHBOARD
    # ======================================================

    def total_quizzes(self):

        self.cursor.execute(
            "SELECT COUNT(*) FROM quiz"
        )

        return self.cursor.fetchone()[0]

    def total_attempts(self):

        self.cursor.execute(
            "SELECT COUNT(*) FROM results"
        )

        return self.cursor.fetchone()[0]

    def highest_score(self):

        self.cursor.execute(
            "SELECT MAX(percentage) FROM results"
        )

        result = self.cursor.fetchone()[0]

        if result is None:
            return 0

        return result

    # ======================================================
    # CLOSE CONNECTION
    # ======================================================

    def close(self):

        if self.connection.is_connected():

            self.cursor.close()

            self.connection.close()