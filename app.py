import yt_dlp
from flask import Flask, request, jsonify
from chord_extractor.extractors import Chordino
from flask_cors import CORS
import json
import os
import tempfile

app = Flask(__name__)
CORS(app)

def baixar_audio(url, output_filename):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
        'outtmpl': f'{output_filename}.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def obter_nome_video(url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        return info_dict.get('title', 'Unknown Title')

def extrair_acordes(arquivo_audio):
    chordino = Chordino()
    acordes = chordino.extract(arquivo_audio)
    acordes_resultado = [{'chord': acorde.chord, 'timestamp': acorde.timestamp} for acorde in acordes]
    return acordes_resultado

@app.route('/identificar-acordes', methods=['POST'])
def identificar_acordes():
    try:
        audio_filepath = None
        audio_filename = None

        if 'file' in request.files:
            arquivo = request.files['file']
            audio_filename = arquivo.filename
            with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_audio:
                audio_filepath = temp_audio.name
                arquivo.save(audio_filepath)

        elif 'url' in request.json:
            url = request.json['url']
            if not url:
                return jsonify({'error': 'Nenhuma URL fornecida'}), 400

            audio_filename = obter_nome_video(url)
            with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_audio:
                audio_filepath = temp_audio.name

            baixar_audio(url, audio_filepath.replace('.wav', ''))

        else:
            return jsonify({'error': 'Nenhum arquivo ou URL fornecido'}), 400

        if not os.path.exists(audio_filepath):
            return jsonify({'error': 'Arquivo de áudio não encontrado'}), 500

        acordes = extrair_acordes(audio_filepath)

        acordes_json = {
            'chords': acordes,
            'name': audio_filename
        }

        os.remove(audio_filepath)

        return jsonify(acordes_json)

    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro: {str(e)}'}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
