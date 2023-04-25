const faqContainer = document.querySelector(".faq-container");
function displayContents(){
    const questions = document.querySelectorAll(".indiv-faq");
    questions.forEach(function(question){
        const toggleBtn = question.querySelector(".up-down");
        toggleBtn.addEventListener('click',function(){
            console.log('hello');
            questions.forEach(function(item){
                if (item != question){
                    item.classList.remove("show-faq");
                }
            });
            question.classList.toggle("show-faq");
        });
    });
}
window.addEventListener("DOMContentLoaded",function(){
    displayContents()
});