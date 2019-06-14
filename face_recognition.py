import face_recognition

#loading images to recognize with others
image=face_recognition.load_image_file("s3.jpg")

#get face encodings
face_encodings=face_recognition.face_encodings(image)
#this contains all face encoded values..for one face use .face_encodings(image)[0]

known_face_encodings=face_encodings
#for multiple_images..
#known_face_encodings=[face_encodings1,face_encodings2,face_encodings3,.....]

#loading the unknown face
unknown_image=face_recognition.load_image_file("unknown.img")

#getting face encodings for unknown image
unknown_image_encodings=face_recognition.face_encodings(unknown_image)

for x in unknown_image_encodings:
    results=euclidean_distance_value=face_recognition.compare_faces(face_encodings,unknown_image_encodings)
    #it compares faces using euclidean distance (vector space)
    #refer 12th maths
    #threshold value for result is 0.6//universal..surfed in many sites
    name="Unknown Face"
    if results:
        name="Its the same Face!"
    print(name)
    #for multiple image inputs
    '''
    if results[0]:
        name="Face1"
    elif results[1]:
        name="Face2"
    elif results[3]:
        name="Face3"
        
    ...
    print("Found "+name+" In The Photo")
    '''


