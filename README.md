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

To run a specific slide deck (e.g., `03-parallelism-and-concurrency.md`):

```bash
npx slidev ./03-parallelism-and-concurrency.md
```

You can also use the predefined npm scripts:

```bash
# Main Index
npm run dev

# Course Introduction
npm run dev:intro
npm run dev:00

# Module 01 - Transition Systems
npm run dev:01

# Module 02 - Program Graphs
npm run dev:02

# Module 03 - Parallelism and Concurrency
npm run dev:03

# Module 04 - Channel Systems
npm run dev:04

# Module 05 - NanoPromela
npm run dev:05

# Module 06 - SMV
npm run dev:06

# Module 07 - State Explosion
npm run dev:07
```

## 📦 Deployment

The presentations are automatically deployed to GitHub Pages on every `push` to the `main` branch using GitHub Actions.

To build manually:
```bash
# Build all decks (HTML + one-file PDF per presentation)
npm run build:all
```

Generated PDFs are written next to each deck build output, for example:

```text
dist/01-transition-systems/01-transition-systems.pdf
dist/22-ltl/22-ltl.pdf
```
