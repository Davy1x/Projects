let upDown = 0;
let leftRight = 0;
const ball = document.getElementById('ball').style;
const uri = 'ws://127.0.0.1:8080';
const sock = new WebSocket(uri);

sock.addEventListener('open',()=>{
  console.log("@RECEIVER: game connected successfully --return");
})
sock.addEventListener('error',()=>{
  console.log("@RECEIVER: err_detect --serve ? / reciver ? stat_err --return");
})

sock.addEventListener('message',(msg)=>{
  circuit(msg.data);
})

function circuit(cmd) {
  switch (cmd) {
    case 'up':
      upDown++;
      break;
    case 'down':
      upDown--;
      break;
    case 'right':
      leftRight++;
      break;
    case 'left':
      leftRight--;
      break;
    
    default:
      console.log("Active");
  }
  ball.top = upDown + 'px';
  ball.left = leftRight + 'px';
}