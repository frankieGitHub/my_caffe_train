import sys
import cv2
import copy
import math
import numpy as np
import os

#file_input_path='/home/coolpad/AI/alive_detect/linronghui/my_face_collect/Real_face/'


def make_diff_img(f1, f2, output):

    print f1
    print f2
    img_cv1 = cv2.imread(f1)
    print('\n--------- read img1 ---------')
    print img_cv1
    
    img_cv2  = cv2.imread(f2)
    print('\n--------- read img2 ---------')
    print img_cv2
    
    print('\n--------- img diff ---------')
    img_diff = img_cv2 - img_cv1

    #print img_diff

    #cv2.imshow('image',img_diff)

    
    cv2.imwrite(output, img_diff)

    #cv2.waitKey(0)   


def main():
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    index = 0;

    #files=os.listdir(input_path)
    #files.sort()
    #print files


    print 'input path is: %s' % input_path
    print 'output path is: %s' % output_path


    for root, dirs, files in os.walk(input_path):
        for ff in files:   
	   print ff
           ffNum = ff.strip('.jpg')
	   for ff2 in files:
	       ff2Num = ff2.strip('.jpg')
               time_diff = long(ff2Num)-long(ffNum)
               if time_diff < 500 and time_diff > 0:
                   print long(ff2Num)
                   print long(ffNum)
	           print time_diff
                   print '\n'
                   make_diff_img(input_path + '/' + ff2, input_path + '/' + ff, output_path + '/' + str(index) + '.jpg')
                   index += 1
               #if long(ff2Num) - long(ffNum) < 500:
                #   print " %s - %s " % (ff2, ff)


if __name__ == "__main__":
    main()
