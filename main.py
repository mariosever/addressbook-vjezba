from flask import Flask, render_template, request, make_response, redirect, url_for
from models import Contact, db

app = Flask(__name__)
db.create_all()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/addnew", methods=["POST"])
def addnew():

    # uzimamo podatke iz forme
    name = request.form.get("name")
    address = request.form.get("address")
    phone = request.form.get("phone")
    email = request.form.get("email")

    # kreiramo objekt contact
    contact = Contact(name=name, address=address, phone=phone, email=email)

    # spremamo u bazu
    db.add(contact)
    db.commit()

    # response
    response = make_response(redirect(url_for("index")))

    return response


@app.route("/contacts")
def contacts():

    # uzmi sve kontakte iz baze
    all_contacts = db.query(Contact).all()

    return render_template("contacts.html", contacts=all_contacts)


if __name__ == "__main__":
    app.run()