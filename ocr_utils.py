import os
import shutil
import uuid
import cv2
from PIL import Image

def process_image(model, tokenizer, image_path, task, ocr_type=None, ocr_box=None, ocr_color=None):
    try:
        result_path = f"./results/{uuid.uuid4()}.html"
        
        if task == "Plain Text OCR":
            res = model.chat(tokenizer, image_path, ocr_type='ocr')
            return res, None

        if task == "Format Text OCR":
            res = model.chat(tokenizer, image_path, ocr_type='format', render=True, save_render_file=result_path)
        elif task == "Fine-grained OCR (Box)":
            res = model.chat(tokenizer, image_path, ocr_type=ocr_type, ocr_box=ocr_box, render=True, save_render_file=result_path)
        elif task == "Fine-grained OCR (Color)":
            res = model.chat(tokenizer, image_path, ocr_type=ocr_type, ocr_color=ocr_color, render=True, save_render_file=result_path)
        elif task == "Multi-crop OCR":
            res = model.chat_crop(tokenizer, image_path, ocr_type='format', render=True, save_render_file=result_path)
        elif task == "Render Formatted OCR":
            res = model.chat(tokenizer, image_path, ocr_type='format', render=True, save_render_file=result_path)
        
        if os.path.exists(result_path):
            with open(result_path, 'r') as f:
                html_content = f.read()
            return res, html_content
        return res, None
    except Exception as e:
        return f"Error: {str(e)}", None
    finally:
        if os.path.exists(image_path):
            os.remove(image_path)
