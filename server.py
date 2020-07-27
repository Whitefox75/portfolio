import os
import csv
from flask import Flask, render_template, request, send_from_directory, redirect

app = Flask(__name__)


# Definiert Template für Startseite
@app.route("/")
def start():
    return render_template("index.html")


# weist den jeweiligen html Seiten eine URL zu
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


# Favicon
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"), "desk_icon.ico",
                               mimetype='image/vnd.microsoft.icon')


# Daten aus Kontakformular als Textdatei
def write_to_file(data):
    with open("database.txt", mode="a") as database:
        fullname = data["fullname"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n {fullname} {email}, {subject}, {message}")


# Daten aus Kontakformular in csv Datei
def write_to_csv(data):
    with open("database.csv", newline="", mode="a") as database2:
        fullname = data["fullname"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([fullname, email, subject, message])


# Kontaktformular abfrage
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("/thank_you.html")
    else:
        return "something went wrong"
