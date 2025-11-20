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


submitBtn.addEventListener("click", function(){
    username1 = player1Input.value.trim();
    username2 = player2Input.value.trim();
    if (!username1 || !username2) return;
    player12.textContent = `Welcome ${username1} and ${username2}, are you ready to play?!`;
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
    tippLines.classList.remove("hidden")

    const limits = [10, 100, 1000, 10000, 100000, 1000000];
    const max = limits[difficulty.value - 1];
    rnum = Math.floor(Math.random() * max) + 1;
    attempts = parseInt(attemptsInput.value)
    if (isNaN(attempts) || attempts <= 0)attempts = Infinity;
});

guessInput.addEventListener("keyup", function(event){
    if (event.key === "Enter"){
        tippBtn.click();
    }
});

tippBtn.addEventListener("click", function(){
    
    const guess = parseInt(guessInput.value);
    if (isNaN(guess)){
        guessLabel.textContent = "Please  enter a number:";
        return;
    }

  if (guess === guessbf || guess <= 0) {
        guessInput.value = "";
        guessInput.focus();
        return;
    }
    
    guessbf = guess;
    attempts--;

    const guessElement = document.createElement("div");
    if (rnum > guess){
        guessElement.textContent = `Your guess: ${guess}: too small`;
        guessLabel.textContent = `The number is bigger! ${attempts} attempst left, please enter your next guess:`;
    }else if (rnum < guess){
        guessElement.textContent = `Your guess: ${guess}: too big`;
        guessLabel.textContent = `The number is smaller! ${attempts} attempst left, please enter your next guess:`;
    }else{
        guessElement.textContent = `Your guess: ${guess}: you guess it!`;
        maradt = attemptsInput.value - attempts;
        result.textContent = `Congratulations ${username1}, you guess it, in ${maradt}. attempts! :) (The number, what i thought: ${rnum})`;
        tippLines.classList.add("hidden");
        result.classList.remove("hidden");
    }

    previousGuesses.insertBefore(guessElement, previousGuesses.firstChild);

    if (attempts === 0){
        setTimeout(() => {
            result.textContent = `Sadly your attempts run out ${username1} ): , anyway The ${rnum} is what I thought :)`;
            tippLines.classList.add("hidden");
            result.classList.remove("hidden");
    }, 500);
    }

    guessInput.value = "";
    guessInput.focus();
});




