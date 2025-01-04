import os
import json
from PIL import Image

# para consulta
def get_files(filetypes: list, files_dir: str):
    """
        retorna lista de listas
    """
    files = [[f for f in os.listdir(files_dir) if f.endswith(type_)] for type_ in filetypes]
    return files

def load_json(filepath):
    f = open(filepath)
    json_data = json.load(f)
    f.close()
    return json_data
    
def save_tags(filepath, output_dir):
    json_data = load_json(filepath)
    file = os.path.basename(filepath)
    filename = os.path.splitext(file)[0]

    # l3 = [x for x in l1 if x not in l2]

    ftags = json_data["tags"]
    ftags = [tag.replace("_", " ") for tag in ftags]
    ftags = ", ".join(tag for tag in ftags)
    output_path = os.path.join(output_dir, filename+".txt")
    with open(output_path, "w") as output:
        output.write(ftags)



def save_png(imgpath, output_dir):
    file = os.path.basename(imgpath)
    filename = os.path.splitext(file)[0]
    output_path = os.path.join(output_dir, filename+".png")

    im = Image.open(imgpath).convert('RGBA')
    background = Image.new('RGBA', im.size, (255,255,255))
    im = Image.alpha_composite(background, im)
    im.save(output_path, 'PNG')


def main():
    files_dir = "data"
    tags_dir = "tags"
    pngs_dir = "pngs"
    if not os.path.exists(tags_dir):
        os.mkdir(tags_dir)
    filetypes = [".json"]
    files = get_files(filetypes, files_dir)[0]
    for jfile in files:
        filepath = os.path.join(files_dir,jfile)
        save_tags(filepath, tags_dir)
    
    imgtypes = [ '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.heif', 
                '.heic', '.ico', '.raw', '.apng', '.jfif', '.exif', '.ico' ]
    files = get_files(imgtypes, files_dir)
    files = [image for imgtype_ in files for image in imgtype_]
    # print(files)
    for image in files:
        imagepath = os.path.join(files_dir,image)
        save_png(imagepath, pngs_dir)

if __name__ == "__main__":
    main()
