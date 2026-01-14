//SIDEBAR TOGGLE 
document.querySelector('.sidebar-toggle').addEventListener('click', () => {
    document.querySelector('.sidebar').classList.toggle('open');
    document.querySelector('.overlay').classList.toggle('active');
});


//BACKGROUND AUDIO
let audioBtn = document.getElementById('audio-btn');
let bgAudio1 = document.getElementById('bg-audio1');
let bgAudio2 = document.getElementById('bg-audio2');
let bgAudio3 = document.getElementById('bg-audio3');
let bgAudio4 = document.getElementById('bg-audio4');
let bgAudio5 = document.getElementById('bg-audio5');

let audArr = [bgAudio1, bgAudio2, bgAudio3, bgAudio4, bgAudio5];
let randAud = Math.floor(Math.random() * 5);
let setAud = audArr[randAud];

var ba = true;

let toggleAudio = () => {
  if (ba) {
    setAud.play();
    ba = !ba;
    audioBtn.classList.remove("bxs-volume-mute");
    audioBtn.classList.add("bxs-volume-full");
  } else {
    setAud.pause();
    ba = !ba;
    audioBtn.classList.remove("bxs-volume-full");
    audioBtn.classList.add("bxs-volume-mute");
  }
};
audioBtn.addEventListener('click', toggleAudio);


//RESET-AUDIO-STATE-BEFORE-A-NEW-LOAD
window.addEventListener("beforeunload", () => {
  bgAudio1.pause();
  bgAudio2.pause();
  bgAudio3.pause();
  bgAudio4.pause();
  bgAudio5.pause();
  audioBtn.classList.remove("bxs-volume-full");
  audioBtn.classList.add("bxs-volume-mute");
  bgTheme.classList.remove('bxs-laugh');
  bgTheme.classList.add('bxs-dizzy');
});


//RELOAD PAGE
function reload(){ location.reload()};


/*New Notification
var path = window.location.pathname;
if (path.endsWith('index.html')) {
  if (!localStorage.getItem('notify')) {
    localStorage.setItem('notify', 'here');
    setTimeout( () => {
    alert('1 New Message Available!');
    location.href = 'notify.html';},2000);
  } else {
   console.log('Skipping notification...')
  }
}*/

//notification update
let bell = document.getElementById('ring-bell');

let bellStatus = 'off';

const alertMsg = () => { 
  if (bellStatus === 'off') {
    bell.classList.remove('bx-bell');
    bell.classList.add('bxs-bell-ring');
    bellStatus = 'on';
  } else {
    bell.classList.remove('bxs-bell-ring');
    bell.classList.add('bx-bell');
    bellStatus = 'off';
  }
};
setInterval(alertMsg, 1000);

//Forward Messages
const userName = document.getElementById('name');
const userNumber = document.getElementById('number');
const userMessage = document.getElementById('message');
const sendUserMessage = document.getElementById('send-msg');
const userMsgWarn = document.getElementById('msg-warn');

sendUserMessage.addEventListener('click', () => {
  if ((userName.value === '') || (userNumber.value === '') || (userMessage.value === '')) {
    sendUserMessage.innerText = '';
    sendUserMessage.innerText = 'Please fill out the form!';
    sendUserMessage.style.background = '';
    sendUserMessage.style.background = '#E57373';
    
    setTimeout(() => {
      sendUserMessage.innerText = '';
      sendUserMessage.innerText = 'Send Message';
      sendUserMessage.style.background = '';
      sendUserMessage.style.background = ' rgba(255, 255, 255, 0.1)';
    },2000)
  } else {
    
    let nameArr = userName.value.split(' ');
    nameArr = nameArr.filter((e) => e.trim() !== '').join(' ');
      
    let numArr = userNumber.value;
    
    let msgArr = userMessage.value.split(' ');
    msgArr = msgArr.filter((l) => l.trim() !== '').join(' ');
    
    sendUserMessage.innerText = '';
    sendUserMessage.innerText = 'Sending';
    sendUserMessage.style.background = '';
    sendUserMessage.style.background = '#FFE082';
    
    const msgToTelegram = `From Codavi Website\n\nName: ${nameArr}\n\nPhone: ${numArr}\n\nMessage Content: ${msgArr}`;
    const teleChatId = `6388314252`;
    const teleTokenId = `7692671260:AAF4ZLB2FTu8uoYOz0ioN6K9WdHVwi3lTZY`;
    
    fetch(`https://api.telegram.org/bot${teleTokenId}/sendMessage?chat_id=${teleChatId}&text=${encodeURIComponent(msgToTelegram)}`).then((data) => {
      if(data.ok) {
      sendUserMessage.innerText = '';
      sendUserMessage.innerText = 'Sent!';
      sendUserMessage.style.background = '';
      sendUserMessage.style.background = '#81C784';
      document.getElementById('success-msg').innerText = `Thank you ${nameArr}`;
      setTimeout(() => {
        sendUserMessage.innerText = '';
        sendUserMessage.innerText = 'Send Message';
        document.getElementById('success-msg').innerText = 'Message';
        sendUserMessage.style.background = '';
        sendUserMessage.style.background = ' rgba(255, 255, 255, 0.1)';
        }, 4000);
        setTimeout(() => {location.reload()}, 7000)
      } else {
        sendUserMessage.innerText = '';
        sendUserMessage.innerText = 'Failed!';
        sendUserMessage.style.background = '';
        sendUserMessage.style.background = '#E57373';
        setTimeout(() => {
          sendUserMessage.innerText = '';
          sendUserMessage.innerText = 'Send Message';
          sendUserMessage.style.background = '';
          sendUserMessage.style.background = ' rgba(255, 255, 255, 0.1)';
        }, 3000);
      }
    })
  }
});