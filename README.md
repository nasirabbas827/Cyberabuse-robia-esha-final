# Cyberabuse Robia Esha Final

Cyberabuse-robia-esha-final is a text classification application for detecting abusive comments.

![Flask](https://img.shields.io/badge/Flask-2563EB?style=flat-square)

## Overview

The Flask implementation is organized around the entry points and modules below.

## Implemented workflows

The source defines these handlers:

- **Home** — `home`

## Getting started

### 1. Get the project

```bash
git clone https://github.com/nasirabbas827/Cyberabuse-robia-esha-final.git
cd Cyberabuse-robia-esha-final
```

### 2. Prepare Python

Create an isolated environment:

```bash
python -m venv .venv
```

Activate it with `.venv\Scripts\activate` on Windows Command Prompt, or `source .venv/bin/activate` on macOS/Linux.

No requirements file is included. The inspected Python imports indicate these dependencies as a starting point:

```bash
python -m pip install Flask joblib scikit-learn
```

Dependency versions are not pinned in this repository.

### 3. Configure and run

Run from the repository root so relative file paths resolve correctly:

```bash
python app.py
```

Open http://127.0.0.1:5000/, or use the address printed by the application.

### Model files

Included artifacts: [`models/multinomial_naive_bayes_model.joblib`](models/multinomial_naive_bayes_model.joblib), [`models/random_forest_model.joblib`](models/random_forest_model.joblib), [`models/svm_(linear_kernel)_model.joblib`](models/svm_%28linear_kernel%29_model.joblib), [`models/tfidf_vectorizer.joblib`](models/tfidf_vectorizer.joblib).

Keep models, preprocessing objects, and label mappings together in the locations expected by the source.

## Repository guide

| Path | Purpose |
| --- | --- |
| [`app.py`](app.py) | Application entry point |
| [`models`](models) | Model resources |
| [`templates`](templates) | HTML page templates |

## Development notes

These setup instructions are based on the repository source. The application has not been executed as part of this documentation update; verify dependencies and configuration in your local environment.
