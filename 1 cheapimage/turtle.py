from PIL import Image



class cimg:
    cheapimgfs=""
    def create():
        wci=80
        hci=29
        print('openandchange')
        path = input('adres img=')
        img = Image.open(path)
        obj = img.load()
        img.close() #закрываем файл с изо, потому что уже загрузили пиесели все
        #newcist=[]
        cheapimg=""
        
        for i in range (0, hci):
            for j in range (0, wci):
                pixc=obj[(img.size[0]/((wci+1)))*(j+1),(img.size[1]/((hci+1)))*(i+1)] #создаем кортеж из открытого изображения с его цветами из среднего числа из клеток
                pixk=(pixc[0]//25,pixc[1]//25,pixc[2]//25)# делим каждый цвет на 25
                x=160+pixk[0]+pixk[1]*12+pixk[2]*11 # делаем из цвета число
                #newcist.append(chr(x))
                cheapimg=cheapimg+chr(x)#добавляем к стрингу символ по номеру этого числа
            #newcist.append('\n')
            cheapimg=cheapimg+'\n'
        cimg.cheapimgfs=cheapimg
        print(cheapimg) #вывод дешевого изобр
        #path = path[:-4]+'.cimg' #удаление расширения и добавление расш дешевого изобр
        #f=open(path,'x')
        #f.write(cheapimg)
        #f.close()
        
        
    def open():
        print('openasci')
        path=input('adres img(.cimg)=')
        f=open(path,'r')
        cheapread=f.read()
        f.close()
        cimg.cheapimgfs=cheapread
        print(cheapread)
        
    def save():
        print('saveasci')
        path=input('adres img(.cimg)=')
        f=open(path,'x')
        f.write(cimg.cheapimgfs)
        f.close()
        
        
def menu():
    print('Type')
    print('     1 for create .cimg from .jpg or .png')
    print('     2 for open .cimg')
    print('     3 for save .cimg')
    print('     4 for exit')

print('Welcome, you open CIV (Cheap Image Viewer)')
print('It\'s program for work with .cimg files (cheap image)')
print('It\'s created for poor Africa')

while (1):
    menu()
    user=int(input('==>'))
    if (user==1):
        cimg.create()
    elif(user==2):
        cimg.open()
    elif(user==3):
        cimg.save()
    elif(user==4):
        break
