import codecs        
imageArray = [] #lower camel case

def setup():
    size(640, 360)
    imgPath = []
    
    #変数 num : 配列の長さnumberを意味
    #Path:画像のPath情報を表す変数
    for num in range(1, 10):  #pic01~09
        imgPath.append("pic0"+ str(num) + ".jpg")
    for num in range(10, 61): #pic10~60
        imgPath.append("pic"+ str(num) + ".jpg")

    for num in range(60):
        imageArray.append(loadImage(imgPath[num]))
    
    getColor() #色情報の取得
     
               
def draw():
   
    #画像の表示:y = hight, x = width
    for y in range(6):
        for x in range(10):
            image(imageArray[x+y*10], x*64, y*60, 64, 60)


def getColor():
    
    #画像をhueAvgに格納
    hueAvg = [0 for i in range(60)]
    
    #ピクセル配列にアクセスする前にpixelsを読み込む
    loadPixels() 
    
    #enumerate: ループする際に配列の添字つきで要素を得る
    for index, img in enumerate(imageArray):
        print ("pic" + str(index + 1))
        
        #読み込んだ色相の値
        hueSum = 0.0
        #読み込んだ色相の数
        count = 0
        
        
        # 画像の縦・横のpixel値を読み取る
        for y in range(img.height):
            for x in range(img.width):
                
                #画像の読み込んでいる位置
                loc = x + y *img.width 
    
                #pixel値の値をH,S,V値に分ける。
                h = hue(img.pixels[loc])
                s = saturation(img.pixels[loc])
                b = brightness(img.pixels[loc])
                
                
                # 止まれの標識のときに、赤色を180~360までにする
                if h != 0:
                    if index >= 20 and index < 40:
                        if 0 < h and h < 127:
                            hueSum += 360-h
                        elif h >= 127 and h <= 255:
                            hueSum += h
                        count += 1
                    # 止まれ以外の画像の時
                    else:
                        hueSum += h 
                        count += 1
                        
        # hueAvg =画像の色相の平均値
        hueAvg[index] = hueSum / count
        print hueSum / count
    
    #読み込んだpixelsの更新    
    updatePixels() 
    #txtファイルに出力
    output = createWriter("hueLevel.txt")
    for value in hueAvg:
        output.println(str(value))
    output.flush()
    output.close()
