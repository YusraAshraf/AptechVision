import cv2

name = 'Yusra'

cam = cv2.VideoCapture(0)

cv2.namedWindow("Press space to take a picture:" ,cv2.WINDOW_NORMAL)
cv2.resizeWindow("Press space to take a picture" ,500,500)

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab a frame")
        break
    cv2.imshow("Press space to take a picture",frame)
    
    k= cv2.waitKey(1)
    if k%256 == 27:
        print("Escape hit , closing....")
        break
    elif k%256 == 32:
        img_name = "dataset/" +name + "/image_{}.jpg" .format(img_counter)
        cv2.imwrite(img_name ,frame)
        print("{} written!" .format(img_name))
        img_counter += 1
cam.release()
cv2.destroyAllWindows()