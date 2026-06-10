# 🚀 AutoApply ATS Framework

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 Overview

Applying to dozens of jobs on enterprise Applicant Tracking Systems (ATS) is repetitive and time-consuming. **AutoApply** is a modular, Selenium-based automation framework designed to navigate complex, candidate-side job application workflows. 

Initially built as a proof-of-concept, this project is evolving into a comprehensive tool that handles dynamic navigation, multi-tab session management, and intelligent form-filling for platforms like SAP SuccessFactors.

## ✨ Key Features

* **Intelligent Form Filling:** Automatically populates standard text fields, dropdowns, and checkboxes based on a unified configuration profile.
* **Dynamic Workflow Navigation:** Handles multi-step application processes, including pagination and asynchronous loading states.
* **Modular Portal Architecture:** Built with scalability in mind. Platform-specific logic is isolated in portal modules, making it easy to support new ATS providers without rewriting core automation logic.
* **Multi-Tab Management:** Seamlessly switches contexts when ATS platforms open external authentication or document-signing windows.
* **Robust Error Handling & Logging:** Detailed execution logs to easily identify UI changes or blocked selectors.

## 🛠️ Tech Stack & Architecture

* **Core Automation:** Python, Selenium WebDriver
* **Browser Interfacing:** ChromeDriver
* **Architecture:** Page Object Model (POM)

### Directory Structure
```text
├── portals/       # Platform-specific automation scripts (e.g., successfactors.py)
├── utils/         # Helper functions (e.g., explicit waits, element locators)
├── logs/          # Execution logs and error screenshots
├── assets/        # Placeholder for test resumes and cover letters
├── config.json    # User profile and target job URLs
├── requirements.txt
└── main.py        # Framework entry point
