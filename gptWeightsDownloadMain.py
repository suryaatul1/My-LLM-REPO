import os
from downloadModelWeights import download_and_load_gpt2

if __name__ == "__main__":
   test=  download_and_load_gpt2(model_size="124M", models_dir="gpt2")