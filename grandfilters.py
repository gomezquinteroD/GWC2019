from PIL import Image

def load_img(imgName):
    im = Image.open(imgName)
    return im

def show_img(myImg):
    myImg.show()

def save_img(imgO, fileName):
    imgO.save(fileName)

def aadya_invfilter(flowerimage):
    #flowerimage.getdata(band = None)
    f = list(flowerimage.getdata())
    invlist = []
    for colors in f:
        x1= 255- colors[0]
        x2= 255- colors[1]
        x3= 255- colors[2]
        invlist.append((x1, x2, x3))

    #nflower = flowerimage.putdata(invlist)

    newflower = Image.new("RGB" ,flowerimage.size)
    newflower.putdata(invlist)
    return newflower

def adriana_inverted(pic1):
    pixels = list(pic1.getdata())

    newImg = []

    for i in pixels:
        inverted = (255-i[0], 255-i[1], 255-i[2])
        newImg.append(inverted)

    newImage = Image.new("RGB", pic1.size, i)
    newImage.putdata(newImg)
    return newImage

def annie_instagram(instagramfilter):
    #obamafilter.getdata(band=None)
    #instagramfilter.getdata(band=None)
    colordata = list(instagramfilter.getdata())
    new_img = []
    for x in colordata:
        total = x[0] + x[1] +x[2]
        if total < 182:
            list1= x[0]-30
            list2= x[1]-30
            list3= x[2]-30
            list4 = (list1, list2, list3)
            new_img.append(list4)
        elif total <364:
            list1= x[0]-20
            list2= x[1]-20
            list3= x[2]-20
            list4 = (list1, list2, list3)
            new_img.append(list4)
        elif total <546:
            list1= x[0]+20
            list2= x[1]+20
            list3= x[2]+20
            list4 = (list1, list2, list3)
            new_img.append(list4)
        elif total >= 546:
            list1= x[0]+30
            list2= x[1]+30
            list3= x[2]+30
            list4 = (list1, list2, list3)
            new_img.append(list4)

    newfilter = Image.new("RGB", instagramfilter.size)
    newfilter.putdata(new_img)
    return newfilter

def breezy_emphasize_color(pic):
    gainsboro = (220, 220, 220)
    light_gray = (211, 211, 211)
    silver = (192, 192, 192)
    dark_gray = (169, 169, 169)
    gray = (128, 128, 128)
    dim_grey = (105, 105, 105)
    pixels = pic.getdata()
    original_banana = []
    for p in pixels:
        sum = p[0] + p[1] + p[2]
        if sum >= 660:
            original_banana.append(gainsboro)
        if sum < 660 and sum >= 633:
            original_banana.append(gainsboro)
        if sum < 633 and sum >= 576:
            original_banana.append(light_gray)
        if sum < 576 and sum >= 487:
            original_banana.append(silver)
        if sum < 487 and sum >= 384:
            original_banana.append(dark_gray)
        if sum < 384 and sum >= 315:
            original_banana.append(gray)
        if sum < 315 and sum >= 0:
            original_banana.append(dim_grey)
    cyan_filtered = Image.new("RGB", pic.size)
    cyan_filtered.putdata(original_banana)
    return cyan_filtered

def cathy_grayscale(pic1):
    pixel = list(pic1.getdata())
    newImg = []
    for i in pixel:
        grayscale = (int((i[0] + i[1] + i[2])/3), int((i[0] + i[1] + i[2])/3), int((i[0] + i[1] + i[2])/3))
        newImg.append(grayscale)
    newImage = Image.new("RGB", pic1.size, i)
    newImage.putdata(newImg)
    return newImage

def jade_half_obama(pic):
    #width = pic.width()
    #half_width = width / 2
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)
    pixels = list(pic.getdata())
    list_len = len(pixels)#/ half_width
    for i in range(list_len // 2):
        red_value = pixels[i][0]
        green_value = pixels[i][1]
        blue_value = pixels[i][2]
        sum = red_value + green_value + blue_value
        if sum < 182:
            pixels[i] = darkBlue
        elif sum >= 182 and sum < 364:
            pixels[i] = red
        elif sum >= 364 and sum < 546:
            pixels[i] = lightBlue
        else:
            pixels[i] = yellow
    im = Image.new("RGB", pic.size)
    im.putdata(pixels)
    return im

def jenn_bluepic(flowerz):
    pixel = list(flowerz.getdata())
    navy = (0,0,128)
    royalblue = (65,105,225)
    bluex = (0, 0, 225)
    lightskyblue = (112,150,158)

    colorpixels = list(flowerz.getdata())
    list_length = len(colorpixels)

    new_look = []

    for p in pixel:
        intensity = p[0] + p[1] + p[2]


        if intensity < 190:
            new_look.append(navy)
        elif intensity >= 190 and intensity < 300:
            new_look.append(royalblue)
        elif intensity >= 300 and intensity < 500:
            new_look.append(bluex)
        elif intensity >= 500:
            new_look.append(lightskyblue)

    filternew = Image.new("RGB", flowerz.size)
    filternew.putdata(new_look)
    return filternew

def jolina_pancon(panda):
    grey = (208, 211, 212)
    darkyellow = (110, 44, 0)
    lightgreen = (115, 198, 182)
    darkorange = (125, 102, 8)

    color = list(panda.getdata())
    list_len = len(color)

    for i in range(list_len):
        Grey1 = color[i][0]
        darkyellow1 = color[i][1]
        Lightorange1 = color[i][2]
        sum = Grey1 + darkyellow1 + Lightorange1

        if sum < 182:
            color [i] = grey
        elif sum > 182 and sum < 364:
            color [i] = darkyellow
        elif sum > 364 and sum < 546:
            color [i] = lightgreen
        elif sum > 546:
            color [i] = darkorange

    sunpanda = Image.new("RGB", panda.size)
    sunpanda.putdata(color)
    return sunpanda

def joyce_blue(winking_cat):
    darkBlue = (100, 150,233)
    red = (0, 26, 33)
    lightBlue = (45, 125, 158)
    yellow = (200, 227, 324)

    new_img = []
    pixels = list(winking_cat.getdata())

    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_img.append(red)
        elif intensity >= 182 and intensity <364:
            new_img.append(red)
        elif intensity >= 364 and intensity < 546:
            new_img.append(lightBlue)
        elif intensity >=546:
            new_img.append(red)

    newim = Image.new("RGB", winking_cat.size)
    newim.putdata(new_img)
    return newim

def kelsey_tint(pic2):

    darkblue = (100, 50, 76)
    red = (317, 26, 33)
    lightblue = (212, 150, 158)
    yellow = (352, 227, 166)
    pixels = list(pic2.getdata())
    new_img2 = []

    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 282:
            new_img2.append(darkblue)
        elif intensity >= 282 and intensity < 464:
            new_img2.append(red)
        elif intensity >= 464 and intensity < 646:
            new_img2.append(lightblue)
        elif intensity >= 646:
            new_img2.append(yellow)

    new_image2 = Image.new("RGB",pic2.size, p)
    new_image2.putdata(new_img2)
    return new_image2

def maggie_grayscale(im):
    colorpixels = list(im.getdata())
    list_length = len(colorpixels)

    for i in range(list_length):
        reddef = colorpixels[i][0]
        greendef = colorpixels[i][1]
        bluedef = colorpixels[i][2]
        sum = reddef + greendef + bluedef
        average = sum/3
        gray = (int(average), int(average), int(average))

        colorpixels[i] = gray
    graypb = Image.new("RGB", im.size)
    graypb.putdata(colorpixels)
    return graypb

def maria_grayscale(im):
    pixel = list(im.getdata())
    black= (0, 0 ,0)
    darkgray= (105,105,105)
    lightgray= (211,211,211)
    white= (255,255,255)
    newgray = []

    for p in pixel:
        intensity = p[0] + p[1] + p[2]
        if intensity < 200:
            newgray.append(black)
        elif intensity >= 180 and intensity < 360:
            newgray.append(darkgray)
        elif intensity >= 360 and intensity < 540:
            newgray.append(lightgray)
        elif intensity >= 540:
            newgray.append(white)

    cat_new = Image.new ("RGB", im.size)
    cat_new.putdata (newgray)
    return cat_new

def sam_obamicon(sun):
    pixels = sun.getdata()
    white = (250, 250, 250)
    pink = (230, 67, 145)
    brightpink = (255, 0, 123)
    darkpink = (148, 0, 71)
    black = (41, 20, 30)
    anotherpink = (255, 77, 162)
    newim = []
    width, height = sun.size
    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 170:
            newim.append(darkpink)
        elif intensity >= 170 and intensity < 364:
            newim.append(white)
        elif intensity >= 364 and intensity < 400:
            newim.append(pink)
        elif intensity >= 400 and intensity < 450:
            newim.append(brightpink)
        elif intensity >= 450:
            newim.append(anotherpink)
    sunny = Image.new("RGB", (width, height))
    sunny.putdata(newim)
    return sunny

def sana_inverted(waves):
    #waves.getdata(band = None)
    colordata = list(waves.getdata())

    new_img = []

    for x in colordata:
        Red1 = 255 - x[0]
        Green1 = 255 - x[1]
        Blue1 = 255 - x[2]
        new_img.append((Red1, Green1, Blue1))

    #Newpicture = waves.putdata(new_img)
    waves2 = Image.new("RGB", waves.size)
    waves2.putdata(new_img)
    return waves2

def nat_rainbow(icecream):
    red = (231, 76, 60)
    orange = (243, 156, 18)
    yellow = (244, 208, 63)
    green = (39, 174, 96)
    blue = (52, 152, 219)
    purple = (142, 68, 173)

    color = list(icecream.getdata())
    list_length = len(color)

    for i in range(list_length):
        redd = color[i][0]
        greend = color[i][1]
        blued = color[i][2]
        sum = redd + greend + blued

        if sum < 150:
            color [i] = red
        elif sum > 150 and sum < 250:
            color [i] = orange
        elif sum > 250 and sum < 350:
            color [i] = yellow
        elif sum > 350 and sum < 400:
            color [i] = green
        elif sum > 400 and sum < 450:
            color [i] = blue
        elif sum > 450:
            color [i] = purple

    new_image2 = Image.new("RGB", icecream.size)
    new_image2.putdata (color)
    return new_image2


def gabby_blue(im):
    pixel = list(im.getdata())
    new_image = []
    x = im.width
    y = im.height
    darkblue = (9, 48, 141)
    regblue = (105, 148, 249)
    lightishblue = (182, 204, 255)
    lightblue = (204, 255, 255)
    for pix in pixel:
        intensity = pix[0] + pix[1] + pix[2]
        if intensity < 182:
            new_image.append(darkblue)
        elif intensity >= 182 and intensity < 364:
            new_image.append(regblue)
        elif intensity >= 364 and intensity < 546:
            new_image.append(lightishblue)
        elif intensity >= 546:
            new_image.append(lightblue)
    newthing = Image.new("RGB", im.size)
    newthing.putdata(new_image)

    return newthing
