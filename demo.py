import cv2
import imageio
from tqdm import tqdm

from basic_transform import (blur, contrast_and_brighten, gamma_saturation,
                             lcd_overlay, noise, rotate, scanner_like, shadow,
                             watermark, wrinkles)
from distortion import distort, perspective, stretch

augmentations = [
    rotate,
    shadow,
    watermark,
    wrinkles,
    lcd_overlay,
    gamma_saturation,
    contrast_and_brighten,
    scanner_like,
    distort,
    perspective,
    stretch,
    blur,
    noise,
]

image = cv2.imread("data/sample.jpg")

def apply_aug(img, fn, args=[]):
    res = fn(img,*args,)
    return res[:, :, ::-1]

# result = apply_aug(image,watermark,["COPY",(20,20,20)]) #watermark
# cv2.imwrite('output2/res_mark.jpg', result)


result = apply_aug(image,lcd_overlay) 
cv2.imwrite('output2/res_lcd.jpg', result)

# result = apply_aug(image,wrinkles)  #揉搓变形
# cv2.imwrite('output2/res_wrinkles.jpg', result)

# result = apply_aug(image,scanner_like) 
# cv2.imwrite('output2/res_scanner.jpg', result)

# result = apply_aug(image,noise,["s&p"]) 
# cv2.imwrite('output2/res_noise.jpg', result)

# result = apply_aug(image,stretch)  #拉伸变形
# cv2.imwrite('output2/res_stretch.jpg', result)

# result = apply_aug(image,perspective)  #透视变形
# cv2.imwrite('output2/res_perspective.jpg', result)

# result = apply_aug(image,blur) 
# cv2.imwrite('output2/res_blur.jpg', result)

result = apply_aug(image,gamma_saturation) 
cv2.imwrite('output2/res_gamma.jpg', result)









# def create_gif(image_list, gif_name, duration=1):
#     frames = []
#     for image in image_list:
#         frames.append(image)
#     imageio.mimsave(gif_name, frames, "GIF", duration=duration)
#     return


# for aug in tqdm(augmentations):
#     aug_list = []
#     for i in range(5):
#         result = aug(image)
#         aug_list.append(result[:, :, ::-1])
#     create_gif(aug_list, f"output2/{aug.__name__}.gif")






















