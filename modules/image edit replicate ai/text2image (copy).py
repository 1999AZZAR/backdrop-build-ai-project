import replicate
import requests

class i2t:
    response = replicate.run(
        "methexis-inc/img2prompt:50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5", # image to prompt
        input={"image": open("/media/azzar/Betha/Download/project/telegram bot/replicate ai/image sample/101.jpg", "rb")}
    )
    print(response)

i2t_instance = i2t()

prompt = i2t_instance.response
nprompt = "tiling, 2 heads, 2 faces, cropped image, out of frame, draft, deformed hands, signatures, twisted fingers, double image, long neck, malformed hands, multiple heads, extra limb, ugly, poorly drawn hands, missing limb, disfigured, cut-off, ugly, grain, low-res, Deformed, blurry, bad anatomy, disfigured, poorly drawn face, mutation, mutated, floating limbs, disconnected limbs, long body, disgusting, poorly drawn, mutilated, mangled, surreal, extra fingers, duplicate artefacts, morbid, gross proportions, missing arms, mutated hands, mutilated hands, cloned face, malformed"
height = 720 # default 1024
width = 1024 # default 1024
sprompt = 0.55 # -1 to 1
refine = "expert_ensemble_refiner" # no_refiner, expert_ensemble_refiner, base_image_refiner
scale = 8.5 # default 7.5
lora_source = "https://pbxt.replicate.delivery/dgeTJ4xBtfqZj0wGnbsoIMSm9sPI5lDzzeyxeQTmCtIeI17LC/trained_model.tar"
inference = 50 # max 50
hnoise = 0.8 # default 0.8 
slora = 0.6 # default 0.6

class t2i:
    _instance = None  # Singleton instance
    
    output = replicate.run(
        # "alexgenovese/sdxl-lora:423422aecd2567600cd6456fdcaef85f21a772e9fa1512311be1eeb4aa0bb0d5",              # image creation
        # "stability-ai/sdxl:2b017d9b67edd2ee1401238df49d75da53c523f36e363881e057f5dc3ed3c5b2",                   # image creation
        # "alexgenovese/sdxl:4b017dc7f7e71d1be25569c854897a433bb4a2bc285b6e1009fce5287d62806c",                   # image creation
        "luosiallen/latent-consistency-model:553803fd018b3cf875a8bc774c99da9b33f36647badfd88a6eec90d61c5f62fc", # image creation
        input={
            "prompt": prompt,
            "negative_prompt" : nprompt,
            "height": height,
            "width": width,
            "prompt_strength" : sprompt,
            "refine": refine,
            "guidance_scale" : scale,
            "lora_url": lora_source,
            "lora_scale": slora,
            "num_inference_steps" : inference,
            "high_noise_frac" : hnoise
            },
    )

    output = output[0]

    print(output)

    response = requests.get(output)

    file = open("sample_image.png", "wb")
    file.write(response.content)
    file.close()

t2i_instance = t2i()
