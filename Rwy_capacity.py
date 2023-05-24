import streamlit as st

def main():
    st.title("ENTREE")
    st.set_page_config(layout="wide")

    loi_options = ["ALEATOIRE", "AUTRE_OPTION"]
    typ_options = ["Type 1", "Type 2", "Type 3"]  # Remplacez par vos options réelles

    loi = st.selectbox("LOI", loi_options)
    typ = st.selectbox("Type", typ_options)
    proportion = st.slider("Proportion", 0, 100)

    # Ajoutez les autres éléments de l'interface utilisateur ici

if __name__ == "__main__":
    main()
