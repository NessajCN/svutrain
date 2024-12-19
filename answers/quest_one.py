import pandas as pd
import numpy as np
import cv2

if __name__ == "__main__":
    # Load the data
    employees = pd.read_csv(
        "assets/employees.csv",
        names=["employee_id", "name", "department", "salary"],
    )
    employees.sort_values(by=["salary"], inplace=True, ascending=False)

    # create a blank image
    image = np.zeros((200, 200, 3), np.uint8)

    # set text property
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255, 255, 255)
    thickness = 2

    # Put text on the image
    i = 1
    for _, row in employees.head(3).iterrows():
        cv2.putText(
            image,
            f"{i}. {row['name']}",
            (0, 50 * i),
            font,
            fontScale,
            color,
            thickness,
            cv2.LINE_AA,
        )
        i += 1
        
    # Save the image
    cv2.imwrite("output/employees.jpg", image)
