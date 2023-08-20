const bar= document.getElementById("bar")
const navbar= document.getElementById("navbar")
const close= document.getElementById("close")
if(bar){
    document.addEventListener('click',()=>{
        navbar.classList.add('active');
    })
}
// if(close){
//     document.addEventListener('click',()=>{
//         navbar.classList.remove('active');
//     })
// }