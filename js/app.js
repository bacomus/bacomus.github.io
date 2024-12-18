let choices = ['Rock', 'Paper', 'Scissor']
let round = 1
let playerScore = 0;
let computerScore = 0;
const computerChoiceDisplay = document.getElementById("computerChoiceDisplay");
const userChoiceDisplay = document.getElementById("userChoiceDisplay");
const roundDisplay = document.getElementById("roundDisplay")

function playGame(playerChoice){
  if (round > 5){
    roundDisplay.textContent = "Game Over! Reset to play again.";
    return;
  }

  const computerChoice = choices[Math.floor(Math.random() * 3)];
  let result = "";
  if (playerChoice === computerChoice){
    result = 'Tie'
    round++;
  } else if (playerChoice === 'Rock' && computerChoice === 'Paper' || playerChoice === 'Paper' && computerChoice === 'Scissor' || playerChoice === 'Scissor' && computerChoice === 'Rock') {
    result = 'You lose'
    computerScore++;
    round++;
  } else {
    result = 'You win'
    playerScore++;
    round++;
  }

  computerChoiceDisplay.textContent = `Computer: ${computerChoice}`;
  userChoiceDisplay.textContent = `Player: ${playerChoice}`;
  roundDisplay.textContent = `Round ${round - 1} Result: ${result}`;
  scoreDisplay.textContent = `Score - Player: ${playerScore} | Computer: ${computerScore}`;
}

function resetGame(){
  round = 1
  computerScore = 0
  playerScore = 0
  computerChoiceDisplay.textContent = "Computer: ";
  userChoiceDisplay.textContent = "Player: ";
  roundDisplay.textContent = "Start a new game!";
  scoreDisplay.textContent = "Score - Player: 0 | Computer: 0";
}