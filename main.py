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

def on_update_interval():
    generar_arbre()
game.on_update_interval(3000, on_update_interval)

# --- MENÚ DE TEXTO PARA SELECCIONAR---
def on_a_pressed():
    if jugador.overlaps_with(venedor):
        eleccio = game.ask_for_number("1:Gal 2:Pat 3:Cab 4:Ou 5:Cav 0:Sortir", 1)
        
        if 1 <= eleccio <= 5:
            processar_transaccio(eleccio - 1)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)
# -------------------------------------------------

def on_b_pressed():
    arbres = sprites.all_of_kind(KIND_ARBRE)
    tajat = False
    
    for arb in arbres:
        if jugador.overlaps_with(arb):
            scene.camera_shake(2, 200)
            arb.destroy(effects.disintegrate, 200)
            info.change_score_by(5)
            music.small_crash.play()
            jugador.say_text("+5kg", 500)
            tajat = True
            break
            
    if not tajat:
        jugador.say_text("No hi ha arbre!", 200)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_update():
    if abs(jugador.x - venedor.x) < 30 and abs(jugador.y - venedor.y) < 30:
        venedor.say_text("A: Mercat", 100)
    
    algun_aprop = False
    for arb in sprites.all_of_kind(KIND_ARBRE):
        if abs(jugador.x - arb.x) < 20 and abs(jugador.y - arb.y) < 20:
            algun_aprop = True
            break
    
    if algun_aprop:
        jugador.say_text("B: Talar", 100)
game.on_update(on_update)

# ANIMACIONES
def on_up(): animation.run_image_animation(jugador, assets.animation("nena-animation-up"), 200, False)
def on_down(): animation.run_image_animation(jugador, assets.animation("nena-animation-down"), 200, False)
def on_left(): animation.run_image_animation(jugador, assets.animation("nena-animation-left"), 200, False)
def on_right(): animation.run_image_animation(jugador, assets.animation("nena-animation-right"), 200, False)

controller.up.on_event(ControllerButtonEvent.PRESSED, on_up)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right)
