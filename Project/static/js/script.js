const button = document.querySelector('.change-button');
const divOfChangeMenu = document.querySelector('.left-menu');
const buttonChangeDarkMode = document.createElement('button');

let darkMode = false;
let opneClose = false;

const h1 = document.querySelectorAll('h1');
const nav = document.querySelector('.navigation');
const mainMenu = document.querySelectorAll('.main');
const cards = document.querySelectorAll('.con');;
const mainText = document.querySelectorAll('.main-text');

button.addEventListener('click', () => {
    if (opneClose === false){
        button.textContent = '<';
        divOfChangeMenu.style.transition = '0.5s';
        divOfChangeMenu.style.display = 'flex';
        divOfChangeMenu.style.width = '325px';
        divOfChangeMenu.style.background = '#6D6D6D';
        divOfChangeMenu.appendChild(buttonChangeDarkMode);
        buttonChangeDarkMode.textContent = 'Темний режим';
        buttonChangeDarkMode.style.width = '175px';
        buttonChangeDarkMode.style.height = '50px';
        buttonChangeDarkMode.style.border = '#007BFF solid';
        buttonChangeDarkMode.style.borderRadius = '25px';
        buttonChangeDarkMode.style.margin = 'auto';
        buttonChangeDarkMode.style.background = '#007BFF';
        buttonChangeDarkMode.style.color = '#FFFFFF';
        buttonChangeDarkMode.style.fontSize = '24px';
        opneClose = true;
    }else{
        button.textContent = '>';
        opneClose = false;
        buttonChangeDarkMode.remove();
        divOfChangeMenu.style.width = '75px';
        divOfChangeMenu.style.background = '#212529';
    }
});

buttonChangeDarkMode.addEventListener('click', () => {
    if (darkMode === false){
        document.body.style.background = '#1C1F2A';
        nav.style.background = '#8B1E3F';
        h1.forEach(text => {
            text.style.color = '#FFFFFF'           
        });
        mainMenu.forEach(menu => {
            menu.style.background = '#D9D9D9'    
            menu.style.color = '#FFFFFF'         
        });
        cards.forEach(card => {
            card.style.background = '#FF5C00'
        });
        mainText.forEach(text => {
            text.style.background = '#8B1E3F'  
        });
        darkMode = true;
    }else{
        document.body.style.background = '#FFFFFF';
        nav.style.background = '#007BFF';
        h1.forEach(text => {
            text.style.color = '#000000'            
        });
        mainMenu.forEach(menu => {
            menu.style.background = '#B4B7BA'  
            menu.style.color = '#000000'           
        });
        cards.forEach(card => {            
            card.style.background = '#007BFF'
        });
        mainText.forEach(text => {
            text.style.background = '#4da3ff'  
        });
        darkMode = false;
    };
});