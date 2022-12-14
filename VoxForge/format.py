import os
import shutil

base = "VoxForge/extracted"
data_folder = "VoxForge/data"
metadata = f"{data_folder}/metadata.csv"
#reset file contents:
open(metadata, 'w').close()

def append_prompts(prompt_path):
    
    all_lines = []
    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            for line in f.readlines():
                name, content = line.split(" ", maxsplit=1)
                all_lines.append(",".join([name, content]))
        
        with open(metadata, "a") as f:
            for line in all_lines:
                f.write(line)
    except UnicodeDecodeError:
        print(prompt_path.split("/")[-3])
    


for folder in os.listdir(base):
    folder_path = os.path.join("VoxForge/extracted", folder)
    if not os.path.isdir(folder_path):
        continue
    inner_folder = os.path.join(folder_path, os.listdir(folder_path)[0])
    prompt_path = os.path.join(inner_folder, "etc", "PROMPTS")
    append_prompts(prompt_path=prompt_path)


