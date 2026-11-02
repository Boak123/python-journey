import logging

logging.basicConfig(
    filename="student.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started.")
logging.warning("Duplicate student registration.")
logging.error("Student record update failed.")