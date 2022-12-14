# importing the "tarfile" module
import tarfile
import os

# open file
dl_dir = "VoxForge/downloads/"
filenames = os.listdir(dl_dir)
for filename in filenames:
    filepath = os.path.join(os.getcwd(), dl_dir, filename)
    file = tarfile.open(filepath)
    file.extractall(f"VoxForge/extracted/{filename.strip('.tgz')}")
    file.close()
  