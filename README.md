# Gemini-Pro-Powered-ATS-Tracker

This project is designed to provide a comprehensive tracking solution powered by Gemini Pro and leveraging Google AI services. Follow these steps to set up and run the application locally.

## Prerequisites

- Python (latest version recommended)
- Conda (for managing environments and packages)

## Setting Up the Environment

1. **Create a Conda Environment**: Open your terminal or Anaconda Prompt and navigate to the directory containing your project. Then, create a new Conda environment with the following command:

    '''bash conda create --name gemini_ats_env python=3.8

    Replace `python=3.8` with the latest Python version available at your time of setup.

2. **Activate the Environment**:

   On Windows:

   bash conda activate gemini_ats_env
   
   On macOS/Linux:

   bash source activate gemini_ats_env


3. **Install Dependencies**: Navigate to your project directory within the activated Conda environment and install the necessary Python packages listed in the `requirements.txt` file:

  bash pip install -r requirements.txt


4. **Install Poppler**: Poppler is used for PDF rendering. Install it via Conda:

  bash conda install -c conda-forge poppler


5. **Obtain API Key**: To use Google AI services, you need an API key. Visit [Google Cloud Console](https://console.cloud.google.com/), create a new project, enable the necessary APIs, and obtain your API key.

6. **Configure API Key**: Create a `.env` file in your project root directory and add your Google API key as follows:

  GOOGLE_API_KEY="your_api_key_here"


   Replace `"your_api_key_here"` with your actual Google API key.

## Running the Application

1. Ensure you are still in your project directory within the activated Conda environment.

2. Run the application using Streamlit:

  bash streamlit run app.py


This will start the Streamlit server and open the application in your default web browser.

## Contributing

Contributions to the Gemini-Pro-Powered-ATS-Tracker are welcome! Please feel free to submit pull requests or report issues through the GitHub repository associated with this project.





