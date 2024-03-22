import cv2 as cv

def get_pixel(path):
    print('\n*******************************************')
    print('************* GET PIXE ON IMAGE *************')
    img = cv.imread(path)
    for i in range(10):
        k = img[0,i]
        print('********************************************')
        print('nilai rgb dari pixel ke : {0} \n red   : {1}\n green : {2}\n blue  : {0}'
            .format(i, k[2],k[1],k[0]))




get_pixel('./img.png')