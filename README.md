
# ChordinoAPI

Este é uma API simples para a extração de acordes feita com Python.

## Como funciona

Esse código implementa uma API em Flask para identificar acordes de um arquivo de áudio ou de um vídeo fornecido via URL do YouTube.

### Dependências

O código utiliza as bibliotecas [yt_dlp](https://documenter.getpostman.com/view/32180238/2sAYQXnCcv) para baixar vídeos do YouTube, [chord_extractor](https://documenter.getpostman.com/view/32180238/2sAYQXnCcv) para extrair acordes, e `flask` para criar a API.

### Funções principais:

- **baixar_audio(url, output_filename)**: Baixa o áudio de um vídeo do YouTube na melhor qualidade disponível, convertendo-o para o formato WAV.
- **obter_nome_video(url)**: Obtém o título de um vídeo do YouTube sem baixá-lo, utilizando a URL fornecida.
- **extrair_acordes(arquivo_audio)**: Utiliza a `chord_extractor` para extrair os acordes de um arquivo de áudio, retornando os acordes com seus respectivos timestamps. Além disso, foi utilizado `Tempfile` para lidar de forma eficiente com arquivos temporários durante o processamento.

## 🚀 Começando

Siga as instruções abaixo para executar a API.

## 📋 Pré-requisitos

- Python 3.8
- Gerenciador de pacotes pip ou conda

## 🔧 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/JeanRauta/chordinoAPI.git
   cd chordinoAPI
   ```

2. Instale as dependências:
   - Se estiver usando o pip:
     ```bash
     pip install -r requirements.txt
     ```
   - Se estiver usando o conda:
     ```bash
     conda env create -f environment.yml
     ```

3. Baixe o ffmpeg:
   - Para instalar o ffmpeg no Windows, será necessário baixá-lo a partir deste [link](https://github.com/yt-dlp/FFmpeg-Builds) e adicioná-lo ao PATH do Windows.
   - No Linux, basta utilizar o seguinte comando:
     ```bash
     sudo apt install ffmpeg
     ```
   - Ou você pode baixar pelo conda utilizando o comando:
     ```bash
     conda install ffmpeg
     ```

## 📦 Executando

- Para executar em modo de desenvolvimento, use o comando:
  ```bash
  flask run
  ```
- Para executar em modo de produção, use o comando:
  ```bash
  gunicorn -c gunicorn_config.py app:app
  ```

## 📂 Estrutura do Projeto

- `app.py` - Script da API
- `gunicorn_config.py` - Script de configurações do servidor WSGI
- `requirements.txt` - Arquivo utilizado para baixar as dependências da API pelo pip
- `environment.yml` - Arquivo utilizado para construir o ambiente virtual conda com todas as dependências do projeto

## 🤝 Interações com a API

### Endpoints

#### POST /identificar-acordes

Este endpoint permite identificar os acordes de um arquivo de áudio ou vídeo a partir de uma URL. A resposta retorna os acordes extraídos com seus respectivos timestamps.

Este endpoint possui duas formas de corpo:

1. **File request**: Envie um arquivo de áudio para identificar os acordes presentes nele.
   - Exemplo:
     ```bash
     curl --location -g '{{URLbase}}/identificar-acordes' --form 'file=@"./teste.mp3"'
     ```

2. **URL request**: Envie uma URL de vídeo de plataformas como YouTube para extrair o áudio e identificar os acordes.
   - Exemplo:
     ```bash
     curl --location -g '{{URLbase}}/identificar-acordes' --data '{
         "url": "https://youtu.be/kivUsDGWojU?si=WWELyp_ch5qN8ZF2"
     }'
     ```

### Resultado da API

```json
{
  "chords": [
    {
      "chord": "N",
      "timestamp": 0.371519274
    },
    {
      "chord": "G",
      "timestamp": 1.114557823
    },
    {
      "chord": "C6",
      "timestamp": 2.285351473
    },
    {
      "chord": "N",
      "timestamp": 3.86430839
    }
  ],
  "name": "teste.mp3"
}
```

Para mais informações, acesse a [documentação do Postman](https://documenter.getpostman.com/view/32180238/2sAYQXnCcv).

## 📜 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.

---

Feito por Jean Rauta
