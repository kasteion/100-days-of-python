from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.sql.expression import func, select

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

# HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    cafe = db.session.execute(db.select(Cafe).order_by(func.random()).limit(1)).scalar()
    # print(cafe.id)
    # print(cafe.__dict__)
    # return jsonify(id = cafe.id, name = cafe.name )
    cafe_dict = cafe.__dict__
    del cafe_dict["_sa_instance_state"]
    return jsonify(cafe_dict)

@app.route("/all")
def all_cafes():
    cafes = [{ k: cafe.__dict__[k] for k in cafe.__dict__ if k != '_sa_instance_state'} for cafe in db.session.execute(db.select(Cafe)).scalars().all()]
    return jsonify({ "cafes": cafes })

@app.route("/search")
def search_cafes():
    loc = request.args.get('loc')
    cafes = [{ k: cafe.__dict__[k] for k in cafe.__dict__ if k != '_sa_instance_state'} for cafe in db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()]

    if len(cafes) == 0:
        return jsonify({ "error": {
            "Not Found": "Sorry, we don't have a cafe at that location"
        }}), 404
    
    return jsonify({ "cafes": cafes })

# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add_cafe():
    # print(request.form.keys())
    # print(request.form.to_dict())
    # print(request.form.get('name'))
    form = request.form
    cafe = Cafe(
        name = form.get('name'),
        map_url = form.get('map_url'),
        img_url = form.get('img_url'),
        location = form.get('location'),
        seats = form.get('seats'),
        has_toilet = bool(form.get('has_toilet')),
        has_wifi = bool(form.get('has_wifi')),
        has_sockets = bool(form.get('has_sockets')),
        can_take_calls = bool(form.get('can_take_calls')),
        coffee_price = form.get('coffee_price')
    )
    db.session.add(cafe)
    db.session.commit()
    return jsonify(esponse={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<id>', methods=['PATCH'])
def update_coffee_price(id):
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == id)).scalar()
    if not cafe:
        return jsonify({ "error": { "Not Found": "Sorry a cafe with that id was not found in the database."}}), 404
    new_price = request.args.get("new_price")
    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify({ "success": "Successfully updated the price" })

# HTTP DELETE - Delete Record
@app.route('/report-closed/<id>', methods=['DELETE'])
def report_closed(id):
    api_key = request.args.get("api-key")
    if api_key != 'TopSecretAPIKey':
        return jsonify({ "error": "Sorry, that's not allowed. Make sure you have the correct api_key"}), 403
    
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == id)).scalar()
    if not cafe:
        return jsonify({ "error": { "Not Found": "Sorry a cafe with that id was not found in the database."}}), 404
    
    db.session.delete(cafe)
    db.session.commit()

    return jsonify({ "success": "Successfully deleted the cafe" })


if __name__ == '__main__':
    app.run(debug=True)
