from app.services.gemini_client import gemini_client

class ParserService:
    def parse_resume(self, text: str):
        prompt = f"""
        Extract structured data from the following resume text.
        Return a JSON object with:
        - "contact_info": {{ name, email, phone, linkedin, location }}
        - "skills": list of strings
        - "experience": list of objects {{ title, company, dates, description, achievements (list) }}
        - "education": list of objects {{ degree, school, dates }}
        - "projects": list of objects {{ title, description, tech_stack }}
        - "certifications": list of strings
        - "summary": string

        Resume Text:
        {text}
        """
        
        # We rely on Gemini's JSON mode
        return gemini_client.generate_json(prompt)

    def parse_job_description(self, jd_text: str):
        prompt = f"""
        Analyze this Job Description and extract:
        - "role_title": string
        - "required_skills": list of strings (must have)
        - "preferred_skills": list of strings (nice to have)
        - "experience_level": string
        - "key_responsibilities": list of strings
        - "domain_keywords": list of strings

        Job Description:
        {jd_text}
        """
        return gemini_client.generate_json(prompt)

parser_service = ParserService()
