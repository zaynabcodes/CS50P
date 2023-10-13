import sys
from PIL import Image, ImageOps

def main():

    # Check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input.jpg output.jpg")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Check input and output extensions
    input_ext = input_path.lower().split('.')[-1]
    output_ext = output_path.lower().split('.')[-1]
    if input_ext not in ['jpg', 'jpeg', 'png'] or output_ext not in ['jpg', 'jpeg', 'png']:
        sys.exit("Input and output must be JPG, JPEG, or PNG images")
    if input_ext != output_ext:
        sys.exit("Input and output must have the same file extension")

    # Open input image
    try:
        input_img = Image.open(input_path)
    except FileNotFoundError:
        sys.exit("Input file does not exist")

    # Open shirt image
    shirt_img = Image.open("shirt.png")

    # Resize input to shirt size
    input_resized = ImageOps.fit(input_img, shirt_img.size, Image.BICUBIC)

    # Paste shirt onto input
    input_resized.paste(shirt_img, (0, 0), shirt_img)

    # Save output image
    input_resized.save(output_path)

if __name__ == "__main__":
    main()