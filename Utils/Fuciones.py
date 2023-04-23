def extract_genre_name(genres):
    genre_list = []
    for genre in genres:
        genre_list.append(genre['name'])
    return genre_list
pelis["genres"] = pelis["genres"].apply(extract_genre_name)

def extract_genre_name(production_companies):
    nombre_productora = []
    for company in production_companies:
        nombre_productora.append(company["name"])
    return nombre_productora
pelis['production_companies'] = pelis['production_companies'].apply(extract_genre_name)


def extract_genre_name(production_countries):
    nombre_pais = []
    for company in production_countries:
        nombre_pais.append(company["name"])
    return nombre_pais
pelis["production_countries"] = pelis["production_countries"].apply(extract_genre_name)

def extract_genre_name(spoken_languages):
    nombre_pais = []
    for company in spoken_languages:
        nombre_pais.append(company["name"])
    return nombre_pais
pelis["spoken_languages"] = pelis["spoken_languages"].apply(extract_genre_name)

for col in ["Presupuesto","Recaudación","Puntuacion de los Criticos y Espectadores","Popularidad"]:
    fig, axs = plt.subplots(ncols=2, figsize=(10, 4))
    
    # Densidad
    sns.kdeplot(data=master_pelis, x=col, ax=axs[0])
    axs[0].set_title(f"Densidad de {col}")
    
    # QQ-plot
    stats.probplot(master_pelis[col], dist="norm", plot=axs[1])
    axs[1].set_title(f"QQ-plot de {col}")
    
    plt.tight_layout()
    plt.show()


for col in master_pelis.columns:
    if col in ["Presupuesto", "Recaudación", "Puntuacion de los Criticos y Espectadores", "Popularidad"]:
        fig, axs = plt.subplots(1, 2, figsize=(12,4))
