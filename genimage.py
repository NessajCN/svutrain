import numpy as np
import cv2

if __name__ == "__main__":
    # create a blank image
    image = np.full((200, 200, 3),255, np.uint8)
    image[30:51, 40:61] = [0, 0, 0]
    image[110:181, 70:141] = [0, 0, 0]
    
    cv2.imwrite("assets/black_rect.png", image)