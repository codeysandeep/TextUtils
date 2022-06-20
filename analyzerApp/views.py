from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# View created for Landing page
def LandingPageView(request):
    buttons = [
        {
            "name": "remove_punctuations_btn",
            "label": "Remove Punctuations"
        },
        {
            "name": "uppercase_converter_btn",
            "label": "Uppercase Converter"
        },
        {
            "name": "extra_spaces_remover_btn",
            "label": "Extra Spaces Remover"
        },
        {
            "name": "numbers_remover_btn",
            "label": "Numbers Remover"
        },
        {
            "name": "blank_lines_remover_btn",
            "label": "Blank Lines Remover"
        }
    ]
    context = {"buttons": buttons}
    return render(request, "landing_page.html", context)


# View created for Analyzer
def AnalyzerView(request):
    remove_punctuations_btn = request.POST.get(
        "remove_punctuations_btn", "off")
    uppercase_converter_btn = request.POST.get(
        "uppercase_converter_btn", "off")
    extra_spaces_remover_btn = request.POST.get(
        "extra_spaces_remover_btn", "off")
    numbers_remover_btn = request.POST.get(
        "numbers_remover_btn", "off")
    blank_lines_remover_btn = request.POST.get(
        "blank_lines_remover_btn", "off")

    input_text = request.POST.get("input_text", "default")

    # =========== Code written for Remove punctuations button ===========
    if remove_punctuations_btn == "on":

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed_text = ""

        for char in input_text:
            if char not in punctuations:
                analyzed_text = analyzed_text + char

        input_text = analyzed_text
        context = {"analyzed_text": analyzed_text}

    # =========== Code written for Uppercase converter button ============
    if uppercase_converter_btn == "on":

        analyzed_text = ""
        for char in input_text:
            analyzed_text = analyzed_text + char.upper()

        input_text = analyzed_text
        context = {"analyzed_text": analyzed_text}

    # ============== Code written for Extra spaces remover button =========
    if extra_spaces_remover_btn == "on":

        analyzed_text = ""
        for index, char in enumerate(input_text):
            if not(input_text[index] == " " and input_text[index+1] == " "):
                analyzed_text = analyzed_text + char

        input_text = analyzed_text
        context = {"analyzed_text": analyzed_text}

    # ================ Code written for Numbers remover button ===============
    if numbers_remover_btn == "on":

        numbers = "0123456789"
        analyzed_text = ""

        for char in input_text:
            if char not in numbers:
                analyzed_text = analyzed_text + char

        input_text = analyzed_text
        context = {"analyzed_text": analyzed_text}

    # ============= Code written for Blank lines remover button ==============
    if blank_lines_remover_btn == "on":

        analyzed_text = ""
        lines = input_text.split("\n")
        non_empty_lines = [line for line in lines if line.strip() != ""]

        for line in non_empty_lines:
            analyzed_text += line + "\n"

        context = {"analyzed_text": analyzed_text}

    if remove_punctuations_btn != "on" and uppercase_converter_btn != "on" and extra_spaces_remover_btn != "on" and numbers_remover_btn != "on" and blank_lines_remover_btn != "on":
        messages.warning(
            request, "Please select any text utility before analyzing text!")
        return redirect('landing_page')

    messages.success(
        request, "Congratulations, your text has been analyzed successfully.")
    return render(request, "analyzed_text.html", context)


# View created for About page
def AboutMePageView(request):
    name = "Sandeep Ahirwar"
    address = "Jhansi"
    programming = "Python"
    skills = ["Java", "HTML( HyperText Markup Language )",
              "CSS( Cascading Style Sheets )", "VanillaJS", "ReactJS", "Django", "MySQL", "Heroku", "Firebase", "GitHub", "Microsoft Office"]
    graduation = {
        "degree": "B.Tech",
        "stream": "Computer Science and Engineering",
        "college": "SR Group of Institutions Jhansi"
    }
    context = {"name": name, "address": address,
               "programming": programming, "skills": skills, "graduation": graduation}
    return render(request, "aboutme_page.html", context)


# View created for Myskills page
def MyskillsPageView(request):
    images = [
        "https://img.icons8.com/color/50/000000/python--v1.png",
        "https://img.icons8.com/color/50/000000/java-coffee-cup-logo--v1.png",
        "https://img.icons8.com/color/50/000000/html-5--v1.png",
        "https://img.icons8.com/color/50/000000/css3.png",
        "https://img.icons8.com/color/50/000000/javascript--v1.png",
        "https://img.icons8.com/color/50/000000/django.png",
    ]
    context = {"images": images}
    return render(request, "myskills_page.html", context)


# View created for Mytools page
def MytoolsPageView(request):
    images = [
        "https://img.icons8.com/color/50/000000/ubuntu--v1.png",
        "https://img.icons8.com/ios-filled/50/000000/github.png",
        "https://img.icons8.com/color/50/000000/pycharm.png",
        "https://img.icons8.com/color/50/000000/visual-studio-code-2019.png",
    ]
    context = {"images": images}
    return render(request, "mytools_page.html", context)


# View created for Connectwithme page
def ConnectwithmePageView(request):
    connections = [
        {
            "link": "https://www.linkedin.com/in/codeysandeep/",
            "image": "https://img.icons8.com/color/50/000000/linkedin.png"
        },
        {
            "link": "https://github.com/codeysandeep",
            "image": "https://img.icons8.com/bubbles/50/000000/github.png"
        },
        {
            "link": "https://twitter.com/codeysandeep",
            "image": "https://img.icons8.com/color/50/000000/twitter--v1.png"
        },
        {
            "link": "https://www.facebook.com/sandeepmalothiya",
            "image": "https://img.icons8.com/color/50/000000/facebook.png"
        },
        {
            "link": "https://www.instagram.com/sandeepmalothiya/",
            "image": "https://img.icons8.com/fluency/50/000000/instagram-new.png"
        },
        {
            "link": "mailto:sandeepmalothiya@gmail.com",
            "image": "https://img.icons8.com/color/50/000000/gmail-new.png"
        }
    ]
    context = {"connections": connections}
    return render(request, "connectwithme_page.html", context)


# View created for Error page
def ErrorPageView(request):
    return render(request, "error_page.html")
