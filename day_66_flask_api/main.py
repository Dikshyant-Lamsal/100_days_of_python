from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean


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


@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/random",methods=["GET"])
def fetch_random():
    cafe = db.session.query(Cafe)
    random_cafe = cafe.order_by(db.func.random()).first()
    cafe= {
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price
    }
    return jsonify(cafe=cafe)

@app.route("/all",methods=["GET"])
def fetch_all():
    cafes = db.session.query(Cafe).all()
    all_cafes = []
    for cafe in cafes:
        cafe_dict = {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price
        }
        all_cafes.append(cafe_dict)
    return jsonify(cafes=all_cafes)

@app.route('/search',methods=["GET"])
def fetch_cafe():
    location = request.args.get('loc')
    print(location)
    cafes = db.session.query(Cafe).filter_by(location=location)
    all_cafes = []
    for cafe in cafes:
        cafe_dict = {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price
        }
        all_cafes.append(cafe_dict)
    return jsonify(cafes=all_cafes)

@app.route("/add",methods={"POST"})
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=request.form.get("has_toilet"),
        has_wifi=request.form.get("has_wifi"),
        has_sockets=request.form.get("has_sockets"),
        can_take_calls=request.form.get("can_take_calls"),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(message="Cafe added successfully"), 201

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_cafe_price(cafe_id):
    cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
    if not cafe:
        return jsonify(error="Cafe not found"), 404
    new_price = request.form.get("coffee_price")
    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(message="Cafe price updated successfully"), 200

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key != "TopSecretAPIKey":
        return jsonify(error="Invalid API key"), 401
    cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
    if not cafe:
        return jsonify(error="Cafe not found"), 404
    db.session.delete(cafe)
    db.session.commit()
    return jsonify(message="Cafe reported as closed successfully"), 200


if __name__ == '__main__':
    app.run(debug=True)
