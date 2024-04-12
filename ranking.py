import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

df = pd.read_csv('dados.csv', usecols=['DESCR_OCORRENCIA_VEICULO', 'DESCR_TIPO_VEICULO', 'DESCR_MARCA_VEICULO'], encoding='latin1')

dados_filtrados = df[(df['DESCR_OCORRENCIA_VEICULO'] == 'Roubado') & (df['DESCR_TIPO_VEICULO'] == 'Automovel')]


ranking = dados_filtrados['DESCR_MARCA_VEICULO'].value_counts().reset_index()
ranking.columns = ['MARCA_VEICULO', 'QUANTIDADE ROUBADA']
ranking['POSICAO'] = ranking.index + 1

@app.route('/', methods=['GET'])
def get_ranking_carros_roubados():
    ranking_json = ranking.to_dict(orient='records')
    return jsonify(ranking_json)

if __name__ == '__main__':
    app.run(debug=True)
