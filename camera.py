import cv2

camera = cv2.VideoCapture(0)

i=0
while (True):
    result, image = camera.read()

    # if result:
    #     cv2.imwrite(f"img/F_Humna{i}.png", image)

    cv2.imshow('frame', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i+=1


camera.release()
cv2.destroyAllWindows()