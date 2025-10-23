"""
Student Grade Management System.

This module provides a Student class for managing student grades,
calculating averages, determining letter grades, and generating reports.
"""


class Student:
    """
    Represents a student with grades and academic status.

    Attributes:
        student_id (str): The unique identifier for the student.
        name (str): The student's name.
        grades (list): List of numeric grades (0-100).
        is_passed (str): Pass/Fail status based on average grade.
        honor (bool): Whether the student is on the honor roll.
        letter_grade (str): Letter grade (A, B, C, D, F) based on average.
    """

    def __init__(self, student_id, name):
        """
        Initialize a new Student instance.

        Args:
            student_id (str): The unique identifier for the student.
            name (str): The student's name.

        Raises:
            ValueError: If student_id or name is empty.
        """
        if not student_id or not name:
            raise ValueError("Student ID and name cannot be empty")

        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = False
        self.letter_grade = "F"

    def add_grade(self, grade):
        """
        Add a grade to the student's grade list.

        Args:
            grade (float or int): The grade to add (must be 0-100).

        Raises:
            ValueError: If grade is not numeric or outside 0-100 range.
        """
        try:
            grade_value = float(grade)
            if not 0 <= grade_value <= 100:
                raise ValueError(f"Grade must be between 0 and 100, got {grade_value}")
            self.grades.append(grade_value)
        except (ValueError, TypeError) as error:
            raise ValueError(f"Invalid grade: {grade}. Must be a number between 0-100") from error

    def calculate_average(self):
        """
        Calculate the average of all grades.

        Returns:
            float: The average grade, or 0.0 if no grades exist.
        """
        if not self.grades:
            return 0.0

        total = sum(self.grades)
        average = total / len(self.grades)
        return average

    def determine_letter_grade(self):
        """
        Determine the letter grade based on average.

        Sets the letter_grade attribute based on the average:
        - A: 90-100
        - B: 80-89
        - C: 70-79
        - D: 60-69
        - F: <60

        Returns:
            str: The letter grade.
        """
        average = self.calculate_average()

        if average >= 90:
            self.letter_grade = "A"
        elif average >= 80:
            self.letter_grade = "B"
        elif average >= 70:
            self.letter_grade = "C"
        elif average >= 60:
            self.letter_grade = "D"
        else:
            self.letter_grade = "F"

        return self.letter_grade

    def determine_pass_fail(self):
        """
        Determine if the student passed or failed.

        Sets is_passed to "Passed" if average >= 60, otherwise "Failed".

        Returns:
            str: "Passed" or "Failed".
        """
        average = self.calculate_average()
        self.is_passed = "Passed" if average >= 60 else "Failed"
        return self.is_passed

    def check_honor(self):
        """
        Check if the student qualifies for the honor roll.

        Sets honor to True if average >= 90, otherwise False.

        Returns:
            bool: True if on honor roll, False otherwise.
        """
        average = self.calculate_average()
        self.honor = average >= 90
        return self.honor

    def delete_grade(self, identifier):
        """
        Delete a grade by value or by index.

        Args:
            identifier (float, int, or str): 
                - If numeric and < len(grades), treated as index
                - Otherwise, treated as grade value to remove

        Raises:
            ValueError: If grade value not found or index out of range.
        """
        try:
            # Try to use as index first
            if isinstance(identifier, int) and 0 <= identifier < len(self.grades):
                del self.grades[identifier]
                print(f"Grade at index {identifier} removed successfully")
                return

            # Try to use as value
            grade_value = float(identifier)
            if grade_value in self.grades:
                self.grades.remove(grade_value)
                print(f"Grade {grade_value} removed successfully")
            else:
                raise ValueError(f"Grade {grade_value} not found in grades list")

        except (ValueError, IndexError) as error:
            raise ValueError(f"Cannot delete grade: {identifier}. "
                           f"Either not found or invalid index.") from error

    def generate_report(self):
        """
        Generate and print a formatted student summary report.

        Displays:
        - Student ID
        - Student Name
        - Number of Grades
        - Average Grade
        - Letter Grade
        - Pass/Fail status
        - Honor Roll status
        """
        # Update all status fields before generating report
        average = self.calculate_average()
        self.determine_letter_grade()
        self.determine_pass_fail()
        self.check_honor()

        print("=" * 50)
        print("STUDENT SUMMARY REPORT")
        print("=" * 50)
        print(f"Student ID:      {self.student_id}")
        print(f"Student Name:    {self.name}")
        print(f"Number of Grades: {len(self.grades)}")
        print(f"Average Grade:   {average:.2f}")
        print(f"Letter Grade:    {self.letter_grade}")
        print(f"Pass/Fail:       {self.is_passed}")
        print(f"Honor Roll:      {'Yes' if self.honor else 'No'}")
        print("=" * 50)


def start_run():
    """
    Main function to demonstrate the Student class functionality.

    Creates a student, adds valid grades, and generates a report.
    Includes error handling for invalid operations.
    """
    try:
        # Create a student with valid data
        student = Student("S001", "John Doe")

        # Add valid grades
        student.add_grade(95.0)
        student.add_grade(88.5)
        student.add_grade(92.0)

        # Try to add an invalid grade (will raise an error)
        try:
            student.add_grade("Fifty")  # This will be caught
        except ValueError as error:
            print(f"Error adding grade: {error}")

        # Calculate and display average
        print(f"\nCurrent average: {student.calculate_average():.2f}")

        # Check honor status
        student.check_honor()

        # Try to delete a grade with invalid index (will be caught)
        try:
            student.delete_grade(10)  # Index out of range
        except ValueError as error:
            print(f"Error deleting grade: {error}")

        # Delete a valid grade
        try:
            student.delete_grade(0)  # Delete first grade
        except ValueError as error:
            print(f"Error: {error}")

        # Generate the final report
        print("\n")
        student.generate_report()

    except ValueError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    start_run()