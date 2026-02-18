# OrangeHRM QA Automation


## 1. Project Overview
This project is a Python + Playwright + Pytest-BDD automation framework for OrangeHRM My Info module coverage.

It uses:
- `pytest` for test execution
- `pytest-bdd` for feature-driven test definitions
- `playwright` for browser automation
- `allure-pytest` for report generation

## 2. Tech Stack
- Python 3.10+ (validated on Python 3.14)
- Playwright (`chromium`)
- Pytest
- Pytest-BDD
- Allure results integration

## 3. Folder Structure
```text
Assesment 5/
|-- config/
|   |-- settings.py
|-- core/
|   |-- browser_manager.py
|-- data/
|   |-- uploads/
|-- features/
|   |-- my_info/
|   |   |-- login.feature
|   |   |-- myinfo.feature
|   |   |-- personal_details.feature
|   |   |-- crud.feature
|   |   |-- restricted.feature
|   |   `-- uploads.feature
|-- pages/
|   |-- login_page.py
|   `-- my_info_page.py
|-- steps/
|   |-- auth_steps.py
|   |-- common_steps.py
|   |-- navigation_steps.py
|   |-- crud_steps.py
|   |-- restricted_steps.py
|   `-- upload_steps.py
|-- tests/
|   |-- test_bdd_runner.py
|   `-- test_myinfo_bdd.py
|-- reports/
|   `-- allure-results/
|-- conftest.py
|-- pytest.ini
|-- requirements.txt
|-- run.ps1
`-- README.md
```

## 4. Configuration
Environment variables are loaded from `.env` through `config/settings.py`.

Required keys:
- `ORANGEHRM_BASE_URL`
- `ESS_USERNAME`
- `ESS_PASSWORD`
- `ADMIN_USERNAME`
- `ADMIN_PASSWORD`
- `HEADLESS`
- `BROWSER`

Example:
```env
ORANGEHRM_BASE_URL=https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
ESS_USERNAME=your_ess_user
ESS_PASSWORD=your_ess_password
ADMIN_USERNAME=Admin
ADMIN_PASSWORD=admin123
HEADLESS=false
BROWSER=chromium
```

## 5. Setup Steps
1. Open terminal in project root.
2. Create virtual environment.
3. Activate virtual environment.
4. Install Python dependencies.
5. Install Playwright browser binaries.

Windows PowerShell:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## 6. Test Run Commands
Run all tests:
```powershell
python -m pytest
```

Run all tests with concise output:
```powershell
python -m pytest -q
```

Run collection only:
```powershell
python -m pytest --collect-only -q -p no:cacheprovider
```

Run by feature test file:
```powershell
python -m pytest tests\test_myinfo_bdd.py -v
```

Run from helper script:
```powershell
.\run.ps1
```

## 7. Reporting
Pytest is configured to write Allure raw results to:
- `reports/allure-results`

Generate and open report (if Allure CLI is installed):
```powershell
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

## 7.1 GitHub Actions CI/CD
This repo includes CI/CD workflow at:
- `.github/workflows/ci-cd.yml`

Pipeline behavior:
- `CI`: runs on `push`, `pull_request`, and `workflow_dispatch`
- installs Python deps + Playwright Chromium
- executes pytest with Allure raw result output
- uploads Allure raw results as workflow artifact
- builds Allure HTML report
- deploys report to `gh-pages` on pushes to `main` or `master`

Required GitHub repository secrets:
- `ORANGEHRM_BASE_URL`
- `ESS_USERNAME`
- `ESS_PASSWORD`
- `ADMIN_USERNAME`
- `ADMIN_PASSWORD`

Setup steps:
1. Push the workflow file to your GitHub repository.
2. Add the required secrets in `Settings -> Secrets and variables -> Actions`.
3. Enable Actions for the repository.
4. Trigger the workflow from `Actions` tab or by pushing to `main`/`master`.
5. After successful publish, open the `gh-pages` branch output for Allure report.

## 8. Working Flow Design
### 8.1 High-Level Flow
1. `tests/*.py` loads scenarios from `features/`.
2. Scenario steps bind to functions in `steps/`.
3. Step functions call page object methods in `pages/`.
4. Page objects use Playwright API to interact with browser.
5. Browser lifecycle and reusable fixtures are managed by `conftest.py`.
6. Runtime settings come from `config/settings.py`.
7. Results are written to `reports/allure-results`.

### 8.2 Execution Flow (Component Design)
```text
Feature File (.feature)
        |
        v
Test Loader (tests/test_*.py -> scenarios())
        |
        v
Step Definitions (steps/*.py)
        |
        v
Page Objects (pages/*.py)
        |
        v
Playwright Browser Context/Page (core/browser_manager.py + fixtures)
        |
        v
Application Under Test (OrangeHRM)
```

### 8.3 Fixture/Dependency Flow
```text
browser_manager (session)
    -> context (per test)
        -> page (per test)
            -> login_page / my_info_page / context_page / upload_page
```

## 9. Covered Test Areas
- Login validation
- My Info navigation visibility
- Personal details validations
- CRUD flows for My Info subsections
- Restricted/read-only section behavior
- Upload validations

## 10. Troubleshooting
### Browser executable missing
Run:
```powershell
python -m playwright install chromium
```

### Step definition not found
- Ensure `pytest-bdd` is installed.
- Ensure step phrase in `.feature` exactly matches step decorator in `steps/`.

### Invalid login / navigation timeouts
- Verify `.env` credentials are valid for your OrangeHRM instance.
- Keep `ORANGEHRM_BASE_URL` pointing to the correct environment.

<!-- ## 11. Maintenance Notes
- Keep feature text and step phrases in sync.
- Prefer stable selectors in page objects.
- Add new scenarios in `features/` first, then bind in `steps/`, then implement in `pages/`. -->
