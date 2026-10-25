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

### Installation

1. Clone the repo
   ```
   git clone https://github.com/fullsterkur-ai/lift-analyzer-service.git
   cd lift-analyzer-service
   ```
2. Create and activate a virtual environment
   ```
   python -m venv .venv
   ```
   Windows:
   ```
   .venv\Scripts\activate
   ```
   macOS/Linux:
   ```
   source .venv/bin/activate
   ```
3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

### Running the Service

```
uvicorn main:app --reload
```

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
