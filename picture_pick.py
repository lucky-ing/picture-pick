import os
import re
import cv2
import sys
#the source folder that you will read the .jpg and .xml from
src0='/home/lucky/open/tuoxie_VOC/tuoxie_color/'
#the destation folder that you will save the .jpg files and .txt files, which are rename and transformed
dst0='/home/lucky/open/tuoxie_VOC/tuoxie_color_temp/'
if __name__=='__main__':
    if len(sys.argv) < 2:
        print(
            'picture_pick program need 2 argv.you must input command like\n   python 123.py [source path] [destination path]')
    else:
        src = sys.argv[1] + '/'
        dst=sys.argv[2]+'/'
        listd=os.listdir(src)
        txt=re.compile(r'.*(jpg)')
        listdir=[]
        for i in listd:
            if re.findall(txt,i):
                listdir.append(i)

        for i in listdir:

            imgsource = src + i
            print(i)
            pic = cv2.imread(imgsource)
            pic=cv2.resize(pic,(471,471))
            textsource = imgsource.replace('jpg', 'txt')
            text=open(textsource).read()
            textlist=text.split()
            #print(int(len(textlist)/5))
            drawpic=pic.copy()
            for j in range(int(len(textlist)/5)):
                xx = float(textlist[1+j*5])
                yy = float(textlist[2+j*5])
                wwidth = float(textlist[3+j*5])
                hheight = float(textlist[4+j*5])
                drawpic=cv2.rectangle(pic,(int((xx-wwidth/2.0)*pic.shape[0]),int((yy-hheight/2.0)*pic.shape[1])),(int((xx+wwidth/2.0)*pic.shape[0]),int((yy+hheight/2.0)*pic.shape[1])),[0,255,0],2)

            cv2.imwrite(dst+i,drawpic)
            #print(hheight)


        '''i_file = open(src + i, 'r')
        i_content = i_file.read()
        i_file.close()
        print(i)
        # print(i_content)
        name = (re.findall(nname, i_content)[0])
        # index = listname.index(name)
        index = 0
        txtname0 = dst + str(p).zfill(4) + '.txt'
        f = open(txtname0, 'w')
        width = int(re.findall(wwidth, i_content)[0])
        height = int(re.findall(hheight, i_content)[0])
        for j in range(re.findall(xxmin, i_content).__len__()):
    
            xmin = int(re.findall(xxmin, i_content)[j])
            ymin = int(re.findall(yymin, i_content)[j])
            xmax = int(re.findall(xxmax, i_content)[j])
            ymax = int(re.findall(yymax, i_content)[j])
    
            # txtname=dst+i
            # txtname0=txtname.replace('xml','txt')
    
            if j != 0:
                f.write('\n')
            f.write(str(index) + ' ' + '%0.4f' % ((float(xmin) + float(xmax)) / float(width) / 2) + ' ' + '%0.4f' % (
            (float(ymin) + float(ymax)) / float(height) / 2) + ' ' + '%0.4f' % (
                    float(xmax - xmin) / float(width)) + ' ' + '%0.4f' % (float(ymax - ymin) / float(height)))
        f.close()
        imgsource = src + i
        imgname0 = imgsource.replace('xml', 'jpg')
        img = cv2.imread(imgname0)
        # print(img)
    
        if img is None:
            imgname0 = imgname0.replace('jpg', 'JPG')
            img = cv2.imread(imgname0)
        if img is None:
            imgname0 = imgname0.replace('JPG', 'png')
            img = cv2.imread(imgname0)
        imgdst = dst + str(p).zfill(4) + '.jpg'
        # imgname1 = imgdst.replace('xml', 'jpg')
        cv2.imwrite(imgdst, img)
        p += 1'''