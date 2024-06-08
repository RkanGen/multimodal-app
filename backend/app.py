from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from PIL import Image
import torch
from transformers import pipeline

app = FastAPI()

# Allow CORS for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def save_image(image, filename):
    output_path = os.path.join(OUTPUT_FOLDER, filename)
    image.save(output_path)
    return output_path

# Placeholder function for StyleGAN3
def process_stylegan3(file_path):
    # Load and preprocess the input image
    image = Image.open(file_path)
    # Perform inference using the StyleGAN3 model
    # This is a placeholder; replace with actual StyleGAN3 inference
    processed_image = image  # Replace with actual processing code
    output_path = save_image(processed_image, "stylegan3_output.png")
    return output_path

# Placeholder function for SDXL
def process_sdxl(file_path):
    # Load and preprocess the input image
    image = Image.open(file_path)
    # Perform inference using the SDXL model
    # This is a placeholder; replace with actual SDXL inference
    processed_image = image  # Replace with actual processing code
    output_path = save_image(processed_image, "sdxl_output.png")
    return output_path

# Example integration for DALL-E using Hugging Face Transformers
def process_dalle(file_path):
    # Load the text prompt from the file
    with open(file_path, 'r') as f:
        prompt = f.read()
    dall_e = pipeline('text-to-image', model='dalle-mini/dalle-mini')
    # Perform inference using the DALL-E model
    generated_image = dall_e(prompt)[0]  # Replace with actual inference code
    output_path = save_image(generated_image, "dalle_output.png")
    return output_path

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), model: str = Form(...)):
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    if model == "stylegan3":
        result = process_stylegan3(file_location)
    elif model == "sdxl":
        result = process_sdxl(file_location)
    elif model == "dall-e":
        result = process_dalle(file_location)
    else:
        return JSONResponse(content={"error": "Unknown model"}, status_code=400)

    return JSONResponse(content={"result": result})

@app.get("/output/{filename}")
async def get_output(filename: str):
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return JSONResponse(content={"error": "File not found"}, status_code=404)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
