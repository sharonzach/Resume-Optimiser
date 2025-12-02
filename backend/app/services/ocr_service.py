import fitz  # PyMuPDF
from PIL import Image
import io
from app.services.gemini_client import gemini_client

class OCRService:
    def pdf_to_images(self, pdf_bytes: bytes):
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        images = []
        for page in doc:
            pix = page.get_pixmap()
            img_data = pix.tobytes("png")
            images.append(Image.open(io.BytesIO(img_data)))
        return images

    def extract_text_and_layout(self, pdf_bytes: bytes):
        images = self.pdf_to_images(pdf_bytes)
        
        prompt = """
        Analyze this resume image. 
        1. Perform OCR to extract all text accurately.
        2. Identify the layout structure (columns, sections).
        3. Return the result as a JSON object with:
           - "full_text": The complete text content.
           - "layout_analysis": Description of columns, margins, and visual hierarchy.
           - "sections": A list of identified sections (e.g., "Experience", "Education") and their raw text content.
        """
        
        # We define a schema for strict output
        schema = {
            "type": "object",
            "properties": {
                "full_text": {"type": "string"},
                "layout_analysis": {"type": "string"},
                "sections": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string"},
                            "content": {"type": "string"}
                        }
                    }
                }
            }
        }

        return gemini_client.analyze_images(prompt, images, response_schema=schema)

ocr_service = OCRService()
