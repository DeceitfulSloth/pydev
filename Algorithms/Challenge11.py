# Python Challenge 11

from PIL import Image

image = Image.open("data\\11\\cave.jpg")

print(image.width, image.height)

evenImage = Image.new('RGB', (image.width // 2, image.height // 2))
oddImage = Image.new('RGB', (image.width // 2, image.height // 2))

for x in range(image.width):
    for y in range(image.height):
        pixelVal = image.getpixel((x,y))
        if (x + y) % 2 == 0:
            evenImage.putpixel((x//2,y//2), pixelVal)
        else:
            oddImage.putpixel((x//2,y//2), pixelVal)

evenImage.save('data\\11\\even.png')
oddImage.save('data\\11\\odd.png')
