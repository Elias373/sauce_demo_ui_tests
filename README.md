# SauceDemo Test Automation

> Automated UI testing for [SauceDemo](https://www.saucedemo.com/) - a demo e-commerce website

### 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Selene](https://img.shields.io/badge/Selene-0E5BBD?style=for-the-badge)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=Jenkins&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-FF4A36?style=for-the-badge)
![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)
![Selenoid](https://img.shields.io/badge/Selenoid-0E5BBD?style=for-the-badge)

### Setup

Before running tests, you need to configure environment variables:

1. Create `.env` file in the project root
2. Add your Selenoid credentials:
```bash
SELENOID_LOGIN=user1
SELENOID_PASSWORD=1234
SELENOID_URL=selenoid.autotests.cloud
```

*The .env file is included in .gitignore to prevent accidentally committing credentials.*

### Run Tests

```bash
# Run all tests with Allure reporting
pytest tests/ --alluredir=allure-results -v

# Run single test
pytest tests/simple_po.py::test_successful_login -v

# View Allure report
allure serve allure-results
```


## Test Coverage

### Authentication Module
✅ Successful Login - Valid credentials authentication  
✅ Failed Login - Invalid credentials error handling  
✅ Logout - User session termination

### Shopping Cart Module
✅ Add Item to Cart - Product addition with counter verification  
✅ Remove Item from Cart - Product removal from cart

### Navigation Module
✅ Menu Navigation - Side menu functionality  
✅ Product Filtering - Sort products by price

### Report Examples

#### Jenkins Build
![Jenkins Build](readme_media/jenkins_build.png)

#### Allure Overview  
![Allure Report](readme_media/allure_overview.png)

#### Test Details
![Test Details](readme_media/test_details.png)

#### Telegram Notification
![Telegram](readme_media/telegram_notification.png)

## 👤 Author

**Illia Karcheuski**

[GitHub](https://github.com/Elias373) • [LinkedIn](https://pl.linkedin.com/in/ilyakorchevsky/ru)
