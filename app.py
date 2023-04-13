from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

photos = [
    {
        "id": 1,
        "title": "Sample Photo 1",
        "url": "https://via.placeholder.com/150/92c952",
    },
    {
        "id": 2,
        "title": "Sample Photo 2",
        "url": "https://via.placeholder.com/150/771796",
    },
]

@app.route("/")
def home():
    return "Welcome to my photo gallery!"

@app.route("/photos", methods=["GET"])
def get_photos():
    return jsonify(photos)

@app.route("/photos/<int:id>", methods=["GET"])
def get_photo_by_id(id):
    photo = next((photo for photo in photos if photo["id"] == id), None)
    if photo is None:
        return jsonify({"message": "Photo not found"}), 404
    return jsonify(photo)

@app.route("/photos", methods=["POST"])
def add_photo():
    title = request.json["title"]
    url = request.json["url"]
    new_photo = {"id": len(photos) + 1, "title": title, "url": url}
    photos.append(new_photo)
    return jsonify(new_photo), 201

@app.route("/photos/<int:id>", methods=["PUT"])
def update_photo(id):
    photo = next((photo for photo in photos if photo["id"] == id), None)
    if photo is None:
        return jsonify({"message": "Photo not found"}), 404

    title = request.json["title"]
    url = request.json["url"]
    photo.update({"title": title, "url": url})
    return jsonify(photo), 200

@app.route("/photos/<int:id>", methods=["DELETE"])
def delete_photo(id):
    photo_index = next((index for index, photo in enumerate(photos) if photo["id"] == id), None)
    if photo_index is None:
        return jsonify({"message": "Photo not found"}), 404

    del photos[photo_index]
    return jsonify({"message": "Photo deleted successfully"}), 200

if __name__ == "__main__":
    app.run(port=3002, debug=True)
