
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import folium
from folium import raster_layers
import rasterio
from io import BytesIO
from PIL import Image
from streamlit_folium import st_folium

# Fonction pour générer des données fictives
def generate_fake_data():
    years = [2025, 2026, 2027, 2028, 2029, 2030]
    tree_coverage = np.random.randint(1000, 5000, size=6)
    co2_sequestration = np.random.randint(5000, 15000, size=6)
    return pd.DataFrame({'Year': years, 'Tree Coverage': tree_coverage, 'CO2 Sequestration (tons)': co2_sequestration})

# Création des données fictives
df = generate_fake_data()

# Fonction pour afficher le tableau de bord
def dashboard():
    st.title("Dashboard: Suivi de la Réforestation")

    # Partie KPIs
    st.markdown("### KPIs Mensuels")
    total_trees = np.random.randint(100000000, 130000000)
    co2_sequestered = np.random.randint(8000, 15000)
    st.metric("Total d'Arbres Plantés", f"{total_trees:,}", delta=f"{np.random.randint(5, 20)}% increase")
    st.metric("CO2 Séquestré", f"{co2_sequestered:,} tons", delta=f"{np.random.randint(10, 20)}% increase")
    
    # Graphiques des prévisions
    st.markdown("### Prévisions de Couverture Végétale")
    fig = px.line(df, x='Year', y='Tree Coverage', title="Prévision de couverture végétale")
    st.plotly_chart(fig)
    
    # Indice de biodiversité
    biodiversity_index = round(np.random.uniform(6.5, 8.5), 1)
    st.markdown("### Indice de Biodiversité")
    st.write(f"Biodiversity Index: {biodiversity_index} (12% improvement since 2024)")

# Page carte (peut-être une image pour maintenant)
def map_page():
    st.title("Carte des Zones")
    st.markdown("Affiche la carte de la zone ici.")
    # Pour la maquette, nous pouvons afficher une image comme carte de fond
    st.image("assets/placeholder_map.jpg", caption="Carte simulée")

# Fonction pour afficher la barre latérale et naviguer
def main():
    st.sidebar.title("Navigation")
    pages = {
        "Dashboard": dashboard,
        "Carte des Zones": map_page
    }

    selection = st.sidebar.radio("Sélectionner une page", list(pages.keys()))
    pages[selection]()

main()
