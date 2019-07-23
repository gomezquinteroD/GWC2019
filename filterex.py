from PIL import Image
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(picture):
    im = Image.open(picture)
    return im



# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(visual):
    visual.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(visual2, coolpic):
    visual2.save(coolpic)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(obj):
    #data from image obj
    pic = obj.getdata()
    #new empty list for new image
    pixel = []
    #obama colors
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    for pix in pic:
        total = pix[0] + pix[1] + pix[2]
        if total < 182:
            pixel.append(darkBlue)
        elif 182 <= total < 364:
            pixel.append(red)
        elif 364 <= total < 546:
            pixel.append(lightBlue)
        else:
            pixel.append(yellow)

    bam = Image.new("RGB", pic.size)
    bam.putdata(pixel)

    return bam




myImg = load_img("cake.jpg")
