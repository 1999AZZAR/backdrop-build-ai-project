# gfpgan

import replicate
import requests

class i2g:
    output = replicate.run(
        "tencentarc/gfpgan:9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3", 
        input={"img": open("/media/azzar/Betha/Download/project/telegram bot/replicate ai/image sample/1100.jpg", "rb")}
    )
    print(output)

    response = requests.get(output)

    file = open("sample_image.png", "wb")
    file.write(response.content)
    file.close()

i2g.instance = i2g()