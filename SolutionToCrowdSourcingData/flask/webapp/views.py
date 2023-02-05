from flask import Blueprint, render_template, request, flash, redirect, url_for
views = Blueprint('views', __name__)

# import sys 
# sys.path.append('../../scraper')
# import os
# os.path.dirname()
# from scraper import htmlCreate

# from scraper.htmlCreate import createHtml
# from ..scraper import htmlCreate

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email-addr')
            social = request.form.get('social-handle')
            phone = request.form.get('phone-number')
            print(name,email,social,phone)
            # htmlCreate.downloader(socials
            return redirect(url_for('views.end'))
        except:
            print("Error Occurred")
    else:
        pass
    return render_template("input.html")

@views.route('/tata')
def end():
    return render_template('end.html')