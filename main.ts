//  --- 1. CONFIGURACIÓ I TIPIFICACIÓ ---
let KIND_ARBRE = SpriteKind.create()
let KIND_NPC = SpriteKind.create()
//  Dades del mercat
let LLISTA_NOMS = ["Gallina", "Patates (kg)", "Cabra", "Ous", "Cavall"]
let LLISTA_PREUS = [6, 1.33, 5, 0.25, 12]
let ES_ANIMAL = [true, false, true, false, true]
//  --- 2. LÒGICA DE MERCAT ---
function validar_operacio(index: number, quantitat: number): boolean {
    if (quantitat <= 0) {
        game.showLongText("Error: La quantitat ha de ser positiva!", DialogLayout.Bottom)
        return false
    }
    
    if (ES_ANIMAL[index] && quantitat % 1 != 0) {
        game.showLongText("Error: Els animals han de ser enters!", DialogLayout.Bottom)
        return false
    }
    
    return true
}

function processar_transaccio(index_prod: number) {
    let q: number;
    let cost: number;
    let falta: number;
    let guany: number;
    let nom = LLISTA_NOMS[index_prod]
    let preu = LLISTA_PREUS[index_prod]
    let opcio = game.askForNumber("1. COMPRAR (Pago llenya) 2. VENDRE (Guanyo llenya)", 1)
    if (opcio == 1) {
        //  COMPRAR
        q = game.askForNumber("Quantes unitats de " + nom + " vols?", 2)
        if (validar_operacio(index_prod, q)) {
            cost = Math.round(q * preu * 100) / 100
            if (info.score() >= cost) {
                info.changeScoreBy(-cost)
                music.baDing.play()
                effects.confetti.startScreenEffect(500)
                game.splash("Tracte fet!", "Has pagat " + ("" + cost) + "kg llenya")
            } else {
                music.wawawawaa.play()
                falta = Math.round((cost - info.score()) * 100) / 100
                game.splash("Error", "Et falten " + ("" + falta) + "kg de llenya")
            }
            
        }
        
    } else if (opcio == 2) {
        //  VENDRE
        q = game.askForNumber("Quantes unitats tens de " + nom + "?", 2)
        if (validar_operacio(index_prod, q)) {
            guany = Math.round(q * preu * 100) / 100
            info.changeScoreBy(guany)
            music.powerUp.play()
            game.splash("Gràcies!", "Et dono " + ("" + guany) + "kg de llenya")
        }
        
    }
    
}

//  --- 3. CONFIGURACIÓ DE L'ENTORN ---
let jugador : Sprite = null
let venedor : Sprite = null
function generar_arbre() {
    let nou_arbre: Sprite;
    let c: number;
    let r: number;
    let loc: tiles.Location;
    if (sprites.allOfKind(KIND_ARBRE).length < 15) {
        //  Usa el nombre "miImagen" que tienes en assets para el árbol
        nou_arbre = sprites.create(assets.image`miImagen`, KIND_ARBRE)
        c = randint(1, 14)
        r = randint(1, 14)
        loc = tiles.getTileLocation(c, r)
        if (!tiles.tileAtLocationIsWall(loc) && Math.abs(c - 8) > 2) {
            tiles.placeOnTile(nou_arbre, loc)
        } else {
            nou_arbre.destroy()
        }
        
    }
    
}

function inicialitzar_entorn() {
    
    //  --- IMPORTANTE: Carga TU mapa desde Assets ---
    tiles.setCurrentTilemap(assets.tilemap`map`)
    //  VENEDOR (NPC)
    venedor = sprites.create(assets.image`miImagen2`, KIND_NPC)
    tiles.placeOnTile(venedor, tiles.getTileLocation(8, 7))
    //  JUGADOR (Nena)
    jugador = sprites.create(assets.image`nena-front`, SpriteKind.Player)
    tiles.placeOnTile(jugador, tiles.getTileLocation(8, 10))
    scene.cameraFollowSprite(jugador)
    controller.moveSprite(jugador)
    info.setScore(0)
    for (let i = 0; i < 10; i++) {
        generar_arbre()
    }
}

//  --- 4. BUCLES I ESDEVENIMENTS ---
inicialitzar_entorn()
game.onUpdateInterval(3000, function on_update_interval() {
    generar_arbre()
})
//  --- MENÚ DE TEXTO PARA SELECCIONAR---
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    let eleccio: number;
    if (jugador.overlapsWith(venedor)) {
        eleccio = game.askForNumber("1:Gal 2:Pat 3:Cab 4:Ou 5:Cav 0:Sortir", 1)
        if (1 <= eleccio && eleccio <= 5) {
            processar_transaccio(eleccio - 1)
        }
        
    }
    
})
//  -------------------------------------------------
controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    let arbres = sprites.allOfKind(KIND_ARBRE)
    let tajat = false
    for (let arb of arbres) {
        if (jugador.overlapsWith(arb)) {
            scene.cameraShake(2, 200)
            arb.destroy(effects.disintegrate, 200)
            info.changeScoreBy(5)
            music.smallCrash.play()
            jugador.sayText("+5kg", 500)
            tajat = true
            break
        }
        
    }
    if (!tajat) {
        jugador.sayText("No hi ha arbre!", 200)
    }
    
})
game.onUpdate(function on_update() {
    if (Math.abs(jugador.x - venedor.x) < 30 && Math.abs(jugador.y - venedor.y) < 30) {
        venedor.sayText("A: Mercat", 100)
    }
    
    let algun_aprop = false
    for (let arb of sprites.allOfKind(KIND_ARBRE)) {
        if (Math.abs(jugador.x - arb.x) < 20 && Math.abs(jugador.y - arb.y) < 20) {
            algun_aprop = true
            break
        }
        
    }
    if (algun_aprop) {
        jugador.sayText("B: Talar", 100)
    }
    
})
//  ANIMACIONES
controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up() {
    animation.runImageAnimation(jugador, assets.animation`nena-animation-up`, 200, false)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down() {
    animation.runImageAnimation(jugador, assets.animation`nena-animation-down`, 200, false)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left() {
    animation.runImageAnimation(jugador, assets.animation`nena-animation-left`, 200, false)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right() {
    animation.runImageAnimation(jugador, assets.animation`nena-animation-right`, 200, false)
})
