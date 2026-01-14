let logArr = [];
const logger = (cmd,clr='#00E676')=>{
  let text = (!cmd.startsWith('@')) ?  `@TRANSMITTER: serve! --cmd transmit_cmd/${cmd}` : cmd ;
  logArr.push(text);
 
  const display = document.getElementById('console');
  let newTexts = document.createElement('p');
  newTexts.textContent = logArr[logArr.length - 1];
  newTexts.style.cssText = `
  color: ${clr};
  font-size: 13px;
  flex: 0 0 auto;
  `;
  display.appendChild(newTexts);
  display.scrollTop = display.scrollHeight;
}

const uri = "ws://127.0.0.1:8080";
const sock = new WebSocket(uri);

sock.addEventListener('open',()=>{
  logger("@CONTROL: establishing a connection/ uri & port loc -8080");
  setTimeout(()=> logger("@CONTROL: time elapsed over -2000 & ms"), 1500);
  setTimeout(()=>{ 
    logger("@CONTROL: transmitter connected successfully: err_stat=0/-return")
  },3000)
  sock.send("Hello from web");
})
sock.addEventListener('error',(err)=>{
  console.log(err);
  logger("@CONTROL_ERR: err_stat=1 on / uri & port loc -8080",'#F44336');
  setTimeout(()=>logger("@CONTROL_ERR: connection terminated -& /middle_man",'#F44336'), 2000);
})
function commander(cmd) {
  if (sock.readyState === WebSocket.OPEN) {
      sock.send(cmd);
      logger(cmd);
  } else {
    logger("@ERROR_UNEXPECTED: case_err --serve / transmit ? / -return", '#F44336');
    return;
  };
}

function cmd(key) {
  switch(key) {
    
    case 'left':
      commander(key);
      break;
      
    case 'up':
      commander(key);
      break;
      
    case 'down':
      commander(key);
      break;
      
    case 'right':
      commander(key);
      break;
    
    default:
      console.log('Awaiting click')
      logger('Active');
  }
}