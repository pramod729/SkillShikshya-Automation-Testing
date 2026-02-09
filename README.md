# Selenium Automation Testing — SkillShikshya Website

## Project Overview

This repository contains automated UI test scripts using Selenium WebDriver and Pytest for the SkillShikshya website. The tests exercise common user flows to validate functionality and help with regression testing.

**Website tested:** https://skillshikshya.com

## Features Tested

### Course Search
- Navigate to the homepage
- Search for a course (e.g., "QA")
- Verify search results contain relevant keywords

### Enroll Form Submission
- Fill out the enrollment form with valid data
- Select options from dropdowns and radio buttons
- Submit the form and verify the success message

### User Registration
- Fill the registration form (name, email, password)
- Submit and verify confirmation or verification message

### User Login
- Enter registered email and password
- Submit login form
- Verify login success via dashboard presence or logout option

## Tools & Technologies
- Programming language: Python
- Automation tool: Selenium WebDriver
- Test framework: Pytest
- Web browser: Google Chrome (recommended)
- Driver management: `webdriver_manager` (for automatic ChromeDriver setup)

### Python libraries
- `selenium`
- `pytest`
- `webdriver-manager`

