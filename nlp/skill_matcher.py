def extract_skills(text):
    skills = {
        "web development": ["html", "css", "javascript", "react", "flask" , "django" , "node.js"],
        "data analyst": ["sql", "excel", "power bi", "pandas" ,"numpy" , "matplotlib" , "tableau"],
        "machine learning": ["machine learning", "nlp", "tensorflow","machine learning", "deep learning", "artificial intelligence","nlp", "computer vision","scikit-learn", "tensorflow", "keras", "pytorch","mlops", "model deployment",],
        "java developer": ["java", "spring", "hibernate", "j2ee", "j2ee", "hibernate", "maven", "gradle", "microservices",  "oracle", "redis", "firebase"],
        "cloud": ["aws", "docker", "aws", "azure", "gcp","ec2", "s3", "lambda", "docker", "kubernetes","ci/cd", "jenkins", "terraform", "cloudformation"]
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
