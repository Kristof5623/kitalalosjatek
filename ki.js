// ...existing code...
let username1;
let username2;
let rnum;
let attempts;
let guessbf;
let maradt;

const submitBtn = document.getElementById("submit");
const startBtn = document.getElementById("start1");
const player12 = document.getElementById("player1,2");
const player1Input = document.getElementById("player1name");
const player2Input = document.getElementById("player2name");
const difficulty = document.querySelector("#player1Difficulty select");
const attemptsInput = document.getElementById("attempts");
const result = document.getElementById("result");
const guessInput = document.getElementById("guess");
const tippLines = document.getElementById("tippLines"); 
const tippBtn = document.getElementById("tippBtn"); 
const begginBtn = document.getElementById("begginBtn");
const previousGuesses = document.getElementById("previousGuesses");

const scoresDiv = document.getElementById("scores");
const nextTurnBtn = document.getElementById("nextTurnBtn");

let currentPlayer = 1; // 1 vagy 2
let scores = {1: 0, 2: 0};
let turnsDone = 0; // összes lejátszott forduló (minden player turn növeli)
const maxRounds = 3; // minden player 3 turn => maxTurns = maxRounds * 2

function updateScoresUI() {
    scoresDiv.textContent = `Pontok — ${username1}: ${scores[1]} | ${username2}: ${scores[2]} — Kör: ${Math.floor(turnsDone/2)+1}/${maxRounds}`;
    scoresDiv.classList.remove("hidden");
}

// start egy adott játékos körét (ugyanazokkal a beállításokkal)
function startTurnFor(player) {
    currentPlayer = player;
    guessbf = undefined;
    previousGuesses.innerHTML = "";
    result.classList.add("hidden");
    tippLines.classList.remove("hidden");
    tippBtn.disabled = false;
    guessInput.disabled = false;
    guessInput.value = "";
    guessInput.focus();

    // beállítjuk a sarokban a jelenlegi játékost
    const name = (currentPlayer === 1) ? username1 : username2;
    const corner = document.getElementById("player1Corner");
    corner.textContent = name;
    corner.classList.remove("hidden");

    // titkos szám és próbák (ugyanazok a beállítások minden körben)
    const limits = [10, 100, 1000, 10000, 100000, 1000000];
    const max = limits[parseInt(difficulty.value, 10) - 1] || 10;
    rnum = Math.floor(Math.random() * max) + 1;
    let total = parseInt(attemptsInput.value, 10);
    attempts = (isNaN(total) || total <= 0) ? Infinity : total;

    updateScoresUI();
}

// inicializálás: submit/start gombok meglévő logikája
submitBtn.addEventListener("click", function(){
    username1 = player1Input.value.trim();
    username2 = player2Input.value.trim();
    if (!username1 || !username2) return;
    player12.textContent = `Üdvözölek ${username1} és ${username2}, készenáltok a játékra?!`;
    player12.classList.remove("hidden"); 
    startBtn.classList.remove("hidden"); 
});

player2Input.addEventListener("keyup", function(e){
    if (e.key !== "Enter") return;
    if (!startBtn.classList.contains("hidden") && !startBtn.disabled) {
        startBtn.click();
    } else {
        submitBtn.click();
    }
});

startBtn.addEventListener("click", function(){
    document.getElementById("kezdo").classList.add("hidden");
    document.getElementById("player1Game").classList.remove("hidden");
    // induljon az 1. játékos körével
    startTurnFor(1);
});

// Enter mint Tipp -> egyszeri listener
guessInput.addEventListener("keyup", function(event){
    if (event.key === "Enter"){
        tippBtn.click();
    }
});

// Tipp feldolgozás
tippBtn.addEventListener("click", function(){
    const guess = parseInt(guessInput.value, 10);
    if (isNaN(guess)){
        // rövid üzenet a result-ban
        result.textContent = "Kérlek adj meg egy számot!";
        result.classList.remove("hidden");
        return;
    }

    if (guess === guessbf || guess <= 0) {
        guessInput.value = "";
        guessInput.focus();
        return; // duplikát esetén nem vonunk le próbát
    }
    
    guessbf = guess;
    // csak véges esetben csökkentjük
    if (Number.isFinite(attempts)) {
        attempts = Math.max(0, attempts - 1);
    }

    const guessElement = document.createElement("div");
    if (rnum > guess){
        guessElement.textContent = `Tipp: ${guess} → túl kicsi`;
        result.textContent = `A számom nagyobb! ${Number.isFinite(attempts) ? attempts : "∞"} próbád maradt.`;
    } else if (rnum < guess){
        guessElement.textContent = `Tipp: ${guess} → túl nagy`;
        result.textContent = `A számom kisebb! ${Number.isFinite(attempts) ? attempts : "∞"} próbád maradt.`;
    } else {
        guessElement.textContent = `Tipp: ${guess} → eltaláltad!`;
        // pont jár, ha eltalálta
        scores[currentPlayer] = (scores[currentPlayer] || 0) + 1;
        maradt = (isFinite(parseInt(attemptsInput.value, 10)) ? (parseInt(attemptsInput.value, 10) - attempts) : "ismeretlen");
        result.textContent = `Gratulálok ${ (currentPlayer===1)?username1:username2 }, eltaláltad ${maradt} próbából! (A szám: ${rnum})`;
        // lezárjuk a kört
        tippLines.classList.add("hidden");
        tippBtn.disabled = true;
        guessInput.disabled = true;
        result.classList.remove("hidden");
        turnsDone++;
        updateScoresUI();
        // ha elértük a max teljes turn számot, vége a mérkőzés
        if (turnsDone >= maxRounds * 2) {
            // végeredmény
            setTimeout(() => showFinalResult(), 600);
        } else {
            // mutatjuk a next gombot (következő játékos)
            nextTurnBtn.textContent = `Következő: ${(currentPlayer===1)?username2:username1}`;
            nextTurnBtn.classList.remove("hidden");
        }
        previousGuesses.insertBefore(guessElement, previousGuesses.firstChild);
        guessInput.value = "";
        return;
    }

    previousGuesses.insertBefore(guessElement, previousGuesses.firstChild);

    // ha elfogytak a próbák (és nem talált)
    if (Number.isFinite(attempts) && attempts === 0){
        // játékos vesztett ezen a körön
        tippLines.classList.add("hidden");
        tippBtn.disabled = true;
        guessInput.disabled = true;
        result.textContent = `Sajnos elfogytak a próbáid. A szám: ${rnum}`;
        result.classList.remove("hidden");
        turnsDone++;
        updateScoresUI();
        if (turnsDone >= maxRounds * 2) {
            setTimeout(() => showFinalResult(), 600);
        } else {
            nextTurnBtn.textContent = `Következő: ${(currentPlayer===1)?username2:username1}`;
            nextTurnBtn.classList.remove("hidden");
        }
    }

    guessInput.value = "";
    guessInput.focus();
});

// Next turn gomb – elindítja a következő játékos körét ugyanazon beállításokkal
nextTurnBtn.addEventListener("click", function(){
    nextTurnBtn.classList.add("hidden");
    // váltás
    const nextPlayer = (currentPlayer === 1) ? 2 : 1;
    startTurnFor(nextPlayer);
});

// végeredmény megjelenítése
function showFinalResult() {
    tippLines.classList.add("hidden");
    nextTurnBtn.classList.add("hidden");
    const p1 = scores[1] || 0;
    const p2 = scores[2] || 0;
    let finalText = `Vége a meccsnek. Pontok — ${username1}: ${p1} | ${username2}: ${p2}. `;
    if (p1 > p2) finalText += `${username1} nyert!`;
    else if (p2 > p1) finalText += `${username2} nyert!`;
    else finalText += "Döntetlen!";
    result.textContent = finalText;
    result.classList.remove("hidden");
    // tiltsuk le a tippelést
    tippBtn.disabled = true;
    guessInput.disabled = true;
    // opcionálisan mutathatsz restart gombot itt (nem módosítom)
}
// ...existing code...