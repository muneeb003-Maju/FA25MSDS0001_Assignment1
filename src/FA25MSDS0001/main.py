from logger import logger

from utils import validate_name
from utils import validate_marks

from services import calculate_grade


def main():
    logger.info("Application started")

    name = input("Enter student name: ")

    if not validate_name(name):
        logger.warning("Empty student name entered")
        print("Error: Name cannot be empty.")
        return

    try:
        marks = int(input("Enter student marks: "))
    except ValueError:
        logger.error("Invalid marks entered")
        print("Error: Marks must be a number.")
        return

    if not validate_marks(marks):
        logger.warning(f"Invalid marks entered: {marks}")
        print("Error: Marks must be between 0 and 100.")
        return

    grade = calculate_grade(marks)

    logger.info("Student report generated")

    print()
    print("Student Report")
    print("================")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()