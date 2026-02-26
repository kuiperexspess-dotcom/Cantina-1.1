import streamlit as st
import pandas as pd
import os

# Configurazione
st.set_page_config(page_title="Giacenza Vini", layout="centered")

DB_FILE = 'inventario_vini.csv'

if not os.path.exists(DB_FILE):
    df = pd.DataFrame(columns=['Nome Vino', 'Uve e %', 'Regione', 'Prezzo', 'Giacenza'])
    df.to_csv(DB_FILE, index=False)

def carica_dati():
    return pd.read_csv(DB_FILE)

def salva_dati(df):
    df.to_csv(DB_FILE, index=False)

st.title("🍷 La Mia Cantina")

# --- AGGIUNGI VINO ---
with st.expander("➕ Aggiungi Nuovo Vino"):
    with st.form("nuovo_vino"):
        nome = st.text_input("Nome")
        uve = st.text_input("Uve e %")
        regione = st.text_input("Regione")
        prezzo = st.number_input("Prezzo (€)", min_value=0.0)
        quantita = st.number_input("Bottiglie", min_value=0, step=1)
        
        if st.form_submit_button("Salva in Inventario"):
            if nome:
                df = carica_dati()
                nuova_riga = pd.DataFrame([[nome, uve, regione, prezzo, quantita]], 
                                         columns=['Nome Vino', 'Uve e %', 'Regione', 'Prezzo', 'Giacenza'])
                df = pd.concat([df, nuova_riga], ignore_index=True)
                salva_dati(df)
                st.success("Salvato!")
                st.rerun()

# --- VENDITA ---
st.divider()
df = carica_dati()
if not df.empty:
    st.subheader("🛒 Registra Vendita")
    vino_sel = st.selectbox("Seleziona vino", df['Nome Vino'].tolist())
    qty_venduta = st.number_input("Quante vendute?", min_value=1, value=1)
    
    if st.button("Conferma Vendita"):
        idx = df.index[df['Nome Vino'] == vino_sel].tolist()[0]
        if df.at[idx, 'Giacenza'] >= qty_venduta:
            df.at[idx, 'Giacenza'] -= qty_venduta
            salva_dati(df)
            st.success("Giacenza aggiornata!")
            st.rerun()
        else:
            st.error("Scorte insufficienti!")

# --- TABELLA ---
st.divider()
st.subheader("📊 Giacenze Attuali")
st.dataframe(df, use_container_width=True)
