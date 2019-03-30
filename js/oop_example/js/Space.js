/* Title: Space
 * Author: jschroeder
 * Status: development
 */
class Space {
	/*
	 * @param x {Integer} column
	 * @param y {Integer} row
	 * @param id {String} gives us a useful way to identify the space in browser
	 * @param token gives us a way to associate a Token object
	 */
	constructor(x, y) {
		this.x = x;
		this.y = y;
		this.id = 'space-${x}-${y}';
		this.token = null;
		this.diameter = 76;
		this.radius = (diameter / 2);
	}
	/*
	 * Create an SVG and style it to meet the visual needs of the game
	 */
	drawSVGSpace() {
		// create a circle SVG element and save as a variable
		const svgSpace = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
		// set several attributes on the svg
		svgSpace.setAttributeNS(null, 'id', this.id);
		svgSpace.setAttributeNS(null, 'cx', (this.x * this.diameter));
		svgSpace.setAttributeNS(null, 'cy', (this.y * this.diameter));
		svgSpace.setAttributeNS(null, 'r', this.radius - 8);
		svgSpace.setAttributeNS(null, 'fill', 'black');
		svgSpace.setAttributeNS(null, 'stroke', 'none');
		// finally attach the svgSpace to the DOM
		document.getElementById('mask').appendChild(svgSpace);
	}
}