/* Title: Board
 * Author: jschroeder
 * Status: development
 */
class Board {
	constructor() {
		this.rows = 6;
		this.columns = 7;
		this.spaces = [];
	}
	/*
	 * Creates and returns a 2D array of space objects
	 * @returns {Array} 2D collection of Space objects
	 */
	createSpaces() {
		let spaces = [];
		// for each row
		for(let x = 0; x < this.columns; x += 1) {
			let column = [];
			for(let y = 0; y < this.columns; y += 1) {
				column.push(new Space(x=x, y=y));
			}
			spaces.push(column);
		}
		return spaces;
	}
	/*
	 * Draw the graphics for the holes in the game
	 * Using the SvgSpace method on the Space object
	 */
	drawHTMLBoard() {
		for(let x = 0; x < this.spaces.length; x += 1) {
			for(let y = 0; y < this.spaces[x].length; y += 1) {
				this.spaces[x][y].drawSVGSpace();
			}
		}
	}
}