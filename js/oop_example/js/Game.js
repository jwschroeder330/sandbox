/* Title: Game
 * Author: jschroeder
 * Status: development
 */
class Game {
	constructor() {
		this.board = new Board();
		this.players = createPlayers();
		this.ready = false;
		this.playerColors = ['#e15258', '#e59a13'];
	}
	/*
	 * Creates two player objects
	 * @return {Array} An array of two Player objects
	 */
	createPlayers() {
		let players = [];
		for(let i = 0; i < 2; i += 1) {
			let active = i == 0 ? true : false;
			let player = new Player(name='Player ${i}', id=i, color=this.playerColors[i], active=active);
			players.push(player);
		}
		return players;
	}
	startGame() {
		
	}
}