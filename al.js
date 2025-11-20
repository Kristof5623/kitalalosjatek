// ...existing code...
const submitBtn = document.getElementById("submit");
const startBtn = document.getElementById("start1");
const playerMsg = document.getElementById("player1,2"); // ezt az id-t érdemes átnevezni egyszerűbbre a HTML-ben
const player1Input = document.getElementById("player1name");
const player2Input = document.getElementById("player2name");
const welcome = document.getElementById("welcomeLetter");
const player1Corner = document.getElementById("player1Corner");
const beker = document.getElementById("beker");
const beker1 = document.getElementById("beker1");

let username1 = "";
let username2 = "";

submitBtn.addEventListener("click", () => {
    username1 = player1Input.value.trim();
    username2 = player2Input.value.trim();
    if (!username1 || !username2) return;
    playerMsg.textContent = `Welcome ${username1} and ${username2}, are you ready to play?!`;
    playerMsg.classList.remove("hidden");
    startBtn.classList.remove("hidden");
});

startBtn.addEventListener("click", () => {
    // elrejti a kezdő UI-t
    welcome.classList.add("hidden");
    playerMsg.classList.add("hidden");
    player1Input.classList.add("hidden");
    player2Input.classList.add("hidden");
    submitBtn.classList.add("hidden");
    startBtn.classList.add("hidden");
    beker.classList.add("hidden");
    beker1.classList.add("hidden");

    // elindítja a játékot
    runGuessingGame();
});

function runGuessingGame() {
    // nehézség bekérése (1-6)
    let mod;
    do {
        mod = parseInt(prompt(
            "Válassz nehézséget:\n1 veryeasy (1-10)\n2 easy (1-100)\n3 normal (1-1.000)\n4 hard (1-10.000)\n5 veryhard (1-100.000)\n6 insane (1-1.000.000)"
        ), 10);
    } while (isNaN(mod) || mod < 1 || mod > 6);

    const limits = [10, 100, 1000, 10000, 100000, 1000000];
    const max = limits[mod - 1];
    const secret = Math.floor(Math.random() * max) + 1;

    let attempts = 0;
    let guess;
    do {
        attempts++;
        guess = parseInt(prompt(`Tippeld meg a számot (1 - ${max}):`), 10);
        if (isNaN(guess)) {
            alert("Kérlek számot adj meg.");
            attempts--; // ne számolja az érvénytelen bevitel
            continue;
        }
        if (guess < secret) {
            alert("A számom nagyobb.");
        } else if (guess > secret) {
            alert("A számom kisebb.");
        }
    } while (guess !== secret);

    const result = `Gratulálok, eltaláltad ${attempts}. próbára (titkos szám: ${secret}).`;
    // megjelenítés a player1Corner-ban
    player1Corner.textContent = `${username1}: ${result}`;
    player1Corner.classList.remove("hidden");
}
// ...existing code...