import os
from fonction import download_process

def main():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "channel_url.txt")
    
    try:
        with open(file_path, 'r') as file:
            # Read all lines and remove empty lines and whitespace
            urls = [line.strip() for line in file.readlines() if line.strip()]
            
        if not urls:
            print('\n\n--- ERROR --- \n\nLe fichier channel_url.txt est vide.')
            return
            
        for url in urls:
            download_process(url)
            
        print('\n\n--- SUCCESS --- \n\n')
    except FileNotFoundError:
        print(f"\n\n--- ERROR --- \n\nLe fichier channel_url.txt n'a pas été trouvé dans le dossier du script.")
    except Exception as e:
        print(f"\n\n--- ERROR --- \n\nErreur lors du traitement de channel_url.txt : {str(e)}")
        print(e)

if __name__ == '__main__':
    main()
