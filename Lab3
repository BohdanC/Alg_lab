from PIL import Image, ImageDraw

f=open('DS9.txt','r')
l=[line.strip() for line in f]
f.close()
list1=[]
lst=[]
for x in l:
    for y in x:
        y=x.split(' ')
    list1.append(y)
for i in list1:
    list2=[int(x) for x in i]
    lst.append(list2)


image = Image.new('RGB', (540,960),(250,250,250))

for i in lst:
    image.putpixel((i),(0,0,0))



pixels_count = len(lst)


h = list(range(pixels_count))



for i in range(1, pixels_count):
    if lst[h[i]][0] < lst[h[0]][0]:
        h[i], h[0] = h[0], h[i]


fo = [h[0]]
h.append(h.pop(0))

def rotate(a,b,c):
  return (b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])

while True:
    right = 0


    for i in range(1, len(h)):
        if rotate(lst[fo[-1]], lst[h[right]], lst[h[i]]) < 0:
            right = i

    if h[right] == fo[0]:

        break
    else:

        fo.append(h.pop(right))


draw = ImageDraw.Draw(image)


for i in range(len(fo)):
    px = lst[fo[i - 1]]
    px2 = lst[fo[i]]


    draw.line((px[0], px[1], px2[0], px2[1]), fill='blue', width=2)


with open('Оболочка.txt', 'w') as file:
    for i in fo:
        file.write(f"{lst[i][0]} {lst[i][1]}\n")



str1=input("Введіть назву зберігаємого файлу:")
frm=input("Введіть формат в якому хочете зберегти:")
image.save(str1+"."+frm)
