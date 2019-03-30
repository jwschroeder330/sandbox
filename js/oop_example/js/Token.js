/* Title: Token
 * Author: jschroeder
 * Status: development
 */
class Token {
	constructor(owner, index){
		this.owner = owner;
		this.id = 'token-${index}-${owner.id}';  // there will be many token objects, how do we reference them?
		this.dropped = false;
	}
	/*
	 *
	 *
	 */
	drawHTMLToken() {
		let token = document.createElement('div');
		document.getElementById('game-board-underlay').appendChild(token);
		token.setAttribute('id', this.id);
		token.setAttribute('class', 'token');
		token.setAttribute('background-color', this.owner.color);
	}
	/*
	 *
	 *
	 */
	get htmlToken() {
		return this.drawHTMLToken();
	}
}