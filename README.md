# YouTube Video Downloader

Este é um simples projeto em Python utilizando a biblioteca **pytube** e **Tkinter** para criar uma interface gráfica que permite ao usuário baixar vídeos do YouTube diretamente para o seu computador ou dispositivo móvel.

## Funcionalidades

- Insira a URL de um vídeo do YouTube.
- O vídeo será baixado na resolução mais alta disponível.
- O script identifica o sistema operacional e salva o arquivo na pasta adequada:
  - **Windows**: Pasta de **Downloads**.
  - **Linux**: Pasta de **Downloads**.
  - **macOS/iOS**: Pasta de **Pictures** ou **Documents**.
  - **Android**: Pasta **DCIM/Camera** (pode variar dependendo do dispositivo).
- Interface gráfica simples com a biblioteca **Tkinter**.

## Requisitos

Antes de rodar o script, você precisa instalar o Python 3 e as bibliotecas necessárias. Execute o seguinte comando para instalar as dependências:

bash
pip install pytube
__________________________________________________________________________________________________________________________________


Como Usar?

1.Clone este repositório para o seu computador:
git clone https://github.com/bruno-moura-2804/youtube-downloader.git

__

2.Navegue até o diretório do projeto:

bash
cd youtube-downloader

__

3.Execute o script:

bash
python downloader.py

__

4.Na interface gráfica, cole a URL do vídeo do YouTube e clique no botão "Baixar Vídeo".
__

5.O vídeo será salvo automaticamente na pasta apropriada, dependendo do seu sistema operacional.
__

Exemplo de Saída
Após o download ser concluído, uma mensagem de sucesso será exibida, indicando o diretório onde o arquivo foi salvo.

Exemplo de mensagem de sucesso:

Download Completo!
Arquivo salvo em: C:/Users/seu-usuario/Downloads

__________________________________________________________________________________________________________________________________

Observações

- O script tenta identificar automaticamente o sistema operacional e salvar o vídeo na pasta de downloads padrão ou em pastas específicas de fotos ou vídeos.
  
- Para dispositivos móveis (Android/iOS), o caminho de download pode variar dependendo do dispositivo, e permissões extras podem ser necessárias.


__________________________________________________________________________________________________________________________________


This is a simple Python project using the **pytube** and **Tkinter** libraries to create a graphical interface that allows the user to download YouTube videos directly to their computer or mobile device.

## Features

- Enter the URL of a YouTube video.
- The video will be downloaded in the highest resolution available.
- The script identifies the operating system and saves the file in the appropriate folder:
- **Windows**: **Downloads** folder.
- **Linux**: **Downloads** folder.
- **macOS/iOS**: **Pictures** or **Documents** folder.
- **Android**: **DCIM/Camera** folder (may vary depending on the device).
- Simple graphical interface using the **Tkinter** library.

## Requirements

Before running the script, you need to install Python 3 and the necessary libraries. Run the following command to install the dependencies:

bash
pip install pytube
__________________________________________________________________________________________________________________

How to Use?

1. Clone this repository to your computer:
git clone https://github.com/bruno-moura-2804/youtube-downloader.git

__

2. Navigate to the project directory:

bash
cd youtube-downloader

__

3. Run the script:

bash
python downloader.py

__

4. In the graphical interface, paste the URL of the YouTube video and click the "Download Video" button.
__

5. The video will be automatically saved in the appropriate folder, depending on your operating system.
__

Example Output
After the download is complete, a success message will be displayed, indicating the directory where the file was saved.

Example Success Message:

Download Complete!
File saved in: C:/Users/your-username/Downloads

__________________________________________________________________________________________________________________________________

Notes

- The script tries to automatically identify the operating system and save the video in the default downloads folder or in specific photo or video folders.

- For mobile devices (Android/iOS), the download path may vary depending on the device, and extra permissions may be required.


