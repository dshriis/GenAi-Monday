# CSET419 - Introduction to Generative AI: Lab 10

## Lab Objective

The objective of this lab is to implement a generative model capable of learning patterns from sequential data and generating new sequences. This project explores sequence generation using deep learning architectures such as Recurrent Neural Networks (RNN), Long Short-Term Memory (LSTM) networks, and Transformer models.

---

## What is Sequential Data Generation?

Sequential data generation is the process where a machine learning model learns underlying patterns from ordered data and generates entirely new sequences that logically follow those exact patterns.

Unlike static data (like a single image), sequential data relies heavily on **context and order**. The meaning of a data point is dependent on what came before it. Examples of sequential data include:

- Text sentences
- Speech signals
- Time-series data
- Music compositions
- DNA sequences

To achieve this, generative models learn the probability distribution of the training sequences. When given a starting prompt, they calculate the mathematical probability of every possible next element and predict what should come next based on previous elements. Common approaches include Markov Models, N-gram Language Models, RNNs, LSTM/GRU Networks, and Transformer Models.

---

## The Data Preparation Pipeline (The Basics)

Neural networks cannot process raw English text; they only understand numbers. Before we can train any model, we must pass the text through a strict preprocessing pipeline.

### 1. Tokenization

Tokenization is the process of breaking down raw text into smaller, digestible pieces called "tokens."

- **Character-level Tokenization:** Breaking a sentence into individual letters (e.g., "c", "a", "t").
- **Word-level Tokenization:** Breaking a sentence into whole words (e.g., "machine", "learning").
  Each unique token is then assigned a specific integer ID (an index). This creates a "Vocabulary" dictionary mapping words to numbers.

### 2. N-Gram Sequences (The Sliding Window)

To teach a model how to predict the next word, we must show it examples of context. We create a "sliding window" of input-output pairs over our tokenized sentences.
For the sentence: _"deep learning models improve"_

- **Step 1:** Input: `[deep]` -> Label: `[learning]`
- **Step 2:** Input: `[deep, learning]` -> Label: `[models]`
- **Step 3:** Input: `[deep, learning, models]` -> Label: `[improve]`

### 3. Padding

Neural networks require input matrices to have uniform, fixed dimensions. Because sentences are naturally different lengths, our n-gram sequences will also be different lengths. We fix this by "padding" the sequences—adding zeroes to the beginning (`padding='pre'`) or end of the arrays until they all match the length of the longest sequence in the dataset.

### 4. Word Embeddings

Instead of just passing raw integer IDs into the network, we use an Embedding Layer. This layer transforms each integer into a dense vector (an array of floating-point numbers) in a multi-dimensional space. Words that are used in similar contexts will mathematically cluster closer together in this space, giving the model a fundamental "understanding" of word relationships.

---

## Core Architectures

### Component I: Recurrent Neural Networks (RNN) & LSTMs

Traditional deep neural networks assume all inputs are independent of each other. RNNs were created to solve this by introducing a **Hidden State** (short-term memory).

- **How an RNN works:** As an RNN processes a sequence step-by-step, it takes the current word AND the hidden state from the previous word to make its calculation.
- **The Vanishing Gradient Problem:** Standard RNNs struggle with long sequences. During training, as errors are backpropagated through many time steps, the gradients shrink to zero. The network effectively "forgets" the beginning of a long sentence by the time it reaches the end.

**The LSTM Upgrade:**
Long Short-Term Memory (LSTM) networks were explicitly designed to handle long-term dependencies. They replace the simple RNN cell with a complex architecture containing a **Cell State** (a conveyor belt carrying information through the whole sequence) and three **Gates**:

1.  **Forget Gate:** Decides what irrelevant information to throw away from the cell state.
2.  **Input Gate:** Decides what new information is important enough to add to the cell state.
3.  **Output Gate:** Decides what the next hidden state should be based on the updated cell state.

### Component II: Transformer Models

Transformers are the foundational architecture behind modern Large Language Models (LLMs). Instead of processing sequences step-by-step like RNNs, Transformers process the entire sequence **simultaneously** in parallel.

- **Positional Encoding:** Because the Transformer processes all words at once, it loses the inherent concept of order. We must manually inject a mathematical "Positional Vector" into the word embeddings so the model knows the exact position of a word in a sentence.
- **Multi-Head Self-Attention:** This is the core engine. It allows the model to look at a single word and simultaneously calculate how strongly it relates to _every other word_ in the entire sequence. "Multi-Head" means it performs this attention calculation multiple times in parallel, allowing it to grasp different types of relationships (e.g., one head might track grammar, while another tracks emotional tone).

---

## Text Generation Strategies (Decoding)

Once the model is trained, it acts as a probability engine. If given the input "machine learning", the final Softmax layer outputs a probability score for every word in the vocabulary being the next word. How we choose that word matters:

### 1. Greedy Decoding (`argmax`)

- **How it works:** The model always picks the single word with the highest absolute mathematical probability.
- **The Problem:** It lacks creativity and is highly prone to getting stuck in infinite loops (e.g., "learning learning learning"), especially on small training datasets.

### 2. Stochastic Sampling & Temperature

- **How it works:** Instead of always taking the top choice, the model treats the probabilities like a weighted roulette wheel and randomly rolls for the next word.
- **Temperature Scaling:** A hyperparameter that adjusts those probabilities before the roll:
    - **Low Temperature (e.g., 0.2):** Makes the model "confident" by exaggerating high probabilities and shrinking low ones. Output is safe and predictable.
    - **Medium Temperature (e.g., 0.7):** A balanced mix of coherence and creativity.
    - **High Temperature (e.g., 1.5):** Flattens the probabilities, giving unlikely words a much higher chance of being picked. Output is highly creative but risks becoming chaotic gibberish.
