#!/usr/bin/env python3
"""Ảnh thumbnail Open Graph (1200x630) — nền TRẮNG finance, full English, không tên cá nhân."""
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

INK=(31,42,55); SOFT=(107,119,133); GREEN=(22,165,80); GOLD=(233,165,59); BLUE=(59,130,246)

# nền trắng -> xám rất nhạt
img=Image.new("RGB",(W,H),(255,255,255)); px=img.load()
for y in range(H):
    t=y/H; c=(int(255+(238-255)*t),int(255+(244-255)*t),int(255+(250-255)*t))
    for x in range(W): px[x,y]=c
d=ImageDraw.Draw(img,"RGBA")

# thanh gold trên + đường chart nhạt nền
d.rectangle([0,0,W,8],fill=GOLD)
chart=[(0,470),(150,440),(300,455),(450,400),(600,420),(750,350),(900,380),(1050,300),(1200,330)]
# fill nhạt dưới đường
d.polygon(chart+[(1200,H),(0,H)],fill=(22,165,80,18))
d.line(chart,fill=(22,165,80,90),width=5,joint="curve")

# vòng điểm (phải)
cx,cy,r=975,275,140
d.ellipse([cx-r,cy-r,cx+r,cy+r],outline=GREEN,width=16)
d.ellipse([cx-r+26,cy-r+26,cx+r-26,cy+r-26],fill=(255,255,255))
f=font(100); s="92"; bb=d.textbbox((0,0),s,font=f)
d.text((cx-(bb[2]-bb[0])/2,cy-85),s,font=f,fill=INK)
d.text((cx-34,cy+28),"/ 100",font=font(30,False),fill=SOFT)

# tiêu đề trái
d.text((70,110),"FINANCIAL",font=font(70),fill=INK)
d.text((70,188),"PROTECTION",font=font(70),fill=GREEN)
d.text((70,266),"SCORE",font=font(70),fill=INK)
d.text((74,360),"Free 60-second assessment",font=font(30,False),fill=SOFT)

# 4 trụ cột chips
x=74
for c in ["Retirement","Family","Health","Estate"]:
    f2=font(26,False); bb=d.textbbox((0,0),c,font=f2); w=bb[2]-bb[0]
    d.rounded_rectangle([x,418,x+w+34,463],radius=22,outline=(210,220,230),width=2,fill=(244,248,251))
    d.text((x+17,427),c,font=f2,fill=INK)
    x+=w+46
    if x>760: break

# dòng ngôn ngữ
d.text((74,540),"English  ·  Tiếng Việt  ·  中文  ·  Español",font=font(28),fill=BLUE)

img.save(os.path.join(os.path.dirname(__file__),"og.jpg"),"JPEG",quality=92)
print("✅ og.jpg")
