import cv2

# define a video capture object
camera = cv2.VideoCapture(0)

i=0
while (True):

    # Capture the video frame
    # by frame
    result, image = camera.read()

    if result:
        cv2.imwrite(f"img/Test_photo{i}.png", image)
    # Display the resulting frame
    cv2.imshow('frame', image)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i+=1

# After the loop release the cap object
camera.release()
# Destroy all the windows
cv2.destroyAllWindows()