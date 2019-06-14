import face_recognition

#loading the image file
image=face_recognition.load_image_file("test.jpg")

#generating face encodings
face_encodings=face_recognition.face_encodings(image)

if len(face_encodings)==0:
    print("No Faces Found")
    #if no faces is there..or if face_recognition coiuld'nt find any face..it shows result length as 0
else:
    encoding_value=face_encodings
    print(encoding_value)

#the above else loop shows encoding data for all faces
#to seperate if for every single face
for x in range(len(face_encodings)):
    encoding_value=face_encodings[x]
    print("The Encoding value for Face {} is :\n".format(x+1))
    print(encoding_value)

#each data set of encoded face value contains 128 values