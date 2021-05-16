import os
from glob import glob
import requests
from PIL import Image,ImageOps
DEEP_AI_API_KEY = 'TOKEN'
bw_image_path = "bw"
colorful_image_path = "cf"
for k in glob(bw_image_path + "/*.png") + glob(bw_image_path + "/*.jpg"):
    pth,ext =(os.path.splitext(k))
    file_name = pth[pth.rindex("\\")+1:]
    file = "{}{}".format(pth,ext)
    print(file)
    img = Image.open(file)
    img = ImageOps.grayscale(img)
    img.save(file)
    
    r = requests.post(
        "https://api.deepai.org/api/colorizer",
        files={
            'image': open("{}".format(file), 'rb'),
        },
        headers={'api-key': DEEP_AI_API_KEY}
    )
    link = r.json()["output_url"]
    print(link)
    download = requests.get(link)
    download_path = "{}/{}".format(colorful_image_path,file_name+ext)
    open(download_path,"wb").write(download.content)
    print(download_path)
