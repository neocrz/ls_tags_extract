import os
import json

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

def main():
    files_dir = "data"
    tags_dir = "tags"
    if not os.path.exists(tags_dir):
        os.mkdir(tags_dir)
    filetypes = [".json"]
    files = get_files(filetypes, files_dir)[0]
    for jfile in files:
        filepath = os.path.join(files_dir,jfile)
        save_tags(filepath, tags_dir)
    


if __name__ == "__main__":
    main()
