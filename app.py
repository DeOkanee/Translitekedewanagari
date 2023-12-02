from flask import Flask, render_template, request, jsonify
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

app = Flask(__name__)

def ubah_ke_dewanagari(teks):
    teks_dewanagari = transliterate(teks, sanscript.ITRANS, sanscript.DEVANAGARI)
    return teks_dewanagari

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ubah_ke_dewanagari', methods=['POST'])
def ubah_ke_dewanagari_ajax():
    teks_input = request.form.get('teks_input', '')
    teks_dewanagari = ubah_ke_dewanagari(teks_input)
    return jsonify(teks_dewanagari)

if __name__ == '__main__':
    app.run(debug=True)
