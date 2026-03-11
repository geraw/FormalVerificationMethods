# Formal Verification Methods Presentations

Interactive slide decks for the Formal Verification Methods course content, built with [Slidev](https://sli.dev/).

🚀 **Live Demo:** [https://geraw.github.io/FormalVerificationMethods/](https://geraw.github.io/FormalVerificationMethods/)

## 🛠 Installation

```bash
# Clone the repository
git clone https://github.com/geraw/FormalVerificationMethods.git
cd FormalVerificationMethods

# Install dependencies
npm install
```

## 🚀 Running Locally

Launch the presentation server for specific topics:

```bash
# Main Index
npm run dev

# Course Introduction
npm run dev:intro

# Z3 Theorem Prover
npm run dev:z3
```

## 📦 Deployment

The presentations are automatically deployed to GitHub Pages on every `push` to the `main` branch using GitHub Actions.

To build manually:
```bash
# Build all decks
npm run build:all
```
