# SauceDemo Test Automation

> End-to-end automated testing framework for the demo e-commerce website  
> [SauceDemo](https://www.saucedemo.com/)

---
## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Selene](https://img.shields.io/badge/Selene-0E5BBD?style=for-the-badge)
![Allure](https://img.shields.io/badge/Allure-FF4A36?style=for-the-badge)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=Jenkins&logoColor=white)
![Selenoid](https://img.shields.io/badge/Selenoid-0E5BBD?style=for-the-badge)
![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)
![TestOps](https://img.shields.io/badge/TestOps-2EA043?style=for-the-badge&logo=allure&logoColor=white)
![Jira](https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=jira&logoColor=white)

---

## 📋 Project Overview

Professional test automation framework featuring:

- **Page Object Model (POM)** for maintainable test structure
- **Allure reporting** with screenshots, videos, logs, and detailed steps
- **Selenoid cloud** test execution in isolated Docker containers
- **Jenkins CI/CD** integration for automated test execution and reporting
- **Telegram notifications** with test completion summaries
- **Allure TestOps** integration for test management
- **Jira integration** for defect tracking

---

## 🚀 Quick Start

### Installation
```bash
# 1. Clone repository
git clone https://github.com/Elias373/sauce_demo_ui_tests.git
cd sauce_demo_ui_tests

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

# 4. Install dependencies
pip install -r requirements.txt
```
### Environment Setup
Create a `.env` file in the project root with the following structure:

```env
# Application under test
BASE_URL=https://www.saucedemo.com
VALID_USERNAME=your_username
VALID_PASSWORD=your_password
INVALID_USERNAME=test_user
INVALID_PASSWORD=wrong_password

# Browser settings
WINDOW_WIDTH=1920
WINDOW_HEIGHT=1080
TIMEOUT=10.0
BROWSER_NAME=chrome
BROWSER_VERSION=128.0

# Selenoid configuration
SELENOID_LOGIN=your_selenoid_login
SELENOID_PASSWORD=your_selenoid_password
ENABLE_VNC=true
ENABLE_VIDEO=true
```

### Run Tests
```bash
# Run all tests
pytest tests/ --alluredir=allure-results -v

# Run a specific test
pytest tests/test_login.py::TestLogin::test_successful_login -v

# View Allure report
allure serve allure-results
```

---

## ✅ Test Coverage

### Authentication Module
| Test Case | Status | Description |
|-----------|--------|-------------|
| Successful Login | ✅ PASS | Valid credentials authentication |
| Failed Login | ✅ PASS | Invalid credentials error handling |
| Logout | ✅ PASS | User session termination |

### Shopping Cart Module
| Test Case | Status | Description |
|-----------|--------|-------------|
| Add Item to Cart | ✅ PASS | Product addition with counter verification |
| Remove Item from Cart | ✅ PASS | Product removal from cart |

### Navigation Module
| Test Case | Status | Description |
|-----------|--------|-------------|
| Menu Navigation | ✅ PASS | Side menu functionality |
| Product Filtering | ✅ PASS | Sort products by price |

#### Test Execution Demo:

![Text Example](readme_media/test_ex.gif)

---

## [Jenkins](https://jenkins.autotests.cloud/job/UI_DIPLOMA/) Build
![Jenkins Build](readme_media/jenkins_build.png)

---
### 📊 Report Examples

#### Allure Overview  
![Allure Report](readme_media/allure_overview.png)

#### Test Details
![Test Details](readme_media/test_details.png)

#### [TestOps](https://allure.autotests.cloud/project/5033/dashboards) Runs
![TestOps Runs](readme_media/testops_runs.png)

#### TestOps Test Cases
![TestOps Test Cases](readme_media/testops_details.png)

#### [Jira](https://jira.autotests.cloud/browse/HOMEWORK-1555) Integration
![Jira Integration](readme_media/jira_integration.png)


#### Telegram Notification
![Telegram](readme_media/telegram_notification.png)

## 👤 Author

**Illia Karcheuski**

[LinkedIn](https://pl.linkedin.com/in/ilyakorchevsky/ru)
