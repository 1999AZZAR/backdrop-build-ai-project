# image upscale

import replicate
import requests

image = open("/media/azzar/Betha/Download/project/telegram bot/20230918_140044.jpg", "rb")
task_type = "Real-World Image Super-Resolution-Large" # Real-World Image Super-Resolution-Large, Real-World Image Super-Resolution-Medium, Grayscale Image Denoising, Color Image Denoising, JPEG Compression Artifact Reduction
noise = 15 # 15, 25, 50

class i2u:
    output = replicate.run(
        # "jingyunliang/swinir:660d922d33153019e8c263a3bba265de882e7f4f70396546b6c9c8f9d47a021a",
        "cjwbw/real-esrgan:d0ee3d708c9b911f122a4ad90046c5d26a0293b99476d697f6bb7f2e251ce2d4", # upscale to 4k
        input={
            "image": image,
            "task_type" : task_type,
            "noise" : noise
            }
    )
    print(output)

    response = requests.get(output)

    file = open("sample_image.png", "wb")
    file.write(response.content)
    file.close()

i2u.instance = i2u()
