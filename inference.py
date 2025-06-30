import os
import cv2
import glob
from realesrgan import RealESRGANer
from basicsr.archs.rrdbnet_arch import RRDBNet

# ✅ Config
model_path = 'experiments/license_plate/models/net_g_latest.pth'
input_dir = 'inputs'
output_dir = 'results'

# ✅ Make output folder if not exists
os.makedirs(output_dir, exist_ok=True)

# ✅ Setup model
model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32)
upsampler = RealESRGANer(
    scale=4,
    model_path=model_path,
    model=model,
    tile=0,
    tile_pad=10,
    pre_pad=0,
    half=False
)

# ✅ Loop through all images in input_dir
img_list = glob.glob(os.path.join(input_dir, '*'))

for img_path in img_list:
    print(f'Processing {img_path}...')
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    output, _ = upsampler.enhance(img, outscale=4)
    base_name = os.path.basename(img_path)
    cv2.imwrite(os.path.join(output_dir, f'enhanced_{base_name}'), output)

print(f'Done! Enhanced images saved in `{output_dir}`.')
