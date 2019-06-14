import PIL.Image
import PIL.ImageDraw
#PIL-Python Image Library
#call the PIL Module attributes seperately

#make sure to install dlib for face recognition
import face_recognition

#creating an image object
image=face_recognition.load_image_file("test.jpg")

#recognizing faces using face_recognition module usng HOG (Histogram of Oriented Gradients)
face_locations=face_recognition.face_locations(image)

#estimating no.of.faces
number_of_faces=len(face_locations)

print("I found {} face in this photo".format(number_of_faces))

#converting image into PIL Image for ML
pil_converted_image=PIL.Image.fromarray(image)

for x in face_locations:
    left , top , right , bottom = x
    print("A Face is located at Pixel Location Top:{} ,Right:{} ,Bottom:{} ,Left:{}".format(top,right,bottom,left))
    drawImage=PIL.ImageDraw.Draw(pil_converted_image)
    drawImage.rectangle([top,right,bottom,left],outline="orange")

#displaying the output image
pil_converted_image.show()