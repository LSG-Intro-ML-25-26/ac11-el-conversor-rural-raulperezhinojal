# 🌲 El Conversor Rural - La Suerte de Monte

[![Work in MakeCode](https://classroom.github.com/assets/work-in-make-code-8824cc13a1a3f34ffcd245c82f0ae96fdae6b7d554b6539aec3a03a70825519c.svg)](https://classroom.github.com/online_ide?assignment_repo_id=22030624&assignment_repo_type=AssignmentRepo)

> Open this page at [https://raimonizard.github.io/makecode-arcade-template-nena-mov/](https://raimonizard.github.io/makecode-arcade-template-nena-mov/)

## 📖 Descripció del Projecte
Aquest videojoc és una eina interactiva basada en la tradició de "La suerte de monte" d'Alcubilla de Avellaneda. El jugador controla a la protagonista (Nena) que ha de gestionar el recurs de la llenya de pi.

L'objectiu és interactuar amb el mercader (NPC) per realitzar trueques (intercanvis) de productes rurals basats en una taula de conversió oficial. El joc permet tant **comprar** productes pagant llenya com **vendre** productes per obtenir llenya.

## 🎮 Com Jugar (Controls)
* **Fletxes de direcció:** Moure el personatge pel bosc.
* **Botó A:** Interactuar amb el Mercader (NPC) per obrir el menú de comerç.
* **Botó B:** Talar arbres propers per aconseguir llenya (+5kg).

## ✨ Funcionalitats Destacades (Retos Extra)
1.  **Conversió Bidireccional:** El sistema permet calcular el canvi en dues direccions:
    * *Opció 1:* Canviar Llenya -> Producte.
    * *Opció 2:* Canviar Producte -> Llenya.
2.  **Sistema de Validació (Smart Coding):** El codi impedeix errors lògics com introduir quantitats negatives o intentar intercanviar "mitja gallina" (decimals en animals).
3.  **Feedback Visual (GUI):**
    * Efecte de **confeti** 🎉 quan es tanca un tracte.
    * Efecte de **tremolor de càmera** (Camera Shake) quan es tala un arbre.
    * Sons interactius per a accions correctes o errors.
4.  **Mapa i NPCs:** Entorn gràfic amb parets, arbres i personatges no jugables.

## 📊 Taula de Conversió (Llenya de Pi)

| Producte | Icona | Cost en Llenya (Aprox) |
| :--- | :---: | :--- |
| **Gallina** | 🐔 | 6 kg / unitat |
| **Patates** | 🥔 | 1.33 kg llenya / kg patata |
| **Cabra** | 🐐 | 5 kg / unitat |
| **Ous** | 🥚 | 0.25 kg / unitat |
| **Cavall** | 🐎 | 12 kg / unitat |

## 📸 Evidències (Captures de Pantalla)

### 1. Menú Principal del Mercat
<img width="1900" height="772" alt="image" src="https://github.com/user-attachments/assets/ed23afea-fc7b-4252-97bd-9c45f06f43b8" />
> El menú mostra les opcions de productes disponibles.

### 2. Acció de Talar i Efectes
<img width="1916" height="814" alt="image" src="https://github.com/user-attachments/assets/5d6c91af-65d3-4238-bdb7-cfc0af964718" />

> Exemple de l'efecte visual en realitzar una acció.

---

## 🛠️ Instruccions Tècniques (MakeCode)

### Use as Extension

This repository can be added as an **extension** in MakeCode.

* open [https://arcade.makecode.com/](https://arcade.makecode.com/)
* click on **New Project**
* click on **Extensions** under the gearwheel menu
* search for **https://github.com/raimonizard/makecode-arcade-template-nena-mov** and import

### Edit this project

To edit this repository in MakeCode.

* open [https://arcade.makecode.com/](https://arcade.makecode.com/)
* click on **Import** then click on **Import URL**
* paste **https://github.com/raimonizard/makecode-arcade-template-nena-mov** and click import

#### Metadata (used for search, rendering)

* for PXT/arcade
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>
