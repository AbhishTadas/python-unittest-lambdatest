# Selenium Grid Testing Project

## Project Overview
This project contains automated test scripts for Selenium Grid testing. It includes:
- Test case implementations in Python
- Test case IDs documentation
- Gitpod configuration for development environment

## Prerequisites
- Python 3.x
- Selenium WebDriver
- Selenium Grid setup
- Chrome/Firefox drivers (if running locally)

## Project Structure
```
.
├── gitpod.yml          # Gitpod configuration
├── Readme.md           # Project documentation
├── testcase IDs.txt    # Test case identifiers
└── testcase.py         # Main test script
```

## Setup Instructions
1. Clone this repository
2. Install dependencies:
   ```bash
   pip install selenium
   ```
3. Configure Selenium Grid hub and nodes
4. Update testcase.py with your Grid URL:
   ```python
   grid_url = "http://your-grid-hub:4444/wd/hub"
   ```

## Running Tests
Execute the test script:
```bash
python testcase.py
```

## Test Case Documentation
Refer to `testcase IDs.txt` for test case identifiers and descriptions.

## Environment Variable
username = "abhsih.tadas"
access_key = "LT_zAgyqW37jYTe0AGJquInrTMv30f9kFfBotOgOtOGjfw4I3F"

## Gitpod Usage
This project includes Gitpod configuration for quick setup:
1. Open in Gitpod
2. The environment will automatically configure with required dependencies

## Contributing
1. Fork the repository
2. Create a new branch for your changes
3. Submit a pull request

## License
[MIT License](LICENSE) (add license file if needed)
