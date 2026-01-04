def extract_skills(text):
    skills = {
        "web development": ["html", "css", "javascript", "react", "flask"],
        "data analyst": ["sql", "excel", "power bi", "pandas"],
        "machine learning": ["machine learning", "nlp", "tensorflow"],
        "java developer": ["java", "spring", "hibernate"],
        "cloud": ["aws", "docker"]
    }

    text = text.lower()
    result = {}

    for role, skill_list in skills.items():
        found = []
        for skill in skill_list:
            if skill in text:
                found.append(skill)
        if found:
            result[role] = found

    return result
