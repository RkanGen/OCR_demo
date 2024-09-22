# OCR_demo using GOT 2.0 from HF

![Capture1](https://github.com/user-attachments/assets/2a65c226-7c31-4662-b9e2-612c2faf209f)



This project uses the GOT-OCR2_0model from Hugging Face for performing various OCR (Optical Character Recognition) tasks on uploaded images. The interface is built using **Streamlit**, which provides a responsive and interactive experience for selecting OCR tasks and viewing results.

## Features

- **Plain Text OCR**: Extracts simple text from images.
- **Format Text OCR**: Extracts text with formatting.
- **Fine-grained OCR (Box)**: Extracts text within specific regions defined by bounding boxes.
- **Fine-grained OCR (Color)**: Extracts text based on selected color.
- **Multi-crop OCR**: Handles multiple crops for OCR extraction.
- **Render Formatted OCR**: Extracts and renders the text with the original document's layout.

## Setup

### Prerequisites

- Python 3.8+
- Install dependencies using `pip`.

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/RkanGen/OCR_demo.git
    cd OCR_demo
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:
    ```bash
    streamlit run app.py
    ```

4. Access the app in your browser at:
    - Local URL: `http://localhost:8501`
    - Network URL: Provided by Streamlit (shown after you run the app).

## Usage

1. Upload an image (PNG, JPG, or JPEG).
2. Select the desired OCR task from the dropdown.
3. Optionally, provide additional parameters like OCR box coordinates or color.
4. Click the **Process OCR** button.
5. View the extracted text and download the result (for formatted OCR tasks).

## Pinning a Model Revision (Optional)

To avoid downloading new versions of the model files every time you run the app, you can pin a specific revision. This will ensure the model code stays the same. Here's how:

1. Navigate to the model page on Hugging Face: [GOT-OCR2_0](https://huggingface.co/ucaslcl/GOT-OCR2_0)
2. Find a specific revision of the model that you trust.
3. In the `AutoModel` and `AutoTokenizer` lines in the `app.py` file, specify the revision:
   ```python
   tokenizer = AutoTokenizer.from_pretrained(model_name, revision="your-revision", trust_remote_code=True)
   model = AutoModel.from_pretrained(model_name, revision="your-revision", trust_remote_code=True).to(device)
   ```

## File Structure

```
got_ocr_project/
│
├── app.py                 # Main Streamlit app
├── ocr_utils.py           # OCR utilities for processing images
├── requirements.txt       # Python dependencies
├── uploads/               # Folder for uploaded images
└── results/               # Folder for OCR results
```

## Notes

- The project relies on the Hugging Face `ucaslcl/GOT-OCR2_0` model.
- Make sure to review any downloaded model code to ensure its security.

