import os
import sys
import xml.etree.ElementTree as ET

# Use the script to search for a parent + child tag in a given directory.
# Child tag is optional.
# python3 FindTargetedTag.py ./sample SUBJECTIVE [HTMLDATA]

def main():
  src_path = sys.argv[1]
  tag = sys.argv[2]
  subTag = None
  if len(sys.argv) > 3:
    subTag = sys.argv[3]
  print(f"Finding '{tag}' in {src_path}")
  dir_list = os.listdir(src_path)
  for file in dir_list:
    if (file.endswith(".pdf")):
      continue
    try:
      file_path = f"{src_path}/{file}"
      print(f"processing: {file}")
      tree = ET.parse(file_path)
      root = tree.getroot()
      body = root.find('.//BODY')
      if body is not None:
        for elem in body.iter(tag):
          if subTag is not None:
            subData = elem.find(f".//{subTag}")
          while True:
            if (subTag is not None):
              print(f"Found {tag} => {subData}: {subData.text}")
            else:
              print(f"Found {tag}")
              for child in elem:
                print(f"{child}: {ET.tostring(child, encoding='unicode')}")
            user_input = input("Type 'c' to continue: ").strip().lower()
            if user_input == 'c':
              print("Resuming...")
              break
    except Exception as e:
      print(f"{file} Error: {e} ")
      continue
if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print("\nProgram terminated.")