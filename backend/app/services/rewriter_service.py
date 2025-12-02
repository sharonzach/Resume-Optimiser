from app.services.gemini_client import gemini_client

class RewriterService:
    def generate_rewrites(self, resume_data: dict, jd_data: dict):
        prompt = f"""
        Rewrite the following resume to better match the job description.
        Generate 4 distinct versions:
        1. "ats_optimized": Focus on keywords, simple formatting, and clarity for machines.
        2. "hr_optimized": Focus on soft skills, culture fit, and readability for humans.
        3. "achievement_boosted": Quantify results, use strong action verbs, emphasize impact.
        4. "domain_specific": Use industry-specific jargon and deep technical framing.

        For each version, provide the full rewritten content (Markdown format).
        
        After generating, RERANK them from 1 (Best) to 4 (Least Best) based on overall effectiveness for getting an interview for this specific JD.
        
        Resume: {resume_data}
        JD: {jd_data}

        Return JSON:
        {{
            "versions": [
                {{ "type": "ats_optimized", "content": "...", "score_improvement_prediction": "..." }},
                ...
            ],
            "ranking": ["type1", "type2", "type3", "type4"]
        }}
        """
        
        return gemini_client.generate_json(prompt, model_type="flash")

rewriter_service = RewriterService()
