//sidebar
const sidebar = document.querySelector(".sidebar");
const navToggle = document.querySelector(".nav-toggle");
const closeBtn = document.querySelector(".close-btn");

navToggle.addEventListener("click", function(){
    sidebar.classList.toggle('show-sidebar');
});

closeBtn.addEventListener("click",function(){
    sidebar.classList.remove("show-sidebar");
});