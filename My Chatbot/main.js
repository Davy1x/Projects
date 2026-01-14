const headText = document.getElementById('intro_text')
const startChat = document.getElementById('start_chat')
const loader = document.getElementById('loader')
const overlay = document.getElementById('overlay')
const body = document.body

window.addEventListener('load', ()=> {
    loader.style.display = 'none'
    body.style.overflow = 'auto'
})