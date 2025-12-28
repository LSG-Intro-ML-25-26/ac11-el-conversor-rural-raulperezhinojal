import controller
import game
import scene
import sprites
import animation
import music
import info
from math import floor

# --- 1. CONFIGURACIÓ I TIPIFICACIÓ ---
KIND_ARBRE = SpriteKind.create()
KIND_NPC = SpriteKind.create()

# Dades del mercat
LLISTA_NOMS = ["Gallina", "Patates (kg)", "Cabra", "Ous", "Cavall"]
LLISTA_PREUS = [6, 1.33, 5, 0.25, 12]
ES_ANIMAL = [True, False, True, False, True]

# --- 2. LÒGICA DE MERCAT ---

def validar_operacio(index, quantitat):
    if quantitat <= 0:
        game.show_long_text("Error: La quantitat ha de ser positiva!", DialogLayout.BOTTOM)
        return False
    if ES_ANIMAL[index] and quantitat % 1 != 0:
        game.show_long_text("Error: Els animals han de ser enters!", DialogLayout.BOTTOM)
        return False
    return True

def processar_transaccio(index_prod):
    nom = LLISTA_NOMS[index_prod]
    preu = LLISTA_PREUS[index_prod]
    
    opcio = game.ask_for_number("1. COMPRAR (Pago llenya) 2. VENDRE (Guanyo llenya)", 1)
    
    if opcio == 1: # COMPRAR
        q = game.ask_for_number("Quantes unitats de " + nom + " vols?", 2)
        if validar_operacio(index_prod, q):
            cost = Math.round(q * preu * 100) / 100
            
            if info.score() >= cost:
                info.change_score_by(-cost)
                music.ba_ding.play()
                effects.confetti.start_screen_effect(500)
                game.splash("Tracte fet!", "Has pagat " + str(cost) + "kg llenya")
            else:
                music.wawawawaa.play()
                falta = Math.round((cost - info.score()) * 100) / 100
                game.splash("Error", "Et falten " + str(falta) + "kg de llenya")
                
    elif opcio == 2: # VENDRE
        q = game.ask_for_number("Quantes unitats tens de " + nom + "?", 2)
        if validar_operacio(index_prod, q):
            guany = Math.round(q * preu * 100) / 100
            info.change_score_by(guany)
            music.power_up.play()
            game.splash("Gràcies!", "Et dono " + str(guany) + "kg de llenya")

# --- 3. CONFIGURACIÓ DE L'ENTORN ---
jugador: Sprite = None
venedor: Sprite = None

def generar_arbre():
    if len(sprites.all_of_kind(KIND_ARBRE)) < 15:
        # Usa el nombre "miImagen" que tienes en assets para el árbol
        nou_arbre = sprites.create(assets.image("miImagen"), KIND_ARBRE)
        
        c = randint(1, 14)
        r = randint(1, 14)
        loc = tiles.get_tile_location(c, r)
        
        if not tiles.tile_at_location_is_wall(loc) and abs(c - 8) > 2:
            tiles.place_on_tile(nou_arbre, loc)
        else:
            nou_arbre.destroy()

def inicialitzar_entorn():
    global venedor, jugador
    
    # --- IMPORTANTE: Carga TU mapa desde Assets ---
    tiles.set_current_tilemap(assets.tilemap("""map"""))

    # VENEDOR (NPC)
    venedor = sprites.create(assets.image("miImagen2"), KIND_NPC)
    tiles.place_on_tile(venedor, tiles.get_tile_location(8, 7))
    
    # JUGADOR (Nena)
    jugador = sprites.create(assets.image("nena-front"), SpriteKind.Player)
    tiles.place_on_tile(jugador, tiles.get_tile_location(8, 10))
    scene.camera_follow_sprite(jugador)
    controller.move_sprite(jugador)
    
    info.set_score(0)
    
    for i in range(10):
        generar_arbre()

# --- 4. BUCLES I ESDEVENIMENTS ---

inicialitzar_entorn()