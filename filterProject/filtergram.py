from filters import *

def main():

    print("Image Editor: ")
    filen = input("Give the file name: ")
    imgs = load_img(filen)


    print("Loading image...")
    show_img(imgs)
    print("Showing image...")
    oImg = obamicon(imgs)
    print("Obamicon activated...")
    show_img(oImg)

main()
