import cv2 #cv2 is the OpenCV library — it helps us work with images, videos, and webcams.

cap = cv2.VideoCapture(0)   
'''
cap = cv2.VideoCapture(0)
1)This starts the default webcam.
2)The 0 there is to access the primary camera. 
3)If there are multiple camera we can use number like 1,2..
4)cap is the object that lets us to read webcam frames.
'''
while True: # For testing purpose I used a infinite loop to keep showing the webcam.
    ret, frame = cap.read()
    ''' 
    cap.read() tries to read one frame from the webcam.
    It returns:
        1)ret → True if successful, False if something went wrong
        2)frame → the actual image from the webcam (like a NumPy array of pixels)
    '''
    
    if not ret: #we termination the operation if there is problem in camera.
        break
    
    cv2.imshow("Webcam Feed", frame) # Shows the frame (image from webcam) in a window titled "Webcam Feed".
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        """
        1)cv2.waitkey(1) waits 1 millisecond for a key press in each loop.
        2)0xFF is a bitwise AND with 0xFF, which is binary 11111111 (i.e., 255 in decimal).
          It extracts only the lowest 8 bits from the keycode.
          why we using this because some times cv2.waitkey returns more than 8 bits so by using the bitwise and(&) we
          ensure only the required 8 bits are returned and check with the q.
        3) ord('q') returns the ascii value of q.
        """
        break

cap.release() #This releases the webcam, so it stops using your camera
cv2.destroyAllWindows() # Closes all OpenCV windows that were opened (like the webcam feed window)
