from ntpath import join
import os

# os.mkdir("./valid")

for folder in os.listdir("train"):
    os.mkdir(os.path.join("valid", folder))