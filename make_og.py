#!/usr/bin/env python3
"""Tạo ảnh thumbnail (Open Graph 1200x630) cho khi share link lên Facebook."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
def font(sz, bold=True):
    for p in (["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
               "/System/Library/Fonts/Supplemental/Arial Unicode.ttf","/System/Library/Fonts/Helvetica.ttc"]):
        if os.path.exists(p):
            try: return ImageFont.truetype(p, sz)
            except: pass
    return ImageFont.load_default()

# nền gradient navy -> xanh đậm
img = Image.new("RGB",(W,H),(14,26,44)); px=img.load()
for y in range(H):
    t=y/H
    c=(int(14+(8-14)*t), int(26+(40-26)*t), int(44+(60-44)*t))
    for x in range(W): px[x,y]=c
d=ImageDraw.Draw(img,"RGBA")

# thanh gold trên
d.rectangle([0,0,W,8],fill=(233,165,59))

# vòng tròn điểm minh hoạ (góc phải)
cx,cy,r=980,300,150
d.ellipse([cx-r,cy-r,cx+r,cy+r],outline=(34,165,101),width=18)
d.ellipse([cx-r+30,cy-r+30,cx+r-30,cy+r-30],fill=(255,255,255))
f=font(110); s="92"
bb=d.textbbox((0,0),s,font=f); d.text((cx-(bb[2]-bb[0])/2,cy-95),s,font=f,fill=(20,42,55))
fz=font(34); d.text((cx-38,cy+25),"/ 100",font=fz,fill=(120,130,145))

# tiêu đề (trái)
d.text((70,120),"FINANCIAL",font=font(72),fill=(255,255,255))
d.text((70,200),"PROTECTION",font=font(72),fill=(54,211,153))
d.text((70,280),"SCORE",font=font(72),fill=(255,255,255))
d.text((74,375),"Free 60-second assessment",font=font(30,False),fill=(160,175,195))

# 4 trụ cột chips
chips=["Retirement","Family","Health","Estate"]
x=74
for c in chips:
    f2=font(26,False); bb=d.textbbox((0,0),c,font=f2); w=bb[2]-bb[0]
    d.rounded_rectangle([x,435,x+w+34,480],radius=22,fill=(255,255,255,28))
    d.text((x+17,444),c,font=f2,fill=(225,235,245))
    x+=w+50
    if x>720: break

# brand + ngôn ngữ
d.text((70,545),"Liam Phan  ·  Tài chính · Bảo hiểm · Sức khỏe · Di sản",font=font(26),fill=(233,165,59))
d.text((70,585),"English · Tiếng Việt · 中文 · Español",font=font(22,False),fill=(140,155,175))

img.save(os.path.join(os.path.dirname(__file__),"og.jpg"),"JPEG",quality=90)
print("✅ og.jpg")
