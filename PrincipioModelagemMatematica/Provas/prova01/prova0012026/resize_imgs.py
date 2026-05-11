from PIL import Image
fns = ['20260422_181107.jpg','20260422_181118.jpg','20260422_181123.jpg']
for fn in fns:
    img = Image.open(fn)
    img2 = img.resize((1020, 471))
    out = fn.replace('.jpg','_small.jpg')
    img2.save(out, quality=85)
    print('Salvo:', out)
