const orderBtn = document.querySelector(".cart-order");
const sidebar = document.querySelector(".sidebar");

orderBtn.addEventListener("click",function(){
    sidebar.classList.toggle("show-sidebar");
});