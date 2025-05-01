# API Test Automation CI/CD Pipeline

## Project Overview

This repository contains end-to-end API test automation for the Restful Booker API using Python, Pytest, and Requests. It includes local test execution and a GitHub Actions pipeline that runs tests, generates an HTML report, and uploads the report as an artifact.

## Tools Used

- Python
- Pytest
- Requests
- Pytest HTML report
- GitHub Actions

## Folder Structure

- `tests/` - API test cases.
- `utils/` - Reusable API client, configuration, and payload helpers.
- `.github/workflows/` - GitHub Actions CI workflow definition.
- `reports/` - Generated HTML reports.

## Test Scenarios

- Health check for Restful Booker API.
- Retrieve booking IDs.
- Create a booking.
- Retrieve booking by ID.
- Update a booking.
- Delete a booking.

## How to Run Locally

1. Create a virtual environment:

```powershell
python -m venv .venv
```

2. Activate the virtual environment:

```powershell
.venv\Scripts\activate
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Run tests:

```powershell
pytest
```

5. Generate HTML report:

```powershell
pytest --html=reports/ci_report.html --self-contained-html
```

## GitHub Actions CI

The workflow is defined in `.github/workflows/ci-tests.yml`. It triggers on `push` and `pull_request`, checks out the repository, sets up Python, installs dependencies, runs `pytest`, generates an HTML report, and uploads the report as an artifact.

## Downloading the Report Artifact

After a workflow run completes, open the GitHub Actions run page and download the `pytest-html-report` artifact from the artifacts section.
