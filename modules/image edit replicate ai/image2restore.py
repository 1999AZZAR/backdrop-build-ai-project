# restoration broken image

import replicate
import requests

image = open("/media/azzar/Betha/Download/project/telegram bot/20230918_140044.jpg", "rb")
task    = "Face Restoration" # Face Restoration, Face Colorization, Face Inpainting

class i2r:
    output = replicate.run(
        # "microsoft/bringing-old-photos-back-to-life:c75db81db6cbd809d93cc3b7e7a088a351a3349c9fa02b6d393e35e0d51ba799",
        # "yangxy/gpen:cf4e15a70049c0119884eb2906c8ae8807af8317bea98313fefd941e414d0c91",
        "cjwbw/daclip-uir:73496e1d669145e494f61f1f8385522063de91fc9949d8726562ec782ba94232", 
        input={
            "image": image,
            "HR" : True,
            "task": task,
            "output_individual": False,
            "broken_image": False
        },
    )

    # output = output[0]
    print(output)

    response = requests.get(output)

    file = open("sample_image.png", "wb")
    file.write(response.content)
    file.close()

i2r_instance = i2r()

# link : 
# https://replicate.com/microsoft/bringing-old-photos-back-to-life
# https://replicate.com/yangxy/gpen
