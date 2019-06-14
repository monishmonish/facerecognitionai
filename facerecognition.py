import face_recognition
import pathlib
import PIL.ImageDraw
import PIL.Image

#loading the image
known_image=face_recognition.load_image_file("//IMAGE FILE")

#encoded value for known image
known_image_encoded_value=face_recognition.face_encodings(known_image)[0]
#for first single face
#for multiple face remove [0] and modify the code

#setting up default paramaters
best_image= None
best_euclidean_distance=0.6

#to scan and compare all images in a folder using pathlib library
for image_location in Path("//DirecoryName").glob("*png","*jpg"):
    #loading unknown image to compare
    unknown_image=face_recognition.load_image_file(image_location)
    #getting face locations manually for more accuracy
    unknown_image_face_locations=face_recognition.face_locations(unknown_image,number_of_times_to_upsample=2)
    #number_of_times_to_upsample=2 magnifies image 2 times for more accuracy to avoid small resolution error
    #getting face encodings
    unknown_image_encoded_value=face_recognition.face_encodings(unknown_image,known_face_locations=unknown_image_face_locations)
    #comparing 2 images using euclidean distnce
    euclidean_distance=face_recognition.compare_faces(unknown_image_encoded_value,known_image_encoded_value)[0]
    # for multiple face remove [0] and modify the code
    #update to sort the best results further
    if euclidean_distance<best_euclidean_distance:
        best_euclidean_distance=euclidean_distance
        best_image=unknown_image

#displaying image in pil
pil_converted_image=PIL.Image.fromarray(best_image)
pil_converted_image.show()

