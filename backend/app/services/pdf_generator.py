from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import io

class PDFService:
    def generate_report(self, scores: dict, rewrites: dict):
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter
        
        y = height - 50
        
        # Title
        c.setFont("Helvetica-Bold", 20)
        c.drawString(50, y, "Resume Optimization Report")
        y -= 40
        
        # Scores
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, "Scores:")
        y -= 20
        c.setFont("Helvetica", 12)
        
        score_data = scores.get("scores", {}) # Assuming structure from scorer
        # If scores is the direct dict
        if "ats_score" in scores:
             score_data = scores
        
        for key, value in score_data.items():
            if isinstance(value, (int, float, str)):
                c.drawString(70, y, f"{key.replace('_', ' ').title()}: {value}")
                y -= 20
        
        y -= 20
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, "Key Insights:")
        y -= 20
        c.setFont("Helvetica", 10)
        
        explanation = scores.get("explanation", "")
        if isinstance(explanation, dict):
             for k, v in explanation.items():
                text = f"{k}: {v}"
                # Simple text wrapping (very basic)
                if len(text) > 90:
                    c.drawString(70, y, text[:90] + "...")
                else:
                    c.drawString(70, y, text)
                y -= 15
        elif isinstance(explanation, str):
             c.drawString(70, y, explanation[:100])
             y -= 15

        # New Page for Rewrites
        c.showPage()
        y = height - 50
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, y, "Top Recommended Rewrite")
        y -= 30
        
        # Get top ranked
        ranking = rewrites.get("ranking", [])
        versions = rewrites.get("versions", [])
        
        top_version = next((v for v in versions if v["type"] == ranking[0]), versions[0] if versions else None)
        
        if top_version:
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, y, f"Type: {top_version['type']}")
            y -= 20
            c.setFont("Helvetica", 10)
            
            text = top_version.get("content", "")
            lines = text.split('\n')
            for line in lines:
                if y < 50:
                    c.showPage()
                    y = height - 50
                c.drawString(50, y, line[:100]) # Basic truncation
                y -= 12
                
        c.save()
        buffer.seek(0)
        return buffer.getvalue()

pdf_service = PDFService()
