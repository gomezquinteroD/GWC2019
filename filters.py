from PIL import Image
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    im = Image.open(filename)
    return im

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(imgName):
    imgName.show()


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(imgFile, imgName):
    imgFile.save(imgName, format = None)
# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(imgO):
    print("Initializing obamicon... ")
    pixels = imgO.getdata()

    #recolored pixels go here
    new_pixels = []

    #define the colors on the obamicon
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    #go through each pixel and determine its intensity
    for p in pixels:
        #intensity is adding all RGB values together
        intensity = p[0] + p[1] + p[2]

        #based on intensity, change pixel to appropriate obama color
        if intensity < 182:
            new_pixels.append(darkBlue)
        elif intensity >= 182 and intensity < 364:
            new_pixels.append(red)
        elif intensity >= 364 and intensity < 546:
            new_pixels.append(lightBlue)
        elif intensity >=546:
            new_pixels.append(yellow)

    #create a new image and input the new pixels
    newim = Image.new("RGB", imgO.size)
    newim.putdata(new_pixels)

    return newim
