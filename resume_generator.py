import ollama
from datetime import datetime

def get_user_input():
    print(" CV Generator - Fill in your details\n" + "=" * 40)

    data = {
        "name": input("Full Name: ").strip(),
        "email": input("email: ").strip(),
        "phone": input("phone: ").strip(),
        "linkedin": input("LinkedIn (optional): ").strip() or None,
        "summary": input("Professional summary: ").strip(),

        "education": [],
        "experience": [],
        "skills": []
    }

    while True:
        print("\n Add Education (leave school blank to finish)")
        school = input("School name: ").strip()
        if not school: break

        data["education"].append({
            "school": school,
            "degree": input("Degree: ").strip(),
            "field": input("Field of Study: ").strip(),
            "year": input("Graduation Year: ").strip()
        })

    while True:
        print("\n Add Work Experience (leave job title blank to finish)")
        title = input("Job Title: ").strip()
        if not title: break

        data["experience"].append({
            "title": title,
            "company": input("Company: ").strip(),
            "start": input("Start Date(MM/YYYY): ").strip(),
            "end": input("End Date (MM/YYYY or 'Present'): ").strip(),
            "bullet_points": []
        })

        print(" Add 2-3 bullet points (leave blank to finish): ")
        while True:
            point = input(f" • ").strip()
            if not point: break
            data['experience'][-1]["bullet_points"].append(point)

    skills = input("\n Enter skills (comma-separated): ").strip()
    data["skills"] = [s.strip() for s in skills.split(",") if s.strip()]
    return data

def generate_resume(data):
    prompt = f"""
    Create a professional resume in Markdown format using this data:

    Name: {data['name']}
    Contact: {data['email']} | {data['phone']} {f"| LinkedIn: {data['linkedin']}" if data['linkedin'] else ""}
    Summary: {data['summary']}

    Education:
    {''.join(f"- {e['degree']} in {e['field']}, {e['school']} ({e['year']})\n" for e in data['education'])}

    Experience:
    {''.join(
        f"- **{exp['title']}** at {exp['company']} ({exp['start']} - {exp['end']})\n"
        + ''.join(f"  • {point}\n" for point in exp['bullet_points'])
        for exp in data['experience']
    )}

    Skills: {', '.join(data['skills'])}

    Format with clear sections, proper spacing, and professional tone."""

    response = ollama.generate(
        model="deepseek-r1:8b",
        prompt=prompt
    )
    return response['response']

def save_resume(content, filename=None):
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"resume_{timestamp}.md"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\n Resume saved as {filename}")

def main():
    data = get_user_input()
    print("\n Generating your resume......")

    resume = generate_resume(data)
    print("\n" + "=" * 40 + "\n")
    print(resume)

    if input("\nSave to file? (y/n): ").lower() == 'y':
        save_resume(resume)

if __name__ == '__main__':
    print("AI Resume Generator")
    main()
