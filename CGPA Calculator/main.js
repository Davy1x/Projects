//LOADER
const loader = document.getElementById('loader')
const overlay = document.getElementById('overlay')
const body = document.getElementById('body')
window.addEventListener('load', () => {
  loader.style.display = 'none'
  body.style.overflowY = 'scroll'
})

//Notification
const notification = document.getElementById('notification')
function sendNotification(
  icon = "fas fa-envelope",
  text = "Thank you for using our Application.",
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
    buttons[1].textContent = 'Email Us'
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


const headerButtons = document.getElementById('header-buttons').querySelectorAll('button')
headerButtons.forEach((btn, index) => {
  if (index === 0) {
    btn.onclick = () => window.location.assign('./_calculator')
  } else if (index === 1) {
    btn.onclick = async () => {
      await sendNotification(
        "fas fa-envelopes-bulk",
        "Contact Us Via Email!",
        false
      ).then((res) => {
        
      })
    }
  }
})