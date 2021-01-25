# Tandin Wangchuk

import face_recognition
from PIL import Image, ImageDraw

#k5
image_of_k5 = face_recognition.load_image_file('./known/k5.jpg')
k5_face_encoding = face_recognition.face_encodings(image_of_k5)[0]

#queen
image_of_queen = face_recognition.load_image_file('./known/queen.jpg')
dechen_face_encoding = face_recognition.face_encodings(image_of_queen)[0]

# array of encoding and name
known_face_encoding = [
    k5_face_encoding,
    dechen_face_encoding
]

known_face_name = [
    "King Jigme K. ",
    "Azhi Jetsun Pema"
]

#load image to test
image_test = face_recognition.load_image_file('./unknown/4.jpg')

#find faces in image_test
face_locations = face_recognition.face_locations(image_test)
face_encodings = face_recognition.face_encodings(image_test, face_locations)

#convert to PIL  format
pil_image = Image.fromarray(image_test)

#ImageDraw instance
draw = ImageDraw.Draw(pil_image)

#loop through faces in Image_test
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    
    matches = face_recognition.compare_faces(known_face_encoding, face_encoding, tolerance=0.5) 

    name = "unknown person"
    
    #if match replace name from known_face_name array
    if True in matches:
        match_index = matches.index(True)
        name = known_face_name[match_index]

    #draw box
    draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

    #draw box and name
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))

#delete draw instance 
del draw

#show image
pil_image.show()

#save image
pil_image.save('identify.jpg')