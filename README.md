# Invoice-Extraction-system-using-Gemini
Sure, here's a README.md file for your Streamlit application:

```markdown
# Invoice Information Extractor 🧑‍💻

Welcome to the Invoice Information Extractor application! This tool utilizes Gemini-Pro-Vision, a powerful generative AI model, to extract information from invoice images.


## Getting Started


### Prerequisites
- Python 3.x
- Streamlit
- Google Generative AI Library
- PIL (Python Imaging Library)
- dotenv

### Installation
1. Clone this repository to your local machine.
2. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and configure your Google API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

### Usage
1. Run the Streamlit application by executing the following command:
   ```
   streamlit run app.py
   ```
2. Enter the information you want to extract from the invoice in the chat input box.
3. Upload the image of your invoice by clicking on "Browse" in the sidebar and selecting the image file (supported formats: JPG, PNG, JPEG).
4. Wait for the application to process the information. The extracted details will be displayed in the app interface.

## File Structure
- `app.py`: Main Python script containing the Streamlit application code.
- `requirements.txt`: List of Python dependencies required by the application.
- `.env`: Configuration file for storing the Google API key.

## About
This application is powered by Gemini-Pro-Vision, a generative AI model developed by Google. It provides a convenient way to extract information from invoice images, making it useful for various business and administrative tasks.

## Feedback
We value your feedback! If you encounter any issues or have suggestions for improvement, please feel free to open an issue or reach out to us.

```

Feel free to customize this README.md file further to include additional details or instructions as needed!
