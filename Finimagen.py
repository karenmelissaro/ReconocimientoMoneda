import cv2

image = cv2.load_image_file('./img/Imagenesnuevas/nueva.jpg')
face_locations = cv2.face_locations(image)


print(f'Existe{len(face_locations)} imagenes de la moneda')