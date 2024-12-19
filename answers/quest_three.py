import cv2

if __name__ == "__main__":
    image = cv2.imread("assets/black_rect.png")
    assert image is not None, "file could not be read, check with os.path.exists()"

    rect_pixels = []
    for p in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[p, j][0] == 0 and image[p, j][1] == 0 and image[p, j][2] == 0:
                rect_pixels.append([p, j])
    rect1 = [rect_pixels[0], rect_pixels[0]]
    for p in rect_pixels:
        if (p[0] == rect1[1][0] and p[1] == rect1[1][1] + 1) or (
            p[0] == rect1[1][0] + 1 and p[1] == rect1[1][1]
        ):
            rect1[1] = p
    
    new_pixels = rect_pixels[rect_pixels.index(rect1[1])+1:]
    print(new_pixels)
    rect2 = [new_pixels[0], new_pixels[0]]
    for n in new_pixels:
        if (n[0] == rect2[1][0] and n[1] == rect2[1][1] + 1) or (
            n[0] == rect2[1][0] + 1 and n[1] == rect2[1][1]
        ):
            rect2[1] = n
    
    output = f"rect1: {rect1}\nrect2: {rect2}"
    with open("output/rects.txt", "w") as f:
        f.write(output)
