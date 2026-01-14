//LOADER
const loader = document.getElementById('loader')
const overlay = document.getElementById('overlay')
const body = document.getElementById('body')
window.addEventListener('load', async () => {
  loader.style.display = 'none'
  body.style.overflowY = 'scroll'
  await sendNotification(
    "fas fa-info-circle",
    "Please click the (Add Semester) button to proceed!",
    false
  )
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


//ACTIVE ELEMENTS
const active = "linear-gradient(#3903AB,#390386)"
const computedActive = "linear-gradient(rgb(57, 3, 171), rgb(57, 3, 134))"
const inActive = "rgba( 0, 0, 0, 0)"
var globalSemesterCount = 0

//FOOTER
let closeTimeout, closeDefaultTimeout
const footer = document.getElementById('footer')
const footerDefault = footer.querySelector('i.fa-bars-staggered')
const footerDiv = footer.querySelector('div')
const deleteSemester = footer.querySelector('i.fa-trash-can')
const reset = footer.querySelector('i.fa-rotate')
const addCourse = footer.querySelector('i.fa-square-plus')
const AI = footer.querySelector('i.fa-robot')

//SEMESTERS
const semesterParent = document.getElementById('main')

//INDICATORS
const indicatorParent = document.getElementById('semester-indicator')

indicatorParent.addEventListener('click', (event) => {
  if (event.target.id.startsWith('si-')) {
    const eventId = event.target.id.split('-')[1]
    const indicatorChildren = indicatorParent.querySelectorAll('span')
    indicatorChildren.forEach((child) => {
      if (child.style.background !== inActive) {
        child.style.background = inActive
      }
    })
    event.target.style.background = active
    const semesterChildren = semesterParent.querySelectorAll('div.semester-cards')
    semesterChildren.forEach((child) => {
      if (child.style.display !== 'none') {
        child.style.display = 'none'
      }
    })
    const semesterOfTarget = document.getElementById(`sc-${eventId}`)
    semesterOfTarget.style.display = 'grid'
    isEmpty()
  }
})


//EMPTY SEMESTER
const emptySemester = document.getElementById('main-empty-container')

function isEmpty() {
  const semesterChildren = semesterParent.querySelectorAll('div.semester-cards')
  for (let c = 0; c < semesterChildren.length; c++) {
    if (semesterChildren[c].style.display === 'grid') {
      if (semesterChildren[c].children.length === 0) {
        emptySemester.style.display = 'flex'
        break
      } else {
        emptySemester.style.display = 'none'
        break
      }
    }
  }
}



//ADD SEMESTERS
const addSemester = document.getElementById('add-semester')
addSemester.addEventListener('click', () => {
  globalSemesterCount++
  createSemesterIndicator(globalSemesterCount)
})





function createSemesterIndicator(count) {
  //<span class="semester-indicator-cards">Semester 1</span>
  const indicatorChildren = indicatorParent.querySelectorAll('span')
  indicatorChildren.forEach((child) => {
    if (child.style.background !== inActive) {
      child.style.background = inActive
    }
  })
  const span = document.createElement('span')
  span.className = "semester-indicator-cards"
  span.id = `si-${count}`
  span.textContent = `Semester ${count}`
  span.style.background = active
  indicatorParent.appendChild(span)
  createSemesterCards(count)
  indicatorParent.scrollTo({
    left: indicatorParent.scrollWidth,
    behavior: 'smooth'
  })
}

function createSemesterCards(count) {
  // <div class="semester-cards"></div>
  const semesterChildren = semesterParent.querySelectorAll('div.semester-cards')
  semesterChildren.forEach((child) => {
    if (child.style.display !== 'none') {
      child.style.display = 'none'
    }
  })
  const div = document.createElement('div')
  div.className = "semester-cards"
  div.id = `sc-${count}`
  div.style.display = 'grid'
  div.onclick = (event) => {
    const eve = event.target
    if (eve.className === 'fas fa-trash') {
      div.removeChild(eve.parentElement)
      if (div.children.length === 0) isEmpty()
    }
  }
  semesterParent.appendChild(div)
  isEmpty()
}

function createCourseCards(parentId) {
  /*
      <div class="course-cards">
        <i class="fas fa-trash"></i>
        <input type="text" placeholder="Course">
        <div>
          <select>
            <option value="A">A</option>
            <option value="B">B</option>
            <option value="C">C</option>
            <option value="D">D</option>
            <option value="E">E</option>
            <option value="F">F</option>
          </select>
          <input type="number" placeholder="Credit">
        </div>
      </div>
  */
  const mainDiv = document.createElement('div')
  mainDiv.className = "course-cards"
  const i = document.createElement('i')
  i.className = "fas fa-trash"
  const input = document.createElement('input')
  input.type = "text"
  input.placeholder = "Course"
  
  const innerDiv = document.createElement('div')
  const select = document.createElement('select')
  const opt1 = document.createElement('option')
  opt1.value = "5.0"
  opt1.textContent = "A"
  const opt2 = document.createElement('option')
  opt2.value = "4.0"
  opt2.textContent = "B"
  const opt3 = document.createElement('option')
  opt3.value = "3.0"
  opt3.textContent = "C"
  const opt4 = document.createElement('option')
  opt4.value = "2.0"
  opt4.textContent = "D"
  const opt5 = document.createElement('option')
  opt5.value = "1.0"
  opt5.textContent = "E"
  const opt6 = document.createElement('option')
  opt6.value = "0.0"
  opt6.textContent = "F"
  const innerInput = document.createElement('input')
  innerInput.type = "number"
  innerInput.placeholder = "Credit"
  
  select.append(opt1, opt2, opt3, opt4, opt5, opt6)
  innerDiv.append(select, innerInput)
  mainDiv.append(i, input, innerDiv)
  document.getElementById(parentId).appendChild(mainDiv)
}






deleteSemester.addEventListener(('click'), async () => {
  if (indicatorParent.children.length === 0) return
  await sendNotification(
    "fas fa-trash-can",
    "Are you sure you want to delete the current semester & courses attached to it, This process can not be undone!",
    true
  ).then((res) => {
    if (res === 'accept') {
      const indicatorChildren = () => indicatorParent.querySelectorAll('span')
      for (let i = 0; i < indicatorChildren().length; i++) {
        
        const child = indicatorChildren()[i]
        const coChild = document.getElementById(`sc-${child.id.split('-')[1]}`)
        
        if (child.style.background === computedActive) {
          indicatorParent.removeChild(child)
          semesterParent.removeChild(coChild)
          if (indicatorChildren()[i]) {
            indicatorChildren()[i].style.background = active
            document.getElementById(`sc-${indicatorChildren()[i].id.split('-')[1]}`).style.display = 'grid'
            
          } else if (indicatorChildren()[i - 1]) {
            indicatorChildren()[i - 1].style.background = active
            document.getElementById(`sc-${indicatorChildren()[i - 1].id.split('-')[1]}`).style.display = 'grid'
          }
          isEmpty()
          if (indicatorChildren().length === 0) {
            globalSemesterCount = 0
            emptySemester.style.display = 'none'
            break
          }
        }
      }
    }
  })
})

reset.addEventListener(('click'), async () => {
  if (indicatorParent.children.length === 0) return
  await sendNotification(
    "fas fa-rotate",
    "The current process will wipe all semesters & courses attached to them, This process can not be undone!",
    true
  ).then(async (res) => {
    if (res === 'accept') {
      indicatorParent.querySelectorAll('span').forEach((child) => {
        indicatorParent.removeChild(child)
      })
      semesterParent.querySelectorAll('div.semester-cards').forEach((child) => {
        semesterParent.removeChild(child)
      })
      globalSemesterCount = 0
      emptySemester.style.display = 'none'
      await sendNotification(
        "fas fa-circle-check",
        "Progress has been reset successfully!",
        false
      )
    }
  })
})

addCourse.addEventListener(('click'), () => {
  if (indicatorParent.children.length === 0) return
  const indicatorChildren = indicatorParent.querySelectorAll('span')
  indicatorChildren.forEach((child) => {
    if (child.style.background === computedActive) {
      const childId = child.id.split('-')[1]
      createCourseCards(`sc-${childId}`)
      isEmpty()
      const newSem = document.getElementById(`sc-${childId}`)
      newSem.scrollTo({
        top: newSem.scrollHeight,
        behavior: 'smooth'
      })
    }
  })
})

AI.addEventListener(('click'), () => {
  
})


footer.addEventListener('click', () => {
  clearTimeout(closeTimeout)
  clearTimeout(closeDefaultTimeout)
  footerDefault.style.display = 'none'
  footer.style.width = '260px'
  footerDiv.style.opacity = '1'
  closeTimeout = setTimeout(() => {
    footer.style.width = '50px'
    footerDiv.style.opacity = '0'
    closeDefaultTimeout = setTimeout(() => footerDefault.style.display = 'flex', 400)
  }, 4000)
})