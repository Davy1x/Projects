//PASSWORD VALIDATION SECTION
var $eye = document.getElementById('input-section').querySelector('.fa-regular.fa-eye');

var $input = document.getElementById('input-section').querySelector('input');

var $screen = document.getElementById('screen');

var $copy = document.getElementById('copy');

//Password Visibility
var eyeBool = true;
var toogleEye = () =>{
  if (eyeBool) {
    $eye.classList.remove('fa-eye');
    $eye.classList.add('fa-eye-slash');
    eyeBool = !eyeBool;
    $input.type = 'password';
  } else {
    $eye.classList.remove('fa-eye-slash');
    $eye.classList.add('fa-eye');
    $input.type = 'text';
    eyeBool = !eyeBool;
  }
};
$eye.addEventListener('click', toogleEye);

//Password validation
var symbols = ['@','#','$','&','+','/','*','!','?','£','¢','€','¥','%','§','_','-'];

var alphaCap = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];

var alphaLow = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

var num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];


let messageTimeout = null;

function showMessage(msg, color = 'gray') {
  clearTimeout(messageTimeout); // cancel previous timer

  $screen.textContent = msg;
  $screen.style.color = color;
  $input.style.border = '0.08rem solid #EF5350';
  $eye.style.backgroundColor = '#EF5350';

  messageTimeout = setTimeout(() => {
    $screen.textContent = '\u200B'; // invisible char
    $input.style.border = '0.08rem solid #4840A0';
    $eye.style.backgroundColor = '#4840A0';
  }, 3000); // shorter time for better UX
}

var validate = () => {
  const nex = $input.value.split('');
  const len = $input.value.length;

  const hasSymbol = nex.some(e => symbols.includes(e));
  const hasUpper = nex.filter(l => alphaCap.includes(l)).length >= 2;
  const hasLower = nex.filter(l => alphaLow.includes(l)).length >= 2;
  const hasNumber = nex.some(z => num.includes(z));

  if (len < 10) return showMessage('At least 10 characters');
  if (!hasSymbol) return showMessage('At least 1 symbol');
  if (!hasUpper) return showMessage('At least 2 uppercases');
  if (!hasLower) return showMessage('At least 2 lowercases');
  if (!hasNumber) return showMessage('At least 1 numeric');

  clearTimeout(messageTimeout); // clear last timer
  $screen.textContent = 'Password is Valid!';
  $screen.style.color = 'gray';
  $input.style.border = '0.08rem solid #64DD17';
  $eye.style.backgroundColor = '#64DD17';
  $copy.addEventListener('click', () => {
    navigator.clipboard.writeText($input.value)
    .then($copy.innerHTML = '<i class="fa-regular fa-clipboard"></i>Copied!')
    .then($copy.style.border = '0.09rem solid #00E676')
    .then(
      setTimeout(() => {
        $copy.innerHTML = '<i class="fa-regular fa-clipboard"></i>Copy to Clipboard';
        $copy.style.border = '0.09rem solid #4840A0';
      }, 2000));
  }
  );
}

$input.addEventListener('input', validate);


//COPY TO CLIPBOARD-1


//SWITCHING PAGES-1
document.getElementById('page-2').addEventListener('click', () => {
  var validator = document.getElementById('cont-2');
  validator.style.display = 'block';
  var generator = document.getElementById('cont-1');
  generator.style.display = 'none';
  document.querySelector('.text-header h1').style.display = 'none';
});

//SWITCHING PAGES-2
document.getElementById('page-1').addEventListener('click', () => {
  var generator = document.getElementById('cont-1');
  generator.style.display = 'block';
  var validator = document.getElementById('cont-2');
  validator.style.display = 'none';
});


// PASSWORD GENERATOR


var screen = document.getElementById('screen-2');
var genBtn = document.getElementById('generate')
var copy2 = document.getElementById('copy-2');

var nummer = [1,2,3,4,5,6,7,8,9,10];
var randTime = Math.floor(Math.random() * nummer.length);
var randTimer = Number(nummer[randTime] + '000');

var justDefine = () => {
  copy2.innerHTML = '<i class="fa-regular fa-clipboard"></i>Copied!';
  copy2.style.border = '0.09rem solid #00E676';};

function passGen() {
  screen.style.border = '0.09rem solid #FBC02D';
  copy2.style.border = '0.09rem solid #4840A0';
  
  var passer = () => {
    const arr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$&?!€£";
    const $arr = Array.from({ length: 16 }, () => arr[Math.floor(Math.random() * arr.length)]);
    screen.value = $arr.join('');
  };
    
  var anime = setInterval(() => passer());
  setTimeout(() => {
    clearInterval(anime)
    screen.style.border = '0.09rem solid #00E676';
    
    copy2.addEventListener('click', () => {
      navigator.clipboard.writeText(screen.value)
      .then(justDefine)
      .then( setTimeout(() => {
        copy2.innerHTML = '<i class="fa-regular fa-clipboard"></i>Copy to Clipboard';
        copy2.style.border = '0.09rem solid #4840A0';
        screen.style.border = '0.09rem solid #4840A0';
        screen.value = '';
      }, 2000));
});
  }, randTimer);
};
genBtn.addEventListener('click', passGen);