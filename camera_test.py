import cv2

camera = cv2.VideoCapture(0)

while True:
	ret, frame = camera.read()
	if not ret:
		break

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1)

	# Esc Key -> close window
	if key == 27:
		break

camera.release()
cv2.destroyAllWindows()
