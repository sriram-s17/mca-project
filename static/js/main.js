let menu_icon = document.querySelector('.menu_icon')
let main_content = document.querySelector(".content")
let sidebar = document.querySelector(".sidebar")
menu_icon.addEventListener("click", ()=>{
    toggle_sidebar(sidebar.classList.contains("shown"));
})
const mediaquery = window.matchMedia('(max-width:850px)');

// adding listener for changes
mediaquery.onchange =()=> toggle_sidebar(mediaquery.matches)

function toggle_sidebar(condition){
    if(condition){
        sidebar.classList.remove("shown")
        sidebar.classList.add("hide")
        main_content.classList.add("full_display")
    }
    else{
        sidebar.classList.add("shown")
        sidebar.classList.remove("hide")
        main_content.classList.remove("full_display")
    }
}