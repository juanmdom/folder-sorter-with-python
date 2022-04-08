# Script para ordenar la carpeta de Downloads

from fileinput import filename
import os, shutil

# The folder you want to sort
folder_path = r"C:\Users\juanmdom\Downloads"

# File extensions that will be reorganized in specific folders
extensions = [".docx", ".txt", ".doc", ".pdf", ".mp4", ".md"
              ".jpg", ".jpeg", ".gif", ".png", ".rar",
              ".zip", ".exe", ".torrent", ".xlsx", ".7z",
              ".js", ".html", ".iso", ".py", ".cpp", ".xml"]

# Stores all files of the folder
files = [os.path.join(folder_path, file) 
          for file in os.listdir(folder_path) 
            if os.path.isfile(os.path.join(folder_path, file))]

# Main function
def main():
  # I remove all pdf's because personal preference
  if os.path.isdir((folder_path + "\\" + "pdf")):
    shutil.rmtree((folder_path + "\\" + "pdf"))
    
  # Checking every file    
  for file in files:
    # Splits the file name and it's extension
    filename, fextension = os.path.splitext(file)

    # If the extension is in the array it creates a specific folder 
    # for that format
    if fextension in extensions:
      # The new folder's name will be the extension of the file
      new_folder_name = fextension.replace(".", "")
      # Checks if the folder where we move the file do exists
      if os.path.isdir((folder_path + "\\" + new_folder_name)):
        shutil.move(file, folder_path + "\\" + new_folder_name)
      # If not we make a new dir
      else:
        os.makedirs(folder_path + "\\" + new_folder_name)
        shutil.move(file, folder_path + "\\" + new_folder_name)
    
    # If that format isn't in the array, we build 'others' folder
    else:
      new_folder_name = "others"
      if os.path.isdir((folder_path + "\\" + new_folder_name)):
        shutil.move(file, folder_path + "\\" + new_folder_name)
      else:
        os.makedirs(folder_path + "\\" + new_folder_name)
        shutil.move(file, folder_path + "\\" + new_folder_name)

if __name__ == "__main__":
  main()
