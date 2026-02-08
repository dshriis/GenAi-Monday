# 🧠 Variational Autoencoder (VAE) – Image Generation Lab

## 📌 Objective

Implement and train a Variational Autoencoder (VAE) that:
- Learns latent representations of image data
- Reconstructs input images with high fidelity
- Generates new, unseen images using the MNIST handwritten digits dataset
- Visualizes the learned latent space

---

## 🤖 What is a Variational Autoencoder (VAE)?

A Variational Autoencoder is a **generative deep learning model** that learns a **probability distribution** over data instead of fixed encodings. Unlike standard autoencoders, VAEs enable:
- **Smooth latent representations** – interpolation between data points
- **Diverse generation** – sampling from learned probability distribution
- **Interpretable latent space** – meaningful dimensions (especially with 2D latent space)

---

## 🔹 VAE Architecture

### **Encoder**
- Compresses input images (28×28) into a probabilistic latent representation
- Outputs mean vector (μ) and log-variance (log σ²)
- Creates a continuous latent space

### **Reparameterization Trick**
Enables backpropagation through randomness by reformulating sampling:

$$z = \mu + \sigma \cdot \epsilon$$

where $\epsilon \sim \mathcal{N}(0, I)$

### **Decoder**
- Reconstructs images from latent vectors
- Enables generation of new images from randomly sampled latent points
- Outputs sigmoid activation for pixel values in [0,1]

---

## 🧩 Implementation Configuration

| Parameter | Value |
|-----------|-------|
| **Dataset** | MNIST (handwritten digits) |
| **Image Size** | 28×28 pixels (grayscale) |
| **Batch Size** | 128 |
| **Epochs** | 20 |
| **Latent Dimension** | 2 |
| **Optimizer** | Adam (lr=1e-3) |
| **Loss Function** | Reconstruction Loss (BCE) + KL Divergence |
| **Train/Test Split** | 60,000 / 10,000 |

---

## 📊 Loss Function Components

**Total Loss = Reconstruction Loss + β × KL Divergence**

- **Reconstruction Loss (BCE):** Measures how well decoded images match originals
- **KL Divergence:** Regularizes latent space to follow standard normal distribution
- **β (Beta):** Weight balancing reconstruction vs. regularization

---

## 🖼️ Expected Results

✅ **Reconstruction Quality**
- Reconstructed images closely resemble original digits
- Minimal pixel-level differences for test samples

✅ **Generation Quality**
- Generated images are novel and diverse
- Smooth transitions between digit classes in latent space

✅ **Training Dynamics**
- Overall loss decreases steadily (indicates stable learning)
- Reconstruction and KL loss balance over epochs

---

## 🚀 Key Features to Explore

1. **Latent Space Visualization** – 2D scatter plot of encoded test samples colored by digit class
2. **Image Interpolation** – Generate smooth transitions between two digits
3. **Random Generation** – Sample from standard normal and decode to create new digits
4. **Reconstruction Analysis** – Compare original vs. reconstructed images

---

## ✅ Conclusion

The Variational Autoencoder successfully:
- Learns a **structured latent space** with meaningful dimensions
- Enables **effective image reconstruction** across training and test sets
- Supports **diverse image generation** from sampled latent vectors
- Demonstrates the power of **probabilistic generative modeling**

we implemented a Variational Autoencoder (VAE) using PyTorch and trained it on the MNIST handwritten digits dataset.
We built an encoder that maps input images to a latent probability distribution defined by mean and log-variance, applied the reparameterization trick to sample latent vectors, and used a decoder to reconstruct images.
The model was trained using a combined loss function consisting of Binary Cross-Entropy reconstruction loss and KL-divergence loss.
After training, we evaluated the model by reconstructing test images, generating new digit samples from random latent vectors, and visualizing the training loss curve to analyze learning behavior.