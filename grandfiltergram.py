from grandfilters import *

def main():
    #change "file_name_here with your image link"
    myImg = load_img("cake.jpg")
    #pick one of the filters here
    newImg = sam_obamicon(myImg)

    newImg.show()

main()
