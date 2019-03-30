/* Title: Player
 * Author: jschroeder
 * Status: development
 */
import Token from Token
class Player {
	constructor(name, id, color, active=false){
		this.name = name;
		this.id = id;
		this.color = color;  // if they choose one of the accepted, then use, else use a random color
		this.active = active;  // turn is decided when starting the game and alternates thereafter
		this.tokens = this.createTokens(21);  // 21 is the number of tokens to create
	}
	/* 
	 * Creates token objects for player
	 * @param {integer} num - Number of token objects to be created
	 * @returns {Array} An array of the newly created tokens
	 */
	createTokens(num) {
		let tokens = [];
		for(let i = 0; i < num; i += 1) {
			tokens.push(new Token(owner=this, index=i));
		}
		return tokens;
	}
}