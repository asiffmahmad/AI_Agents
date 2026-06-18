# 🤖 AI Agents Base Template

Welcome to the **AI Agents Base Template**! This repository is designed to serve as the foundational starting point for all your future development projects. It comes pre-configured with a powerful set of AI agents built using the [Google Antigravity SDK](https://github.com/google/antigravity), an automated CI/CD pipeline, and a massive Enterprise AI Prompt Library.

By starting your new projects from this template, you get an automated AI workforce out-of-the-box!

---

## ✨ Features Built-In

### 1. Automated AI Code Reviewer (GitHub Actions)
Every time you push code or open a Pull Request, an AI Code Reviewer automatically analyzes your changes.
- **How it works:** Driven by the `scripts/ai_reviewer.py` script running in GitHub Actions. It is a "Smart Dispatcher" that detects file extensions (Java, TypeScript, React, SQL) and triggers the correct skill.
- **Customization:** You can change exactly how the AI reviews your code without touching Python! Just edit the markdown instructions in the `skills/` directory. 
- **Scoring:** It provides a highly detailed breakdown and assigns a **Code Quality Score out of 100**.

### 2. AI README Generator Agent
Tired of writing documentation? This template includes a dedicated agent that reads your codebase and writes the documentation for you.
- **How it works:** Run `python scripts/readme_generator.py` locally.
- **Capabilities:** It automatically scans your codebase dynamically using glob patterns, understands your project's architecture, and outputs a clean markdown file.

### 3. Enterprise AI Prompt Library (`prompts/`)
A massive collection of over 60 highly structured, professional prompts designed to augment every phase of the software lifecycle. These prompts are ready to be copied and pasted to autonomous AI agents for requirements gathering, architecture planning, code generation, and release management.

### 4. Base Java Spring Boot Application
A pre-configured, compiling Java 17 Spring Boot CRUD application is included in the `java-crud-app/` directory. It uses an H2 in-memory database and comes with standard Entity, Repository, and Controller patterns ready to be extended.

---

## 💻 IDE Independence

**This repository can be used by any developer in any IDE.** 
There is absolutely no lock-in to any specific code editor. The AI agents are built using standard Python and the public `google-antigravity` package. 

**To run the agents locally in ANY editor (VS Code, IntelliJ, Terminal):**
1. Install the SDK: `pip install google-antigravity`
2. Export your API key: `export GEMINI_API_KEY="your_api_key_here"`
3. Run the scripts natively: `python scripts/readme_generator.py`

---

## 🚀 How to Use This Template

### Step 1: Create a New Project
1. On GitHub, click the green **"Use this template"** button to create a brand new repository based on this code.
2. Clone your new repository to your local machine.

### Step 2: Configure the AI (Required)
For the automated AI Code Reviewer to work in GitHub Actions, it needs access to the Gemini API.
1. Get a free API key from [Google AI Studio](https://aistudio.google.com/app/api-keys).
2. Go to your new GitHub Repository -> **Settings** -> **Secrets and variables** -> **Actions**.
3. Create a **New repository secret** named exactly `GEMINI_API_KEY` and paste your key.

---

## 📈 Recommended Development Workflow

The software development lifecycle is fully augmented by autonomous AI agents using the prompt library stored in the `prompts/` directory. The recommended 12-step workflow is:

1. **Project Discovery** → Execute `prompts/project-discovery-and-requirements-analysis.md`
2. **Product Requirements Document (PRD)** → Execute `prompts/create-product-requirements-document.md`
3. **Application User Flow Document** → Execute `prompts/create-application-user-flow-document.md`
4. **Technical Requirements Document (TRD)** → Execute `prompts/create-technical-requirements-document.md`
5. **System Architecture Document** → Execute `prompts/create-system-architecture-document.md`
6. **Feature Implementation Plan** → Execute `prompts/create-feature-implementation-plan.md`
7. **Development Tasks** → Execute `prompts/generate-development-tasks.md`
8. **Development** → Engineers and AI Coders implement the tasks.
9. **Code Review** → Automated analysis via `prompts/review-source-code-quality.md` and related review prompts.
10. **Documentation Update** → Execute the relevant `prompts/update-*.md` prompts to keep architecture and requirements in sync with the code.
11. **Release Preparation** → Execute `prompts/generate-release-notes.md` and `prompts/review-release-readiness.md`.
12. **Production Release** → Execute `prompts/create-production-deployment-checklist.md`.

---

## 🌿 Git Branch Strategy

This repository relies on a robust branching model to preserve AI project knowledge, templates, and standards.

### The `ai-agents` Branch
There is a dedicated, protected branch named `ai-agents`. This branch serves as the source of truth for the project's AI operating system and contains:
* `prompts/`
* `templates/`
* `standards/`
* `documentation-guidelines/`
* `architecture-guidelines/`

### Workflow Rules
1. **Never develop features directly on the `ai-agents` branch**.
2. **Feature Branching**: When starting new development, create a new feature branch (e.g., `feature/user-auth`).
3. **Merging the Core Base**: **Before** writing any code, you must merge the `ai-agents` branch into your new feature branch. This guarantees that your feature branch has access to the latest prompt library, project context, and architecture decision records.
   ```bash
   git checkout -b feature/new-feature
   git merge ai-agents
   ```
4. **Evolving the Prompts**: If you discover that an AI agent needs better instructions, update the corresponding markdown file in the `prompts/` directory and commit it.
5. **Backporting**: Periodically merge updates to the prompt library back into the `ai-agents` branch so that future feature branches inherit the improved AI logic.

---

## 🤖 AI Agent Operating Rules
Every AI agent operating in this repository is strictly bound by the following rules:
1. Think before generating output.
2. Identify missing information.
3. Ask clarifying questions when necessary.
4. Preserve existing project knowledge.
5. Avoid making undocumented assumptions.
6. Reference related documents.
7. Maintain consistency across all project artifacts.
8. Produce professional markdown documentation.
