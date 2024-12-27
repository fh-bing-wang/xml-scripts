import os
import sys
import xml.etree.ElementTree as ET

# A script to find documents with repeated SOAP tags in a given directory.
# Once a document is found, the program pauses, and press "c" to continue.

# python3 FindRepeatedSoap.py ./sample SUBJECTIVE

def main():
    src_path = sys.argv[1]
    tag = sys.argv[2]

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
                targetedTags = body.findall(f".//{tag}")
                if len(targetedTags) > 1:
                    print(f"Found multiple '{tag}'s in {file}")
                    for index, elem in enumerate(targetedTags):
                        print(tag, index + 1)
                        print(ET.tostring(elem, encoding='unicode'))
                        print("\n")

                    while True:
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
