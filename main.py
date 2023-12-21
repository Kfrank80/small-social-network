# main.py

from flask import render_template, Flask
import connexion

from controllers.users import People

app = connexion.App(__name__, specification_dir="./")
app.add_api("social-network-swagger.yaml")


@app.route("/")
def home():
    people = People
    return render_template("home.html", people=people)


if __name__ == "__main__":
    app.run(host="localhost", port=8080)
