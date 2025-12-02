import google.generativeai as genai
from app.core.config import settings
import json
import typing_extensions

# Configure the SDK
genai.configure(api_key=settings.GOOGLE_API_KEY)

class GeminiClient:
    def __init__(self):
        # Using latest aliases from the list
        self.model_flash = genai.GenerativeModel('gemini-flash-latest')
        self.model_pro = genai.GenerativeModel('gemini-pro-latest')

    def generate_text(self, prompt: str, model_type="flash") -> str:
        model = self.model_pro if model_type == "pro" else self.model_flash
        response = model.generate_content(prompt)
        return response.text

    def generate_json(self, prompt: str, response_schema=None, model_type="flash"):
        model = self.model_pro if model_type == "pro" else self.model_flash
        
        generation_config = genai.GenerationConfig(
            response_mime_type="application/json",
            response_schema=response_schema
        )
        
        response = model.generate_content(prompt, generation_config=generation_config)
        try:
            return json.loads(response.text)
        except json.JSONDecodeError:
            # Fallback if JSON parsing fails (rare with response_mime_type)
            return {"error": "Failed to parse JSON", "raw": response.text}

    def analyze_images(self, prompt: str, images: list, response_schema=None):
        """
        images: List of PIL Image objects or image bytes
        """
        model = self.model_flash # Flash is great for vision
        
        content = [prompt] + images
        
        generation_config = None
        if response_schema:
            generation_config = genai.GenerationConfig(
                response_mime_type="application/json",
                response_schema=response_schema
            )

        response = model.generate_content(content, generation_config=generation_config)
        
        if response_schema:
             try:
                return json.loads(response.text)
             except:
                return response.text
        return response.text

gemini_client = GeminiClient()
