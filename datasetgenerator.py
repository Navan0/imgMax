from PIL import Image, ImageDraw, ImageFont
import os
# from google.colab import files
font = 'Brawl'
os.mkdir('/home/navaneeth/work/fontMagic/fonts/'+font)
words = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","0","1","2","3","4","5","6","7","8","9"]
no = 62
lo = 10
for m in range(lo):
    for i in range(no):

        img = Image.new('RGB', (320, 320), color=(0+m*2, 0+m*5, 0+m*6))
        fnt = ImageFont.truetype('/home/navaneeth/work/All Fonts/Best Commercial Fonts/Brawl.ttf', 100)
        d = ImageDraw.Draw(img)
        d.text(((320-100)/2,    (320-100)/2), words[i], font=fnt, fill=(255, 255, 255))
        print("time for a gamble"+"  "+words[i]+words[i]+words[i]+words[i]+words[i]+words[i])

        # if you need to sub class the font directory into alphabets uncomment the below try catch method
        # try:
        #     if(words[i] == words[i]):
        #         os.mkdir('/home/navaneeth/work/fontMagic/fonts/'+font+'/'+words[i])
        # except Exception as e:
        #     print("time for a gamble"+"  "+words[i]+words[i]+words[i]+words[i]+words[i])
        img.save('/home/navaneeth/work/fontMagic/fonts/'+font+'/'+font+str(i)+str(m)+'.png')
print("hope you've enjoyed a espresso arabica")
