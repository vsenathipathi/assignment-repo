# Build a script to extract text from images using Tesseract OCR.
import os, sys
import pytesseract
from PIL import Image

path = r"C:\Users\mails\Downloads\python_test_folder\images"
image_list = os.listdir(path)

# output_dir=os.path.join(path,"ocr_output")
output_dir = r"C:\Users\mails\Downloads\python_test_folder\output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for i in image_list:
    if i.endswith((".png", ".jpg", ".jpeg")):
        filename = str(i.split(".")[0])
        try:
            img = Image.open(os.path.join(path, i))
            extracted_text = pytesseract.image_to_string(img, lang="eng")
            print(f"\n==========Extracted text from {i}==========\n{extracted_text}")

            with open(os.path.join(output_dir, f"{filename}.txt"), "w") as f:
                f.write(extracted_text)
                print(f"Text written to {filename}.txt")
        except Exception as e:
            print(f"Error processing {i}: {e}")
