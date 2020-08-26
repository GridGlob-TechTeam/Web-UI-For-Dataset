import cv2 

def click_event(event, x, y, flags, coordinates):
	if event == cv2.EVENT_LBUTTONDOWN:
		coordinates.append(x)
		coordinates.append(y)
		print(x, ' ', y)
		print(coordinates)

def read_Image(file):
	img = cv2.imread(file, 1)
	img = cv2.resize(img,(512,512))
	cv2.imshow('image', img) 

	coordinates = []
	cv2.setMouseCallback('image', click_event, coordinates)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
	x,y,w,h = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
	if(y>h):
		y,h = h,y
	if(x>w):
		x,w = w,x
	crop_img = img[y:h, x:w]
	cv2.imshow("cropped", crop_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows() 

	return None



if __name__=="__main__": 
	
	file = 'img.jpg'
	a = read_Image(file)
