let username1;
let username2;
let rnum;
let attempts;
let guessbf;
let maradt;
let setAttempts;
let roundsp1;
let roundsp2;
let p1point;
let p2point;
let clickCount = 0;
let win = 0;

const maxrounds = 3;
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
const nextBtn = document.getElementById("nextBtn");
const finishBtn = document.getElementById("finishBtn");
const users = [username1, username2]
const targetURL = "../nyiltnapdisplay/nydisplay.html"; 

function navigateTo(url){
  if (!url) return;
  window.location.href = url;
}

document.addEventListener("keydown", (event1) => {
  if (event1.ctrlKey && event1.shiftKey && event1.code === "KeyA") {
    navigateTo(targetURL);
  }
});

submitBtn.addEventListener("click", function(){
    username1 = player1Input.value.trim();
    username2 = player2Input.value.trim();
    if (!username1 || !username2) return;
    player12.textContent = `Üdvözöllek, ${username1} és ${username2}, készen álltok a játékra?!`;
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
    welcomeLetter.classList.add("hidden");        
    player12.classList.add("hidden");  
    player1Input.classList.add("hidden"); 
    submitBtn.classList.add("hidden");     
    startBtn.classList.add("hidden");     
    player2Input.classList.add("hidden"); 
    document.getElementById("kezdo").classList.add("hidden");
    document.getElementById("player1Game").classList.remove("hidden");
});

begginBtn.addEventListener("click", function(){
    player1Game.classList.add("hidden");

    player1Corner.innerHTML = username1;
    player1Corner.classList.remove("hidden");
    tippLines.classList.remove("hidden");

    const limits = [10, 100, 1000, 10000, 100000, 1000000];
    const max = limits[difficulty.value - 1];
    rnum = Math.floor(Math.random() * max) + 1;
    attempts = parseInt(attemptsInput.value);
    if (isNaN(attempts) || attempts <= 0)attempts = Infinity;
    setAttempts = attempts;

});

guessInput.addEventListener("keyup", function(event){
        if (event.key === "Enter"){
            tippBtn.click();
        }
});

tippBtn.addEventListener("click", function(){
    
    const guess = parseInt(guessInput.value);
    if (isNaN(guess)){
        guessLabel.textContent = "Kérlak adj meg egy számot:";
        return;
    }

    if (guess === guessbf || guess <= 0) {
        guessInput.value = "";
        guessInput.focus();
        return;
    }
    
    guessbf = guess;
    attempts--;

    const currentPlayer = (clickCount % 2 === 0) ? username1 : username2;

    const guessElement = document.createElement("div");
    if (rnum > guess){
        guessElement.textContent = `Tipped: ${guess}: túl kicsi`;
        guessLabel.textContent = `A számom nagyobb! ${attempts} próbád maradt még, kérlek add meg a következő tipped:`;
    }else if (rnum < guess){
        guessElement.textContent = `Tipped: ${guess}: túl nagy`;
        guessLabel.textContent = `A számom kisebb! ${attempts} próbád maradt még, kérlek add meg a következő tipped:`;
    }else{
        guessElement.textContent = `Tipped: ${guess}: eltaláltad!`;
        maradt = attemptsInput.value - attempts;
        win++;
        result.textContent = `Gratulálok ${currentPlayer}, eltaláltad ${maradt}. próbából! :) (A szám, amire gondoltam: ${rnum})`;
        roundsp1++;
        p1point++;
        tippLines.classList.add("hidden");
        result.classList.remove("hidden");
        nextBtn.classList.remove("hidden");
        finishBtn.classList.remove("hidden");
    }

    previousGuesses.insertBefore(guessElement, previousGuesses.firstChild);

    if (win === 0 && attempts === 0){
        setTimeout(() => {
            result.textContent = `Sajnos, elfogytak a tippelési lehetőségeid ${currentPlayer} ): , amúgy a(z) ${rnum}-re/ra gondoltam :)`;
            roundsp1++;
            tippLines.classList.add("hidden");
            result.classList.remove("hidden");
            nextBtn.classList.remove("hidden");
            finishBtn.classList.remove("hidden");
    }, 500);
    }

    guessInput.value = "";
    guessInput.focus();
   
});

function resetGame(){
    const limits = [10, 100, 1000, 10000, 100000, 1000000];
    const max = limits[difficulty.value - 1];
    rnum = Math.floor(Math.random() * max) + 1;
    guessLabel.textContent = "Kérlak adj meg egy számot:";
    attempts = setAttempts;
    guessbf = undefined;
    previousGuesses.innerHTML = "";
    result.classList.add("hidden");
    tippLines.classList.remove("hidden");
    nextBtn.classList.add("hidden");
    finishBtn.classList.add("hidden");
    win = 0;
    if (clickCount % 2 === 0) {
        player1Corner.innerHTML = username1;
    }else {
        player1Corner.innerHTML = username2;
    }
}

nextBtn.addEventListener("click" , function(){
    clickCount++;
    resetGame();
})

finishBtn.addEventListener("click" , function(){
    location.reload();
})

