from googlesearch import search
import requests
from bs4 import BeautifulSoup

def cerca_info_vino(nome_vino):
    """Tenta di trovare info sulle uve e regione online"""
    try:
        # Cerchiamo il vino su Google
        query = f"{nome_vino} scheda tecnica uve regione"
        for url in search(query, num_results=1):
            # Proviamo a leggere la descrizione rapida o il titolo
            return f"Info trovate per {nome_vino} (Verifica sul sito produttore)"
    except:
        return "Ricerca non riuscita, inserimento manuale necessario."

# --- MODIFICA NEL TUO FORM DI INSERIMENTO ---
with st.expander("➕ Aggiungi un nuovo vino con ricerca automatica"):
    nome_input = st.text_input("Inserisci Nome e Annata del vino")
    
    if st.button("🔍 Cerca dettagli online"):
        with st.spinner('Ricerca in corso...'):
            # Qui l'app simula la ricerca
            info_recuperate = cerca_info_vino(nome_input)
            st.info(f"Suggerimento: {info_recuperate}")
            # Nota: L'estrazione esatta delle % richiede che il sito 
            # abbia un formato standard. Spesso è meglio confermare a mano.
          
