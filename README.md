<h1 align="center">TrackHire</h1>
<p align="center">
An application tracking system (ATS) built using Google GEMINI Pro Vision API, which analyzes job descriptions and matches keywords to provided resumes in PDF format. The app outputs suggestions to improve the resume to better match the job description.
</p>

## Table of Contents

<details>
<summary>Table of Contents</summary>

- [Description](#description)
  - [Table of Contents](#table-of-contents)
 
  - [How to use the Application](#how-to-use-the-application)
  - [Try the Application](#try-the-application)
  - [Technology Stack](#technology-stack)
  - [Features](#features)
  - [CI/CD Pipeline](#cicd-pipeline)
  - [Authors](#authors)
- [License](#license)

</details>

### How to Use the Application:

1. Create a GOOGLE_API_KEY
2. Add it locally to a .env file
3. Clone the repo
4. Install dependencies
5. Run python3 app.py
6. Add a job description by copying and pasting it into the "Job Description" section.
7. Upload a copy of your resume in PDF format.
8. Click the "Submit" button.
9. View the analysis results.

## Try the Application

Access the application on Hugging Face: [ATS Resume Analyzer](https://huggingface.co/spaces/SANDRAMSC/portfolio_project#ats-tracking-system)


## Technology Stack

| Technology | Description                 |
| ---------- | --------------------------- |
| Terraform  | Infrastructure as code      |
| Python     | Programming Language        |
| Streamlit  | Web Framework               |
| Docker     | Containerization            |
| GitHub Actions | CI/CD Automation        |
| AWS (EKS,ECR)    | Cloud Deployment            |
| GEMINI AI  | Job Description Analysis    |
| Hugging Face  | description   |

## Features

- Job Description Analysis:
  - Analyzes job descriptions to extract keywords.
  - Matches keywords to resumes in PDF format.
- Resume Improvement Suggestions:
  - Provides suggestions to improve the resume for better alignment with the job description.
  
## CI/CD Pipeline

Utilized Terraform, Docker, GitHub Actions, AWS EC2, AWS ECR to create a complete CI/CD pipeline. The pipeline automates the deployment process, ensuring efficient and reliable updates to the application.


## Authors

| Name           | GitHub                                      |
| -------------- | ------------------------------------------- |
| Sandra Ashipala | [GitHub](https://github.com/sandramsc) |

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
