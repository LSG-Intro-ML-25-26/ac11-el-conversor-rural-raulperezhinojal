//  --- 1. CONFIGURACIÓ I TIPIFICACIÓ ---
let KIND_ARBRE = SpriteKind.create()
let KIND_NPC = SpriteKind.create()
//  Dades del mercat
let LLISTA_NOMS = ["Gallina", "Patates (kg)", "Cabra", "Ous", "Cavall"]
let LLISTA_PREUS = [6, 1.33, 5, 0.25, 12]
let ES_ANIMAL = [true, false, true, false, true]
//  --- 2. LÒGICA DE MERCAT ---
function validar_operacio(index: any, quantitat: number): boolean {
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

function processar_transaccio(index_prod: any) {
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
