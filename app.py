import streamlit as st
import os
import uuid
import shutil
import cv2
import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer, AutoConfig
import numpy as np
from ocr_utils import process_image

# Paths for uploads and results
UPLOAD_FOLDER = './uploads'
RESULTS_FOLDER = './results'

# Create directories if they don't exist
for folder in [UPLOAD_FOLDER, RESULTS_FOLDER]:
    os.makedirs(folder, exist_ok=True)

# Load model and tokenizer
model_name = 'ucaslcl/GOT-OCR2_0'
device = 'cuda' if torch.cuda.is_available() else 'cpu'

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModel.from_pretrained(model_name, trust_remote_code=True, low_cpu_mem_usage=True).to(device)
model.eval()

# Streamlit app layout
st.title('📝 GOT OCR Project')

task = st.selectbox(
    'Select OCR Task',
    ['Plain Text OCR', 'Format Text OCR', 'Fine-grained OCR (Box)', 'Fine-grained OCR (Color)', 'Multi-crop OCR', 'Render Formatted OCR']
)

uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

ocr_type = None
ocr_box = None
ocr_color = None

if task == "Fine-grained OCR (Box)":
    ocr_type = st.selectbox('OCR Type', ["ocr", "format"])
    ocr_box = st.text_input('Enter OCR Box Coordinates (x1, y1, x2, y2)', placeholder="[100,100,200,200]")
elif task == "Fine-grained OCR (Color)":
    ocr_type = st.selectbox('OCR Type', ["ocr", "format"])
    ocr_color = st.selectbox('Select OCR Color', ['red', 'green', 'blue'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button('Process OCR'):
        # Process the image
        unique_id = str(uuid.uuid4())
        image_path = os.path.join(UPLOAD_FOLDER, f"{unique_id}.png")
        image.save(image_path)

        result, html_content = process_image(model, tokenizer, image_path, task, ocr_type, ocr_box, ocr_color)

        if isinstance(result, str) and result.startswith("Error:"):
            st.error(result)
        else:
            st.subheader("OCR Result")
            st.text(result)
            
            if html_content:
                st.markdown(html_content, unsafe_allow_html=True)
                st.download_button("Download HTML Result", html_content, file_name=f"result_{unique_id}.html", mime="text/html")
