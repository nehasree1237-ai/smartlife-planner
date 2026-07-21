import pandas as pd
import os

def save_student(student):
    df = pd.DataFrame([student])

    file_path = os.path.join("data", "students.csv")

    if os.path.exists(file_path):
        df.to_csv(file_path, mode="a", header=False, index=False)
    else:
        df.to_csv(file_path, index=False)