from PIL import Image


def cutting(path_input, path_output):
    # image_path = 'images/1.jpg'
    img = Image.open(path_input)
    size = img.size
    width, height = img.size
    sq = min(width, height)
    sq_img = img.crop((0, 0, sq, sq))
    sq_img.thumbnail((480, 480))
    sq_img.save(path_output)



