from rembg import remove
from PIL import Image
def bg_remove(img_path: str, out_path: str):
    input_image = Image.open(img_path)
    output = remove(input_image)
    output.save(out_path)