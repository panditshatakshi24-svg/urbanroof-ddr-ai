import fitz
import os

def extract_images(pdf_path, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    doc = fitz.open(pdf_path)

    saved_images = []

    for page_num in range(len(doc)):

        for img_index, img in enumerate(doc.get_page_images(page_num)):

            xref = img[0]

            base_image = doc.extract_image(xref)

            width = base_image.get("width", 0)
            height = base_image.get("height", 0)

            # Ignore tiny images/icons
            if width < 200 or height < 200:
                continue

            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            image_name = f"page_{page_num+1}_{img_index}.{image_ext}"

            image_path = os.path.join(output_folder, image_name)

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            saved_images.append(image_path)

    return saved_images