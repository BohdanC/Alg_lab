from PIL import Image

f=open('DS9.txt','r')
l=[line.strip() for line in f]
f.close()
list=[]
lst=[]
for x in l:
    for y in x:
        y=x.split(' ')
    list.append(y)
for i in list:
    list1=[int(x) for x in i]
    lst.append(list1)


image = Image.new('RGB', (540,960),(250,250,250))

for i in lst:
    image.putpixel((i),(0,0,0))

str1=input("Введіть назву зберігаємого файлу:")
frm=input("Введіть формат в якому хочете зберегти:")
image.save(str1+"."+frm)
