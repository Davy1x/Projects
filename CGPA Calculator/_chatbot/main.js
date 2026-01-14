//LOADER
const loader = document.getElementById('loader')
const overlay = document.getElementById('overlay')
const body = document.getElementById('body')
window.addEventListener('load', () => {
  const aiVid = document.getElementById('ai-vid')
  aiVid.oncanplaythrough = () => {
    loader.style.display = 'none'
    body.style.overflowY = 'scroll'
  }
})

//Notification
const notification = document.getElementById('notification')
function sendNotification(
  icon = "fas fa-envelope",
  text = "Thanks for using our Application.",
  feedback = true
) {
  notification.style.display = 'flex'
  overlay.style.display = 'block'
  body.style.overflowY = 'hidden'
  notification.querySelector('i').className = icon
  notification.querySelector('p').textContent = text
  const buttons = notification.querySelectorAll('button')
  if (feedback) {
    buttons[1].textContent = 'Accept'
  } else {
    buttons[1].textContent = 'Ok'
  }
  buttons.forEach((btn) => { btn.onclick = null })
  return new Promise((resolve, reject) => {
    buttons[0].onclick = () => {
      notification.style.display = 'none'
      overlay.style.display = 'none'
      body.style.overflowY = 'scroll'
      resolve("reject")
    }
    buttons[1].onclick = () => {
      notification.style.display = 'none'
      overlay.style.display = 'none'
      body.style.overflowY = 'scroll'
      resolve("accept")
    }
  })
}

//FOOTER OPERATIONS
const userInput = document.getElementById('input-box')
const sendBtn = document.getElementById('send-btn')

userInput.addEventListener('keydown',(event)=>{
  if (event.key === "Backspace") {
    userInput.style.height = `${userInput.scrollHeight - 1}px`
  }
  userInput.style.height = `${userInput.scrollHeight}px`
})