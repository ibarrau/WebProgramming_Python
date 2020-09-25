document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = count;
});

let counter = 0;

function count(){
    counter++;
    //It only selects the FIRST h1 in the page.
    document.querySelector('#counter').innerHTML = counter;
    
    // % chequear resto (remainer) y triple para valores exactos
    if (counter % 10 === 0) {
        // Estas ese simbolo ayuda a poner variables dentro del mensaje
        alert(`Counter is at ${counter}!`)
    }
}