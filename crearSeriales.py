from PIL import Image
import cv2

print('1 --> MFV-1')
print('2 --> MFV-2')
print('3 --> MFV-3')
print('4 --> Bateria corta')
print('5 --> Bateria larga')
print('6 --> Inversor')
print('7 --> Regulador')
print('8 --> Medidor')
print('9 --> Poste')
print('10 --> Regulador 2')
print('11 --> Medidor 2 (los dos primeros espacios deben ser dobles')
print('12 --> Regulador 3')

item = input('Digita el item correspondiente al serial: ')

outFile = input('Digita el item del usuario: ')

Serial = input('Digita el serial: ')




if(item == "1"):
    img = cv2.imread('./seriales/a_panel_1.jpg')
    tama = img.shape
    
    outFile = outFile + "-" + input('Digita el nombre del dispositivo: ')
    
    #Serial = '99882107130095579'
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    font=0
    position               = (93,162)
    fontScale              = 0.9
    fontColor              = (0,0,5)
    
    cv2.putText(img,Serial,
        position,
        font,
        fontScale,
        fontColor,2)
    Gaussian = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imwrite(outFile+'.jpg',Gaussian)

if(item == "2"):
    img = cv2.imread('./seriales/a_panel_2.jpg')
    tama = img.shape
    outFile = outFile + "-" + input('Digita el nombre del dispositivo: ')
    #Serial = '99882107130095579'
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    font=0
    position               = (64,105)
    fontScale              = 0.8
    fontColor              = (0,0,5)
    
    cv2.putText(img,Serial,
        position,
        font,
        fontScale,
        fontColor,2)
    Gaussian = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imwrite(outFile+'.jpg',Gaussian)

if(item == "3"):
    outFile = outFile + "-" + input('Digita el nombre del dispositivo: ')
    img = cv2.imread('./seriales/b_panel_2.jpg')
    tama = img.shape
    
    #Serial = '99882107130095579'
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    font=0
    position               = (169,430)
    fontScale              = 1
    fontColor              = (0,0,5)
    
    cv2.putText(img,Serial,
        position,
        font,
        fontScale,
        fontColor,2)
    Gaussian = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imwrite(outFile+'.jpg',Gaussian)

if(item == "4"):

    outFile = outFile + '-bateria'
    
    img = cv2.imread('./seriales/bateria_corta.jpg')
    tama = img.shape
    
    #Serial = 'SN:B2567'
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    font=0
    position               = (184,453)
    fontScale              = 3.2
    fontColor              = (0,0,15)
    
    cv2.putText(img,Serial,
        position,
        font,
        fontScale,
        fontColor,6)
    Gaussian = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imwrite(outFile+'.jpg',Gaussian)

if(item == "5"):

    outFile = outFile + '-bateria'
    img = cv2.imread('./seriales/bateria_larga.jpg')
    tama = img.shape
    
    #Serial = 'SN:B2567ASDF'
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    font=0
    position               = (94,153)
    fontScale              = 1
    fontColor              = (0,0,5)
    
    cv2.putText(img,Serial,
        position,
        font,
        fontScale,
        fontColor,2)
    Gaussian = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imwrite(outFile+'.jpg',Gaussian)

if(item == "6"):
    
    outFile = outFile + '-inversor'

    img = cv2.imread('./seriales/inversor.jpg')
    tama = img.shape
    
    #Serial = 'SN:8P102212A0434220400045'
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    font=0
    position               = (9,106)
    fontScale              = 0.65
    fontColor              = (0,0,5)
    
    cv2.putText(img,Serial,
        position,
        font,
        fontScale,
        fontColor,1)
    Gaussian = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imwrite(outFile+'.jpg',Gaussian)

if(item == "7"):

    outFile = outFile + '-regulador'

    img = cv2.imread('./seriales/regulador.jpg')
    tama = img.shape
    
    #Serial = 'SN:RC4567-311'
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    font=0
    position               = (24,275)
    fontScale              = 2
    fontColor              = (0,0,45)
    
    cv2.putText(img,Serial,
        position,
        font,
        fontScale,
        fontColor,5)
    Gaussian = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imwrite(outFile+'.jpg',Gaussian)

if(item == "8"):

    outFile = outFile + '-medidor'

    img = cv2.imread('./seriales/medidor.jpg')
    tama = img.shape
    
    #Serial = '51 9616 7695 7'
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    font=0
    position               = (138,153)
    fontScale              = 1
    fontColor              = (0,0,5)
    
    cv2.putText(img,Serial,
        position,
        font,
        fontScale,
        fontColor,2)
    Gaussian = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imwrite(outFile+'.jpg',Gaussian)

if(item == "9"):
    
    outFile = outFile + '-poste'

    img = cv2.imread('./seriales/poste.jpg')
    tama = img.shape
    
    #Serial = 'SP:PR567-311'
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    font=0
    position               = (200,281)
    fontScale              = 1.7
    fontColor              = (0,0,20)
    
    cv2.putText(img,Serial,
        position,
        font,
        fontScale,
        fontColor,4)
    Gaussian = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imwrite(outFile+'.jpg',Gaussian)

if(item == "10"):

    outFile = outFile + '-regulador'

    img = cv2.imread('./seriales/regulador_2.jpg')
    tama = img.shape
    
    #Serial = 'SN:RC1449-311'
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    font=0
    position               = (57,128)
    fontScale              = 1.2
    fontColor              = (5,5,5)
    
    cv2.putText(img,Serial,
        position,
        font,
        fontScale,
        fontColor,3)
    Gaussian = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imwrite(outFile+'.jpg',Gaussian)
    

if(item == "11"):

    outFile = outFile + '-medidor'

    img = cv2.imread('./seriales/medidor_2.jpeg')
    tama = img.shape
    
    #Serial = '95  4567  8765 4'
    #serial2 = Serial[:2]
    #serial3 = Serial[3:7]
    
    
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    font=0
    position               = (190,616)
    fontScale              = 0.99
    fontColor              = (5,5,5)
    
    #serial2 =  
    
    cv2.putText(img,Serial,
        position,
        font,
        fontScale,
        fontColor,3)
    Gaussian = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imwrite(outFile+'.jpg',Gaussian)
    

if(item == "12"):

    outFile = outFile + '-regulador'

    img = cv2.imread('./seriales/regulador_3.jpeg')
    tama = img.shape
    
    #Serial = 'SN:RC4444-311'
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    font=0
    position               = (331,600)
    fontScale              = 1.1
    fontColor              = (5,5,5)
    
    cv2.putText(img,Serial,
        position,
        font,
        fontScale,
        fontColor,3)
    Gaussian = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imwrite(outFile+'.jpg',Gaussian)