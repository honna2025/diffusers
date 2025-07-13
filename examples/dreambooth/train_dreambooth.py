from google.colab import drive
drive.mount(https://drive.google.com/drive/folders/1WCJ4Hl1nSCUvbVDZoU-jUpNalnGLueca?usp=sharing)
!pip install diffusers transformers accelerate
from diffusers import StableDiffusionPipeline
model_id = "CompVis/stable-diffusion-v1-4"
