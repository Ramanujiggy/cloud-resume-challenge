// script.js
const count =
document.getElementById('count');


updateVisitCount();

function updateVisitCount(){
    fetch('https://personalsitegenie.azurewebsites.net/api/http_trigger?code=xJF62ARATa722za-unJXD2qwdng5WsRohzdu4-goM2fGAzFuEP_xLg%3D%3D')
    .then(res => res.json())
    .then(res=>{count.innerHTML=res.value});
}

