from django.shortcuts import render



def portfolio(request):
    context = {
        "name": "Manish Basnet",
        "title": "Python & Data Science Student",
        "about": "I am an undergraduate student learning Data Science, Django, and Python.",
        "skills": ["Python", "Django", "Pandas", "NumPy", "FastAPI"],
        "projects": [
            {"name": "Sales Dashboard", "description": "Data analysis project", "link": "#"},
            {"name": "FastAPI App", "description": "Backend API project", "link": "#"},
        ],
        "email": "manishbasnet1@gmail.com",
        "github": "https://github.com/Enmessionate",
        "linkedin": "https://www.linkedin.com/in/manish-basnet-2b71a73a9",
    }

    return render(request, "home\index.html", context)
 