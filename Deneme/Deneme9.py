from PIL import Image, ImageOps, ImageChops

# İlk görüntüyü yükle
img1 = Image.open("Output/Deneme8_norm_before.png").convert("L")

# Histogram eşitleme yap
img1 = ImageOps.equalize(img1)

# İkinci görüntüyü yükle
img2 = Image.open("Output/Deneme8_norm_after.png").convert("L")

# Histogram eşitleme yap
img2 = ImageOps.equalize(img2)

# İki görüntü arasındaki farkı al
diff = ImageChops.difference(img1, img2)


img1.save("Output/Deneme9_im1.png")
img2.save("Output/Deneme9_im2.png")

# Fark görüntüsünü kaydet
diff.save("Output/Deneme9_fark.png")