from app.services.gemini_client import gemini_client

class ScorerService:
    def calculate_scores(self, resume_data: dict, jd_data: dict, layout_analysis: str):
        prompt = f"""
        You are an expert ATS and HR AI. Evaluate the resume against the job description.
        
        Resume Data: {resume_data}
        Job Description: {jd_data}
        Layout Analysis: {layout_analysis}

        Compute the following scores (0-100) and provide detailed reasons:
        1. "ats_score": How well the resume parses and contains keywords.
        2. "jd_match_score": Semantic match between resume and JD.
        3. "skill_gap_score": 100 - (missing critical skills penalty). High score means low gap.
        4. "bias_score": 100 means NO bias. Lower score means potential bias detected (age, gender, origin markers).
        5. "layout_score": Based on the layout analysis (clarity, structure).

        Also provide:
        - "missing_skills": List of skills in JD but not in Resume.
        - "explanation": Detailed feedback for each score.
        - "market_demand_suggestions": Suggest 3-5 high-value skills to add based on current market trends for this role (use your internal knowledge).

        Return JSON.
        """
        
        return gemini_client.generate_json(prompt, model_type="flash")

scorer_service = ScorerService()
