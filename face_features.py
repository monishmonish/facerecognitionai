import PIL.Image
import PIL.ImageDraw
#PIL-Python Image Library
#call the PIL Module attributes seperately

#make sure to install dlib for face recognition
import face_recognition

#creating an image object
image=face_recognition.load_image_file("test.jpg")

#find all facial features as landmarks
face_features_group=face_recognition.face_landmarks(image)

#estimating no.of.faces
number_of_faces=len(face_features_group)

#print("I found {} face in this photo".format(number_of_faces))

#converting image into PIL Image for ML
pil_converted_image=PIL.Image.fromarray(image)

#overall pil image draw object
draw=PIL.ImageDraw.Draw(pil_converted_image)


for x in face_features_group:
    for name,list_of_points in x.items():
        print("The {} in this face has the following points : {}".format(name,list_of_points))
        draw.line(list_of_points,fill="red",width=2)

#displaying the output image
pil_converted_image.show()