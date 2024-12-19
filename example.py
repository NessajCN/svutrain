import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    BLUE = [255,0,0]
    
    img1 = cv.imread('images/opencv-logo-white.png')
    assert img1 is not None, "file could not be read, check with os.path.exists()"
    
    print(img1[100,100])
    
    replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
    reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
    reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
    wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
    constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
    
    plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
    plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
    plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
    plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
    plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
    plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
    
    plt.show()
    
    # fig, ax = plt.subplots()
    # ax.plot([0, 5], [0, 5])

    # fig.canvas.draw()
    # img_plot = np.array(fig.canvas.renderer.buffer_rgba())

    # cv2.imshow("Image", cv2.cvtColor(img_plot, cv2.COLOR_RGBA2BGR))

    # cv2.waitKey(0)
