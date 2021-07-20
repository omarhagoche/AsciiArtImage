from PIL import Image as Image_lib
  # /home/kodigo88/Downloads/7f577cf5f6bc75957ac67556c776c99a.jpg
Ascii = ["W","E","C","O","D","@",":",",","*","."," "]

def image_resizer(image,new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width,new_height))
    return(resized_image)

def convert_To_Gray(image):
    gray_image=image.convert("L")
    return(gray_image)

def pixels_to_ascii(image):
    try:
        pixels = image.getdata()
        chars = "".join([Ascii[pixel//25] for pixel in pixels])
        return(chars)
    except Exception as ex:
        print(str(ex))
    
def main(new_width=100):
    path = input("Enter Path Of Image (ex : /home/Desktop/HappyEid.jpeg):\n")
    try:
        image = Image_lib.open(path)
        resized_image = image_resizer(image)
        Gray_Image = convert_To_Gray(resized_image)
        new_image_data = pixels_to_ascii(Gray_Image)

        pixels = len(new_image_data)
        ascii_art_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0,pixels,new_width))
        
        print(ascii_art_image)

        with open("Ascii_Art_image","w") as File:
            File.write(ascii_art_image)
    except:
        print("Wrong Path or unvalid image")


main()