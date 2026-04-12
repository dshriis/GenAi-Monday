# CSET419 – Lab 11: Fine-Tuning GPT-2 for Real-World Applications

> Fine-tune a pre-trained GPT-2 model for two industry domains: e-commerce product review generation and food-tech recipe instruction generation.

---

## Objective

This lab demonstrates how **transfer learning** and **fine-tuning** adapt a general-purpose language model (GPT-2) to specific business domains — without training from scratch.

---

## Lab Structure

| File | Description |
|---|---|
| `component1_product_review_generator.ipynb` | Fine-tune GPT-2 on product reviews (e-commerce) |
| `component2_recipe_generator.ipynb` | Fine-tune GPT-2 on recipe instructions (food-tech) |

---

## Learning Outcomes

After completing this lab you will be able to:

1. Understand how fine-tuning applies to real-world industry applications
2. Load and configure a pre-trained GPT-2 model using Hugging Face Transformers
3. Prepare domain-specific datasets for causal language modeling
4. Fine-tune the model and compare generated output before and after training
5. Evaluate practical generation quality using perplexity

---

## Requirements

```
torch
transformers
datasets
accelerate
```

Install all dependencies with:

```bash
pip install transformers datasets accelerate -q
```

> **Recommended:** Run on Google Colab with a GPU runtime for faster training.  
> Go to **Runtime > Change runtime type > T4 GPU**.

---

## Component I — Product Review Generator (E-Commerce)

**Scenario:** An e-commerce company wants an AI tool that auto-generates realistic product reviews for demo storefronts and seller guidance.

### Steps
1. Load GPT-2 and generate **baseline** reviews (before fine-tuning)
2. Prepare and tokenize the 20-sample product review corpus
3. Fine-tune for 15 epochs using the Hugging Face `Trainer` API
4. Generate reviews from the fine-tuned model and compare against baseline

### What to Expect

| | Baseline | Fine-Tuned |
|---|---|---|
| Tone | Generic, Wikipedia-style | Conversational, review-style |
| Vocabulary | Broad and unrelated | Domain-specific ("battery life", "highly recommend") |
| Structure | Random | Follows product review patterns |
| Perplexity | High | Lower |

---

## Component II — Recipe Instruction Generator (Food-Tech)

**Scenario:** A food-tech startup is building a smart cooking app that generates step-by-step recipe instructions from a dish name prompt.

### Steps
1. Reload a **fresh** GPT-2 instance (independent of Component I)
2. Prepare and tokenize the 20-sample recipe instruction corpus
3. Fine-tune for 15 epochs
4. Generate recipes from dish-name prompts and compare against baseline

### Training Data Covers
- Butter Chicken
- Pasta Carbonara
- Vegetable Stir Fry
- Chocolate Chip Cookies

### What to Expect

| | Baseline | Fine-Tuned |
|---|---|---|
| Tone | Generic, Wikipedia-style | Instructional, step-by-step |
| Vocabulary | Broad and unrelated | Cooking terms (marinate, simmer, al dente) |
| Flow | Random | Logical sequence: marinate -> cook -> serve |
| Perplexity | High | Lower |

---

## Training Configuration

Both components use identical hyperparameters:

| Parameter | Value |
|---|---|
| Epochs | 15 |
| Batch size | 4 |
| Learning rate | 5e-5 |
| Weight decay | 0.01 |
| Warmup steps | 50 |
| Max token length | 128 |
| Mixed precision (fp16) | Auto (enabled if GPU available) |

---

## Lightweight Model Alternatives

If GPT-2 is too slow for your environment, swap `'gpt2'` in the `from_pretrained()` calls:

| Model | Size | Notes |
|---|---|---|
| `distilgpt2` | 82M | Faster than GPT-2, great for quick runs |
| `EleutherAI/gpt-neo-125M` | 125M | Open-source GPT-3 alternative |
| `TinyLlama/TinyLlama-1.1B-Chat-v1.0` | 1.1B | Efficient on free Colab |
| `Qwen/Qwen2.5-0.5B` | 0.5B | Very capable for its size |
| `facebook/opt-125m` | 125M | Meta's open GPT alternative |

---

## Real-World Applications of Fine-Tuning

- **E-Commerce** — Product descriptions, customer reviews, recommendation text
- **Food-Tech** — Recipe instructions, meal plans, cooking tips
- **Healthcare** — Clinical notes, patient summaries, medical documentation
- **Customer Support** — Context-aware chatbot replies trained on company FAQ data
- **Marketing** — Ad copy, email campaigns, social media posts in brand voice

---

## Notes

- Each component loads its own independent model instance so they do not interfere with each other.
- With only 20 training samples, the model learns domain style and vocabulary rather than memorising specific examples. Production systems use thousands of samples.
- Perplexity is used as the primary evaluation metric — lower perplexity means the model is more confident and consistent within the target domain.
