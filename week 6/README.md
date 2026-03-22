# CSET419 – Lab 6: Pix2Pix GAN

Image-to-image translation using a U-Net Generator and PatchGAN Discriminator, compared against a baseline CNN encoder-decoder.

## What This Lab Does

Takes edge sketches of shoes as input and generates realistic shoe images using a Pix2Pix GAN.

```
Edge Sketch  →  [Pix2Pix GAN]  →  Realistic Shoe Photo
```

## Models

| Model | Architecture | Loss |
|-------|-------------|------|
| **Pix2Pix GAN** | U-Net + PatchGAN Discriminator | Adversarial + L1 |
| **Baseline CNN** | U-Net Encoder-Decoder | MSE + L1 only |

## Dataset

[Edges2Shoes](http://efrosgans.eecs.berkeley.edu/pix2pix/datasets/edges2shoes.tar.gz) — paired edge sketches and real shoe photos.

## How to Run

1. Open `genAI_lab6_simple.ipynb` in Google Colab
2. Set Runtime → Change runtime type → **T4 GPU**
3. Run all cells top to bottom

## Requirements

No installs needed — all libraries are pre-installed in Google Colab.

- PyTorch
- torchvision
- matplotlib
- Pillow
- tqdm

## Results

After training, the notebook shows:
- Side-by-side visual comparison of Pix2Pix vs Baseline CNN outputs
- Training loss curves (Generator, Discriminator, L1)
- Quantitative metrics: MSE, L1, PSNR

## Key Concepts

- **U-Net** — encoder-decoder with skip connections that preserve spatial detail
- **PatchGAN** — discriminator that scores local patches instead of the whole image
- **Adversarial loss** — forces the generator to produce sharp, realistic textures
- **L1 loss** — keeps the output structurally close to the real image
