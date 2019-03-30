/* Title: Main
 * Author: jschroeder
 * Status: development
 */
// initialize our game object
const game = new Game();

// initialize our start button and wait to start the game
let startButton = document.getElementById('begin-game');
startButton.addEventListener('click', () => {
	game.startGame();
	this.style.display = 'none';  // hide the start button
	document.getElementById('play-area').style.opacity = '1';  // make the play area visible
});

