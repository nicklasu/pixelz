from PIL import Image
# "Wiki-sisters" by oekaki is licensed under CC BY-SA 3.0
# Link: https://commons.wikimedia.org/wiki/File:Wiki-sisters.png


def blur(img):
    px = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            if x % 10:
                px[x, y] = px[x - 1, y - 3]


def pixel(img):
    px = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            if x % 5:
                px[x, y] = px[x - 1, y]


def wild(img):
    px = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            if x % 500:
                px[x, y] = px[x - 1, y - 1]


if __name__ == '__main__':
    with Image.open("Wiki-sisters.png") as im:
        # Try different settings by uncommenting
        # You can run multiple functions at once

        # blur(im)
        pixel(im)
        # wild(im)
        im.show()
