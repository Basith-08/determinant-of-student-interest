from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

kriteria = {
    "B01": "Suka bernyanyi",
    "B02": "Suka bermain musik",
    "B03": "Memiliki konsentrasi dan ingatan yang kuat",
    "B04": "Mempunyai fisik yang sehat",
    "B05": "Suka menari",
    "B06": "Suka meniru gerakan tubuh",
    "B07": "Suka bekerja sama dalam tim",
    "B08": "Menyukai bela diri (pencak silat)",
    "B09": "Memiliki jiwa pantang menyerah",
    "B10": "Mempunyai mental yang kuat",
    "B11": "Suka bermain futsal atau bola",
    "B12": "Memiliki karakter disiplin",
    "B13": "Mempunyai berat ideal",
    "B14": "Memiliki jiwa kejujuran",
    "B15": "Tidak mudah takut akan alam sekitar",
    "B16": "Memiliki jiwa kepemimpinan",
    "B17": "Memiliki rasa bertanggung jawab",
    "B18": "Mempunyai tinggi ideal",
    "B19": "Mempunyai postur tegap",
    "B20": "Mampu melakukan PBB",
}

interests = [
    kriteria["B01"],
    kriteria["B02"],
    kriteria["B03"],
    kriteria["B04"],
    kriteria["B05"],
    kriteria["B06"],
    kriteria["B07"],
    kriteria["B08"],
    kriteria["B09"],
    kriteria["B10"],
    kriteria["B11"],
    kriteria["B12"],
    kriteria["B13"],
    kriteria["B14"],
    kriteria["B15"],
    kriteria["B16"],
    kriteria["B17"],
    kriteria["B18"],
    kriteria["B19"],
    kriteria["B20"],
]

extracurriculars = {
    "Seni musik": [
        kriteria["B01"],
        kriteria["B02"],
        kriteria["B03"],
        kriteria["B04"],
    ],
    "Seni tari": [
        kriteria["B03"],
        kriteria["B04"],
        kriteria["B05"],
        kriteria["B06"],
        kriteria["B07"],
    ],
    "Pencak Silat": [
        kriteria["B04"],
        kriteria["B07"],
        kriteria["B08"],
        kriteria["B09"],
        kriteria["B10"],
    ],
    "Futsal": [
        kriteria["B04"],
        kriteria["B07"],
        kriteria["B09"],
        kriteria["B10"],
        kriteria["B11"],
        kriteria["B12"],
        kriteria["B13"],
    ],
    "Pramuka": [
        kriteria["B04"],
        kriteria["B07"],
        kriteria["B09"],
        kriteria["B10"],
        kriteria["B12"],
        kriteria["B14"],
        kriteria["B15"],
        kriteria["B16"],
        kriteria["B17"],
    ],
    "Paskibra": [
        kriteria["B04"],
        kriteria["B07"],
        kriteria["B09"],
        kriteria["B10"],
        kriteria["B12"],
        kriteria["B18"],
        kriteria["B19"],
        kriteria["B20"],
    ],
}

selected_interests = []
current_interest_index = 0


def hitung_rekomendasi(selected_interests, extracurriculars):
    results = {}
    for extracurricular, interest_list in extracurriculars.items():
        match_count = sum(
            1 for interest in selected_interests if interest in interest_list
        )
        results[extracurricular] = (match_count / len(interest_list)) * 100
    return results


@app.route("/")
def index():
    return render_template("index.html", interest=interests[0])


@app.route("/submit", methods=["POST"])
def submit():
    global selected_interests, current_interest_index

    data = request.get_json()
    answer = data.get("answer")

    if answer == "yes":
        selected_interests.append(interests[current_interest_index])

    current_interest_index += 1

    if current_interest_index >= len(interests):
        results = hitung_rekomendasi(selected_interests, extracurriculars)
        selected_interests = []
        current_interest_index = 0
        return jsonify({"done": True, "results": results})

    return jsonify({"done": False, "interest": interests[current_interest_index]})


@app.route("/results", methods=["GET"])
def results():
    results = request.args.get("results")
    data = json.loads(results)
    return render_template("result.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
