from flask import Flask, render_template, request

app = Flask(__name__)

rules = {
    "suka_bernyanyi dan suka_bermain_musik dan memiliki_konsentrasi_dan_ingatan_yang_kuat dan mempunyai_fisik_yang_sehat": {
        "ekstrakurikuler": "Seni Musik",
        "presentation": "Ekstrakurikuler Seni Musik adalah kesempatan untuk mengeksplorasi bakat musikal Anda bersama teman-teman sekelas. Bergabunglah dalam latihan musik yang menyenangkan dan tampil di berbagai acara sekolah untuk menampilkan bakat vokal dan musik Anda",
    },
    "memiliki_konsentrasi_dan_ingatan_yang_kuat dan mempunyai_fisik_yang_sehat dan suka_menari dan suka_meniru_gerakan_tubuh dan suka_bekerja_sama_dalam_tim": {
        "ekstrakurikuler": "Seni Tari",
        "presentation": "Dalam ekstrakurikuler Seni Tari, Anda akan mempelajari gerakan-gerakan yang indah dan ekspresif, menggali berbagai jenis tarian dari budaya berbeda, dan berkolaborasi dengan teman-teman untuk menciptakan karya-karya yang memukau. Bergabunglah dengan kami untuk menggali keindahan seni melalui gerakan tubuh dan ekspresi emosi.",
    },
    "mempunyai_fisik_yang_sehat dan suka_bekerja_sama_dalam_tim dan menyukai_bela_diri dan memiliki_jiwa_pantang_menyerah dan mempunyai_mental_yang_kuat": {
        "ekstrakurikuler": "Pencak silat",
        "presentation": "Gabunglah dengan ekstrakurikuler Pencak Silat dan kembangkan kekuatan fisik, keterampilan bela diri, serta semangat kebersamaan melalui latihan intensif dan kompetisi yang menarik.",
    },
    "mempunyai_fisik_yang_sehat dan suka_bekerja_sama_dalam_tim dan memiliki_jiwa_pantang_menyerah dan mempunyai_mental_yang_kuat dan suka_bermain_futsal_atau_bola dan memiliki_karakter_disiplin dan mempunyai_berat_ideal": {
        "ekstrakurikuler": "Futsal",
        "presentation": "Ekstrakurikuler Futsal memberikan kesempatan untuk berlatih teknik olahraga dan kerjasama tim. Bersiaplah untuk terlibat dalam latihan intensif dan pertandingan seru bersama tim futsal sekolah!",
    },
    "mempunyai_fisik_yang_sehat dan suka_bekerja_sama_dalam_tim dan memiliki_jiwa_pantang_menyerah dan mempunyai_mental_yang_kuat dan memiliki_karakter_disiplin dan memiliki_jiwa_kejujuran dan tidak_mudah_takut_akan_alam_sekitar dan memiliki_jiwa_kepemimpinan dan memiliki_rasa_bertanggung_jawab": {
        "ekstrakurikuler": "Pramuka",
        "presentation": "Pramuka adalah kegiatan yang mengembangkan keterampilan survival, kepemimpinan, dan kebersamaan melalui petualangan alam terbuka, pelatihan keterampilan praktis, serta pengabdian kepada masyarakat. Bergabunglah dengan Pramuka untuk menjelajahi alam, belajar tentang keberanian, dan membangun karakter yang tangguh.",
    },
    "mempunyai_fisik_yang_sehat dan suka_bekerja_sama_dalam_tim dan memiliki_jiwa_pantang_menyerah dan mempunyai_mental_yang_kuat dan memiliki_karakter_disiplin dan mempunyai_tinggi_ideal dan mempunyai_postur_tegap dan mampu_melakukan_PBB": {
        "ekstrakurikuler": "Paskibra",
        "presentation": "Gabunglah dengan Paskibra untuk pengalaman unik dalam belajar kedisiplinan, kerjasama tim, dan pengembangan kepemimpinan melalui latihan disiplin militer, upacara bendera, dan berpartisipasi dalam acara-acara nasional yang menginspirasi.",
    },
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    facts = request.form.getlist("facts")
    derived_facts = infer_facts(facts)
    recommendations = calculate_recommendations(derived_facts)
    return render_template("result.html", recommendations=recommendations)


def infer_facts(facts):
    derived_facts = []
    for rule, _ in rules.items():
        conditions = rule.split(" dan ")
        if all(condition in facts for condition in conditions):
            derived_facts.append(rules[rule])
    return derived_facts


def calculate_recommendations(derived_facts):

    recommendations = []
    for fact in derived_facts:
        if fact not in recommendations:
            recommendations.append(fact)
    return recommendations


if __name__ == "__main__":
    app.run(debug=True)
