from PIL import Image, ImageFilter, ImageDraw, ImageFont


def one():
    image = Image.open("star platinum.jpg")

    image.show("star platinum.jpg")

    width, height = image.size

    print("Размер изоборадения: {}px x {}px".format(width, height))

    format = image.format

    print("Формат файла: {}".format(format))

    model = image.mode

    print("Цветовая модель: {}".format(model))


def two():
    image = Image.open("star platinum.jpg")

    width, height = image.size

    new_img = (width // 3, height // 3)
    small_img = image.resize(new_img)
    small_img.save("small_img.png")

    horizontal_img = image.transpose(method=Image.FLIP_LEFT_RIGHT)
    horizontal_img.save("horizontal_img.png")

    vertical_img = image.transpose(method=Image.FLIP_TOP_BOTTOM)
    vertical_img.save("vertical_img.png")

    small_img.show("small_img.png")
    horizontal_img.show("horizontal_img.png")
    vertical_img.show("vertical_img.png")


def three():
    imgs = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for file in imgs:
        with Image.open(file) as img:
            img.load()
            new_img = img.filter(ImageFilter.EMBOSS)
            new_img.show()
            new_img.save("new_" + file)


def four():
    img = Image.open("1.jpg").convert("RGBA")
    txt = Image.new('RGBA', img.size, (225, 225, 225, 0))

    draw = ImageDraw.Draw(txt)
    font = ImageFont.truetype("impact.ttf", 40)
    draw.text((384, 500), "Watermark", fill=(0, 0, 0, 90), font=font)

    combined = Image.alpha_composite(img, txt)
    combined.show()
    combined.save("watermark1.png")

# one()
# two()
# three()
# four()
