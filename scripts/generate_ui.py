from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import math, random

ROOT=Path("assets/minecraft/textures/gui")
def font(size,bold=False):
    candidates=["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"]
    for p in candidates:
        if Path(p).exists(): return ImageFont.truetype(p,size)
    return ImageFont.load_default()

def title_scene(seed):
    random.seed(seed); w=h=256
    im=Image.new("RGB",(w,h),(7,5,17)); px=im.load()
    for y in range(h):
        for x in range(w):
            glow=max(0,1-math.sqrt(((x-125)/180)**2+((y-100)/150)**2))
            px[x,y]=(int(7+20*glow),int(5+7*glow),int(17+35*glow))
    d=ImageDraw.Draw(im,"RGBA")
    # distant mountains and obsidian citadel silhouette
    d.polygon([(0,175),(35,130),(67,165),(105,112),(143,163),(180,122),(220,170),(256,135),(256,256),(0,256)],fill=(15,9,30,255))
    d.polygon([(0,207),(42,170),(76,202),(117,155),(158,207),(203,168),(256,210),(256,256),(0,256)],fill=(6,5,15,255))
    d.rectangle((105,92,151,205),fill=(10,8,22,255),outline=(115,69,160,220),width=2)
    d.polygon([(99,94),(128,58),(157,94)],fill=(13,9,26,255),outline=(184,135,65,230))
    d.rectangle((116,115,140,205),fill=(19,10,34,255),outline=(93,52,137,220),width=2)
    d.rectangle((123,132,133,159),fill=(135,70,210,150))
    d.line((128,60,128,23),fill=(230,190,100,230),width=2)
    d.polygon([(128,18),(134,29),(128,26),(122,29)],fill=(255,221,150,255))
    # magical stars and drifting embers
    for _ in range(100):
        x=random.randrange(w); y=random.randrange(190)
        r=random.choice([1,1,2])
        col=random.choice([(190,140,255,160),(255,205,100,150),(110,190,255,130)])
        d.ellipse((x-r,y-r,x+r,y+r),fill=col)
    d.line([(0,222),(256,222)],fill=(155,105,205,90),width=1)
    return im

bg=ROOT/"title"/"background"; bg.mkdir(parents=True,exist_ok=True)
for i in range(6): title_scene(i).save(bg/f"panorama_{i}.png")
# Standard 1.12 title logo atlas: preserve expected 256x64 dimensions.
logo=Image.new("RGBA",(256,64),(0,0,0,0)); d=ImageDraw.Draw(logo)
d.text((128,8),"NEXORA",font=font(35,True),anchor="mt",fill=(238,205,130,255),stroke_width=2,stroke_fill=(48,23,72,255))
d.text((128,46),"S T U D I O S",font=font(10,True),anchor="mt",fill=(190,150,230,255))
logo.save(ROOT/"title"/"minecraft.png")
# Vanilla button atlas: keep vanilla atlas dimensions and three button-state rows.
widgets=ROOT/"widgets.png"; widgets.parent.mkdir(parents=True,exist_ok=True)
im=Image.new("RGBA",(256,256),(0,0,0,0)); d=ImageDraw.Draw(im)
for y,base,edge in [(46,(23,13,39,255),(126,78,170,255)),(66,(43,24,65,255),(225,185,105,255)),(86,(13,9,25,255),(85,55,115,255))]:
    d.rectangle((0,y,199,y+19),fill=base,outline=edge,width=1)
    d.line((2,y+2,197,y+2),fill=(255,255,255,30),width=1)
im.save(widgets)
# Reusable dark RPG inventory panels with vanilla 1.12 dimensions.
def panel(path,w,h,title_text):
    path.parent.mkdir(parents=True,exist_ok=True)
    im=Image.new("RGBA",(w,h),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rectangle((0,0,w-1,h-1),fill=(13,9,23,245),outline=(131,83,173,255),width=2)
    d.rectangle((4,4,w-5,24),fill=(35,19,54,255),outline=(188,145,78,255),width=1)
    d.line((7,27,w-8,27),fill=(114,72,151,255),width=1)
    # Subtle rune corners and inner border
    d.rectangle((5,31,w-6,h-6),outline=(61,42,83,210),width=1)
    for x,y in [(8,8),(w-9,8),(8,h-9),(w-9,h-9)]:
        d.polygon([(x,y-3),(x+3,y),(x,y+3),(x-3,y)],fill=(222,178,95,230))
    d.text((w//2,8),title_text,font=font(9,True),anchor="mt",fill=(238,213,160,255))
    im.save(path)
container=ROOT/"container"
panel(container/"inventory.png",176,166,"NEXORA  |  EQUIPMENT")
panel(container/"crafting_table.png",176,166,"NEXORA  |  FORGE")
panel(container/"generic_54.png",176,222,"NEXORA  |  TREASURE")
panel(container/"chest.png",176,166,"NEXORA  |  CHEST")
panel(container/"dispenser.png",176,166,"NEXORA  |  DEVICE")
# GUI overlays / icons for themed menus and hotbar.
icons=ROOT/"icons.png"; im=Image.new("RGBA",(256,256),(0,0,0,0)); d=ImageDraw.Draw(im)
for i in range(16):
    x=(i%16)*16; y=(i//16)*16
    d.rectangle((x+1,y+1,x+14,y+14),outline=(135,90,175,190),width=1)
im.save(icons)
print("Generated NEXORA title panorama, logo, button atlas and RPG inventory panels.")
