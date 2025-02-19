import cv2

# Charger l'image
image = cv2.imread("image.jpg")

# Définir le nouveau facteur d'échelle
scale_factor = 4  # Agrandir 2x

# Redimensionner avec interpolation bicubique
upscaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

# Sauvegarder l'image améliorée
cv2.imwrite("image_upscaled.jpg", upscaled_image)

# Afficher l'image
cv2.imshow("Upscaled Image", upscaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
