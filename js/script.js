// script.js
const count =
document.getElementById('count');


updateVisitCount();

function updateVisitCount(){
    fetch('https://api.countapi.xyz/update/danielazocardev/codepen/?amount=1')
    .then(res => res.json())
    .then(res=>{count.innerHTML=res.value});
}

