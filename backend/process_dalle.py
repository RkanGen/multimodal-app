from transformers import pipeline

def process_dalle(file_path):
    # Load the text prompt from the file
    with open(file_path, 'r') as f:
        prompt = f.read()
    dall_e = pipeline('text-to-image', model='CompVis/DALL-E')
    # Perform inference using the DALL-E model
    generated_image = dall_e(prompt)[0]['generated_image']  # Adjust based on actual output
    output_path = save_image(generated_image, "dalle_output.png")
    return output_path
