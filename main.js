const choix = ["Pierre", "Feuille", "Ciseaux"];
const joueur = document.getElementById("joueur");
const ordi = document.getElementById("ordi");
const resultat = document.getElementById("resultat");
const score = document.getElementById("score");
const rejouerBtn = document.getElementById("rejouer");

let manche = 0;

function playRound(humanChoice) {
    if (manche >= 5) return;

    const choixOrdi = choix[Math.floor(Math.random() * 3)];
    let res = "";

    if (humanChoice === choixOrdi) {
        res = "MATCH NUL";
    } else if (
        (humanChoice == "Pierre" && choixOrdi == "Feuille") ||
        (humanChoice == "Feuille" && choixOrdi == "Ciseaux") ||
        (humanChoice == "Ciseaux" && choixOrdi == "Pierre")
    ) {
        res = "VOUS AVEZ PERDU";
    } else {
        res = "VOUS AVEZ GAGNÉ";
    }

    joueur.textContent = `CHOIX JOUEUR : ${humanChoice}`;
    ordi.textContent = `CHOIX ORDI : ${choixOrdi}`;
    resultat.textContent = `RÉSULTAT : ${res}`;
    
    manche++;
    score.textContent = `Manche : ${manche}/5`;

    if (manche === 5) {
        rejouerBtn.style.display = "block";
    }
}

function resetGame() {
    manche = 0;
    joueur.textContent = "CHOIX JOUEUR :";
    ordi.textContent = "CHOIX ORDI :";
    resultat.textContent = "RÉSULTAT :";
    score.textContent = "Manche : 0/5";
    rejouerBtn.style.display = "none";
}