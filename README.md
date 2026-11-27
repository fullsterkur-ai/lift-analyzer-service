# Lift Analyzer Service

> Analyzes lifts for Fullsterkur.ai. Tracks movement from video to assess lift quality and technique.

<br />
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#tech-stack">Tech Stack</a></li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#running-the-service">Running the Service</a></li>
      </ul>
    </li>
    <li><a href="#scripts-and-tools">Scripts and Tools</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
  </ol>
</details>

---

## Tech Stack

| <img src="https://raw.githubusercontent.com/github/explore/main/topics/python/python.png" width="60" /> | <img src="https://raw.githubusercontent.com/github/explore/main/topics/opencv/opencv.png" width="60" /> | <img src="https://mediapipe.dev/images/mediapipe_small.png" width="60" /> | <img src="https://raw.githubusercontent.com/github/explore/main/topics/tensorflow/tensorflow.png" width="60" /> | <img src="https://raw.githubusercontent.com/github/explore/main/topics/fastapi/fastapi.png" width="60" /> |
|:---:|:---:|:---:|:---:|:---:|
| **Python**<br>Language the service is built in. | **OpenCV**<br>Reads and processes video frames before they're passed to the pose model. | **MediaPipe**<br>Tracks body and barbell landmarks from video to analyze lift form. | **TensorFlow**<br>Trains and runs the models that score lift technique and detect faults. | **FastAPI**<br>Serves the analysis to the Mobile app over HTTP. |

---

## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [UV](https://docs.astral.sh/uv/getting-started/installation/)

### Installation

1. Clone the repo
   ```
   git clone https://github.com/fullsterkur-ai/lift-analyzer-service.git
   cd lift-analyzer-service
   ```
2. Setup project environment
   ```
   uv sync
   ```
3. Prepare dev tooling
   ```
   python .githooks/prepare.py
   ```
   
### Running the Service

```
uv run fastapi dev --port 8001
```

---

## Scripts and Tools

The following commands are available for formatting and linting the codebase.

| Command | Description |
|---|---|
| `uv run ruff format --check .` | Check code formatting |
| `uv run ruff format .` | Automatically format code |
| `uv run ruff check .` | Check for linting issues |
| `uv run ruff check --fix .` | Automatically fix linting issues |

---


## Project Structure

```
lift-analyzer-service/
├── artifacts/   # Trained models and training outputs
├── data/        # Datasets
├── ml/          # Model/pose analysis code
└── requirements.txt
```

---

## See Also

- [Main repository README](https://github.com/fullsterkur-ai/J26-SE-342): project overview, architecture, components, and team
- [DEVELOPMENT.md](https://github.com/fullsterkur-ai/J26-SE-342/blob/main/DEVELOPMENT.md): coding conventions and branching/merging strategy

<p align="right">(<a href="#lift-analyzer-service">back to top</a>)</p>
