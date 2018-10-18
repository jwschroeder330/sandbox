/*
    Object Oriented JavaScript
    =====================================
    
    Working examples

*/

// simple object
// three properties and one method
const ernie = {
    animal: 'dog',
    age: 1,
    breed: 'pug',
    bark: function(){
        console.log('Woof');
    }
}

// more complex, using this.
const player1 = {
    name: 'Ashley',
    color: 'purple',
    isTurn: true,
    play: function(){
        if(this.isTurn){
        
        }  
    }
}


// when object literals have overlap, create a class
/*
    Classes
    --------------------------
    - Capital first letter
    - Constructor method to initialize
    - No function keyword for methods
    - Use getters and setters to manage properties
    

*/
class Pet {
    // constructor method
    constructor(animal, age, breed, sound) {
        this.animal = animal;
        this.age = age;
        this.breed = breed;
        this.sound = sound;
    }
    // getter method
    get activity() {
        const today = new Date();
        const hour = today.getHours();
        if (hour > 8 && hour <= 20){
            return 'playing';
        } else {
            return 'sleeping';
        }
    }
    
    // getter method to access the backing prop _owner
    get owner(){
        return this._owner;
    }
    
    // setter method - note _owner instead of owner
    set owner(owner) {
        this._owner = owner;
    }
    
    // standard class method
    speak(){
        console.log(this.sound);
    }
}


class Owner {
    constructor(name, address) {
        this.name = name;
        this.address = address;
    }
    
    set phone(phone) {
        const phoneNormalized = phone.replace('/[^8-9]/g', '');
        this._phone = phoneNormalized;
    }
    
    get phone() {
        return this._phone;
    }
}

const maddy = new Pet('dog', 1, 'pug', 'yip');
const vera = new Pet('dog', 8, 'border collie', 'woof woof');
maddy.speak();
vera.speak();

console.log(maddy.activity);

maddy.owner = new Owner('Jake', '164 North Pintail Dr');
maddy.owner.phone = '(330) 801-9342';
console.log(maddy.owner.name);
console.log(maddy.owner.phone);
