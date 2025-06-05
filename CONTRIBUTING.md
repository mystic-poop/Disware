# Contributing to Disware

Thank you for your interest in contributing to Disware! This guide will help you get started with the project.

## Before You Start
1. **Read our [Code of Conduct](CODE_OF_CONDUCT.md)**  
   All contributors must adhere to our community standards.
2. **Check existing issues**  
   Search [open issues](https://github.com/mystic-poop/Disware/issues) to avoid duplicates.
3. **Discuss feature requests**  
   Open an issue for discussion before working on major changes.

## Setup Development Environment
### Prerequisites
- Python 3.10+ (recommended)
- pip (latest version)
- Git
- discord.py

### Installation
```bash
# Fork & clone the repository
git clone https://github.com/YOUR_USERNAME/Disware.git
cd Disware

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -m disware --version
