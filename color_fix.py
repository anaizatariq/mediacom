import sys
from PIL import Image

def gold_to_red(image_path, output_path):
    # Open image
    img = Image.open(image_path)
    img = img.convert("RGBA")
    data = img.getdata()

    new_data = []
    # Dark Goldenrod is approx (184, 134, 11)
    # The previous script might have replaced red with this gold color.
    # Gold generally has High Red, Med Green, Low Blue.
    # Let's target any pixel where R > G and R > B and G is somewhat high (gold/yellow)
    # A simple threshold for gold/yellow:
    
    for item in data:
        r, g, b, a = item
        # If it's a golden/yellowish pixel
        if r > 100 and g > 80 and b < 100 and r > g:
            # Change to pure red
            new_data.append((220, 20, 30, a))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path)
    print(f"Processed {image_path}")

gold_to_red("assets/logo-navbar-clean.png", "assets/logo-navbar-clean.png")
gold_to_red("assets/logo.png", "assets/logo.png")
gold_to_red("assets/logo-navbar.png", "assets/logo-navbar.png")
