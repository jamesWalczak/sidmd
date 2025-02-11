#!/bin/bash
set -e  # Exit on error

#ensure pip is up to date
python -m pip install --upgrade pip

#required for Google Gemini AI
#pip install -q -U google-generativeai 

#required for ChatGPT AI
pip install -q openai
