CSET419 – Generative AI Lab 2
Basic GAN for Image Generation
📌 Overview

This project implements a Basic Generative Adversarial Network (GAN) using PyTorch to generate synthetic images similar to MNIST and Fashion-MNIST. The trained generator is also used to simulate noisy image scenarios and produce realistic samples from the learned data distribution.

📊 Dataset

MNIST (handwritten digits)

Fashion-MNIST (clothing items)

Datasets are loaded via Torchvision and normalized to [-1, 1].


🧠 Model

Generator: Fully connected network mapping noise → 28×28 images

Discriminator: Fully connected network classifying real vs fake images

⚙️ Training

The generator and discriminator are trained alternately using adversarial learning. Loss values are logged per epoch, and generated images are saved periodically.

💾 Model Saving

Trained models are saved using torch.save for reuse without retraining.
