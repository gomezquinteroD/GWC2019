from PIL import Image
    # Rename this file to be "filters.py"
    # Add commands to import modules here.

    # Define your load_img() function here.
    #       Parameters: The name of the file to be opened (string)
    #       Returns: The image object with the opened file.
def load_img(imgName):
    im = Image.open(imgName)
    return im

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(myImg):
    myImg.show()
# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(imgO, fileName):
    imgO.save(fileName)


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(myImg):
    #obamicon here
    pixels = myImg.getdata()

    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    #make a NEW list for our NEW, recolored image
    new_img = []

    for p in pixels:
        #calculate intensity for EACH pixel
        intensity = p[0] + p[1] + p[2]

        #low intensity
        if intensity < 182:
            new_img.append(darkBlue)
        #Med - Low intensity
        elif intensity >= 182 and intensity < 364:
            new_img.append(red)
        #Med - High intensity
        elif intensity >= 364 and intensity < 546:
            new_img.append(lightBlue)
        elif intensity >= 546:
            new_img.append(yellow) 

    #create a NEW image OBJECT
    newim = Image.new("RGB", myImg.size)
    newim.putdata(new_img)



#im = load_img("cake.jpg")
#show_img(im)

#save_img(im, "MyCake.jpg")
