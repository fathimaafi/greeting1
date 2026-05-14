[![Run Tests](https://github.com/fathimaafi/greeting/actions/workflows/python-tests.yml/badge.svg)](https://github.com/fathimaafi/greeting/actions/workflows/python-tests.yml)

# Greeter Project

A simple Python project that greets users and includes automated tests. It features a basic command-line interface and a modular `greet` function.

## Status Badge
The badge at the top of this README reflects the current state of the CI pipeline on the `main` branch:

| Badge | Meaning |
|---|---|
| ![passing](https://img.shields.io/badge/build-passing-brightgreen) | All Pylint and unit tests passed successfully |
| ![failing](https://img.shields.io/badge/build-failing-red) | One or more Pylint checks or unit tests failed |
| ![no status](https://img.shields.io/badge/build-no--status-lightgrey) | No workflow has run yet on this branch |

The badge is generated from the workflow file `.github/workflows/python-tests.yml` and updates automatically after every push to `main` or pull request. Click the badge to navigate directly to the Actions page for full run details.

## Project Structure

- `greeter.py`: Core logic with a `greet` function and an interactive command-line interface.
- `test_greet.py`: Unit tests using the `unittest` framework to verify the greeting logic.
- `requirements.txt`: Project dependencies (Pylint).
- `.github/workflows/python-tests.yml`: GitHub Actions workflow configuration for automated testing and linting.

## How to Run Locally

### 1. Install Dependencies
Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

### 2. Run the Greeter Script
To run the interactive script, execute the following command from the project root:

```bash
python greeter.py
```

### 3. Run Tests
To run the unit tests and verify the project, use the following command:

```bash
python -m unittest discover -s . -p test_greet.py -v
```

### 4. Linting
This project uses **Pylint** for static code analysis.

#### What is Linting?
Linting is the process of running a tool (a "linter") that analyzes your source code for potential errors, bugs, stylistic issues, and suspicious constructs. It helps maintain code quality, ensures consistency across the codebase, and can catch common mistakes before they become run-time issues.

#### How to Run Linting Locally
Run Pylint on the project files:

```bash
python -m pylint greeter.py test_greet.py
```

## GitHub Actions
The project includes a GitHub Actions workflow located in `.github/workflows/python-tests.yml`. This workflow automatically runs Pylint and unit tests on every push to the `main` branch or when a pull request is created. This ensures that the codebase remains stable and follows quality standards.

### Triggering the Workflow Manually
You can also manually run the GitHub Actions workflow from the GitHub repository:
1. Navigate to the **Actions** tab in your repository.
2. Select the **Run Tests** workflow from the left sidebar.
3. Click the **Run workflow** dropdown button.
4. Select the branch you want to run the workflow on and click **Run workflow**.

### Failure Notifications
If the CI workflow fails (either during linting or unit tests), an automated notification email will be sent to the designated recipient.

To enable this feature, the following **Secrets** must be configured in the GitHub repository (`Settings > Secrets and variables > Actions`):
- `MAIL_USERNAME`: The SMTP sender email address (e.g., a Gmail address).
- `MAIL_PASSWORD`: The Gmail App Password (generated at Google Account → Security → 2-Step Verification → App passwords).
- `MAIL_RECIPIENT`: The email address that should receive the failure reports.

The workflow uses these secrets with the `dawidd6/action-send-mail` action to provide immediate alerts for failed builds.

## Artifacts
The workflow uploads a `test-results.txt` artifact after every run containing the full Pylint and test output regardless of pass or failure.

### What the Artifact Contains
The artifact file is structured in three sections:
```
=== PYLINT RESULTS ===
<pylint output and score>
Pylint status: PASSED | FAILED (exit code: <code>)

=== TEST RESULTS ===
<unittest output with pass/fail details>
Test status: PASSED | FAILED (exit code: <code>)

=== OVERALL STATUS ===
Result: SUCCESS - All checks passed | FAILED
  - Pylint failed with exit code <code>
  - Tests failed with exit code <code>
```

### How to Access Artifacts
1. Navigate to the **Actions** tab in your GitHub repository.
2. Click on the workflow run you want to inspect.
3. Scroll down to the **Artifacts** section at the bottom of the run summary page.
4. Click **My Artifact for test results** to download the zip file.
5. Extract the zip and open `test-results.txt` to view the full Pylint and test output.

### Interpreting the Artifact
- **Pylint status PASSED** — no linting issues found, score is 10.00/10.
- **Pylint status FAILED** — linting issues found with details of each issue and exit code.
- **Test status PASSED** — all tests passed successfully.
- **Test status FAILED** — one or more tests failed with `AssertionError` details showing expected vs actual values.
- **Overall Result SUCCESS** — both Pylint and tests passed.
- **Overall Result FAILED** — one or both of Pylint and tests failed with exit codes listed.

## Pull Requests and CI
To maintain the quality of the project, all changes should be submitted through Pull Requests (PRs).

### 1. Creating a Pull Request
- Create a new branch for your changes: `git checkout -b feature-name`.
- Commit and push your changes to your fork or the repository.
- Open a Pull Request against the `main` branch on GitHub.

### 2. Continuous Integration (CI)
- Once a PR is opened, the GitHub Actions CI workflow will automatically trigger.
- It will install dependencies from `requirements.txt`, run **Pylint** for code quality, and execute the **unittest** suite.
- You can monitor the progress in the **Checks** tab of your PR.

### 3. Reviewing a Pull Request
- **Check CI Status:** Ensure all checks have passed (indicated by a green checkmark). If any checks fail, review the logs in the GitHub Actions tab to identify and fix the issues.
- **Code Review:** Review the code for logic, readability, and adherence to project standards.
- **Merge:** Once the CI passes and the code is approved, the PR can be safely merged into the `main` branch.
