import pandas as pd
from fonction import download_process

def main():
    file_path = input("Enter the path of the file list url: ").strip()
    file_path = file_path.strip('"').strip("'")
    file_path = file_path.replace("\\", "/")
    
    try:
        df = pd.read_excel(file_path)
        if 'url' not in df.columns:
            print('La colonne "url" est manquante.')
            return
        for index, row in df.iterrows():
            channel_url = row['url']
            download_process(channel_url)
        print('Tous les traitements ont été effectués avec succès.')
    except Exception as e:
        print(f"Erreur lors du traitement de {file_path} : {str(e)}")
        print(e)

if __name__ == '__main__':
    main()
