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
		let div = document.createElement('div');
		div.setAttribute('id') = this.id;
		div.setAttribute('class') = 'token';
		div.setAttribute('background-color') = this.owner.color;
		document.getElementById('game-board-underlay').appendChild(div);
		return div;
	}
	/*
	 *
	 *
	 */
	get htmlToken() {
		return this.drawHTMLToken();
	}
}