# ATS Job Application Automation Framework

## Overview

A Selenium-based automation framework for automating candidate-side job application workflows on enterprise ATS platforms such as SAP SuccessFactors.

## Features

- Automated job application workflow
- Dynamic ATS navigation
- Multi-tab handling
- Form auto-fill
- Resume and cover letter workflow support
- Dropdown and checkbox handling
- Modular portal architecture

## Tech Stack

- Python
- Selenium
- ChromeDriver

## Supported Platforms

- Capgemini Careers (SAP SuccessFactors)

## Project Structure

- portals/
- utils/
- logs/
- assets/

## Current Limitations

Some ATS upload widgets use proprietary JavaScript-based upload handlers requiring platform-specific integrations.

## Future Improvements

- Multi-platform ATS support
- AI-based job matching
- Dashboard integration
- Async automation workflows

## Run Project

```bash
pip install -r requirements.txt
python main.py