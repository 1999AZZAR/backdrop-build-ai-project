# image age modifier

import replicate
import requests

image = open("path to file", "rb")
age = "30"

class i2a:
    output = replicate.run(
        "yuval-alaluf/sam:9222a21c181b707209ef12b5e0d7e94c994b58f01c7b2fec075d2e892362f13c",
        input={
            "image": image,
            "target_age": age
            }
    )
    print(output)

    response = requests.get(output)

    file = open("sample_image.png", "wb")
    file.write(response.content)
    file.close()

i2a.instance = i2a()
