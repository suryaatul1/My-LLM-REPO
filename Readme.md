# 🧠 My-LLM-Repo

A personal exploration into how Large Language Models (LLMs) like **GPT-2** are built — from scratch.  
This repository contains my experiments, notes, and code for constructing a **mini GPT-2–style transformer** model, purely for **learning and research purposes**.

---

## 🚀 Project Overview

This project is inspired by “Build an LLM from Scratch” resources and aims to deepen my understanding of:
- Tokenization and embedding mechanisms  
- Transformer architecture (multi-head self-attention, feed-forward layers)  
- Positional encodings and layer normalization  
- Training objectives like next-token prediction  
- Scaling, optimization, and evaluation of small LLMs  

The goal is not to compete with production models — but to **learn by doing** 🧩.

---

## 🏗️ Architecture

This model follows a **GPT-2–like structure**, including:

- **Embedding layer** for token + positional embeddings  
- **Transformer blocks** with:
  - Multi-Head Self-Attention  
  - Layer Normalization  
  - Feed-Forward Network (MLP)
- **Causal Masking** for autoregressive training  
- **Language Modeling Head** for token prediction  

🧩 **Framework:** PyTorch  
📚 **Reference Architecture:** GPT-2  

---

## 🧪 Current Features

✅ Tokenizer (basic whitespace/BPE style)  
✅ Model forward pass and training loop  
✅ Configurable hyperparameters (layers, heads, embedding size)  
✅ Text generation using top-k sampling  
✅ Evaluation with simple perplexity metrics  

---

🎓 Learning Focus

This repo is primarily for educational purposes, to understand:
How transformers process and generate text
Why attention mechanisms work
How optimization and token prediction are implemented
How scaling affects model performance



## Reference
“Build an LLM from Scratch” guides,github and tutorials --  Sebastian Raschka 
GPT-2 Paper: Language Models are Unsupervised Multitask Learners (OpenAI, 2019)a
YouTube Series: Building LLM from Scratch by Dr. Raj Dandekar


---

## ⚙️ Setup & Usage

### 1️⃣ Clone the repo
```bash
git clone https://github.com/<your-username>/My-LLM-Repo.git
cd My-LLM-Repo



