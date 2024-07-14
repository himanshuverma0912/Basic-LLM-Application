## Gemini's Wisdom Well 🔮: A Text and Image Understanding Oracle

Welcome to Gemini's Wisdom Well, an AI-powered application that unlocks the power of Google's Gemini LLM to interpret both text and images! This Streamlit app offers two modes of interaction:

1. **Textual Q&A (app.py):**
   - Ask any question and receive insightful answers from Gemini.
   - Ideal for general knowledge queries, explanations, creative writing prompts, etc.

2. **Image Analysis (vision.py):**
   - Upload an image and get a description or analysis from Gemini.
   - Great for understanding the content of images, generating captions, or sparking creative ideas.


### Features

* **Multimodal Understanding:** Gemini can process both text and image inputs to provide comprehensive responses.
* **Instant Answers:** Receive quick and informative feedback from the AI model.
* **Interactive Interface:** Enjoy a user-friendly Streamlit web app for seamless interaction.
* **Customization:** Adapt the appearance and functionality of the app through CSS.

### Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Your Gemini API Key:**

   * Create a `.env` file in the project's root directory.
   * Add your Gemini API key to the `.env` file:
     ```
     GOOGLE_API_KEY=your_gemini_api_key_here
     ```

**Important Note:** You must obtain your own Gemini API key from Google and replace `your_gemini_api_key_here` with your actual key. The `.env` file is used to keep your API key secure and out of version control.

4. **Run the Desired Application:**

   * **Textual Q&A:**
     ```bash
     streamlit run app.py
     ```

   * **Image Analysis:**
     ```bash
     streamlit run vision.py
     ```

### How to Use

* **Textual Q&A:**
   1. Type your question into the text box.
   2. Click "Ask the question" to get Gemini's response.

* **Image Analysis:**
   1. Upload an image using the file uploader.
   2. Optionally, provide a text prompt to guide the analysis.
   3. Click "Tell me about the image" to get Gemini's description.

### Code Explanation

* **`app.py`:**  Script for the textual question-answering interface.
* **`vision.py`:** Script for the image analysis interface.
* **`.env`:** Stores your Google Gemini API key.
* **`requirements.txt`:** Lists the Python libraries required to run the app.

### Customization (Optional)

You can tailor the app's appearance using the CSS styles provided in the code.  Feel free to experiment with different colors, fonts, and layouts to personalize the experience.

### Contributing

Contributions are encouraged! If you have any ideas for new features, improvements, or bug fixes, please open an issue or submit a pull request.
