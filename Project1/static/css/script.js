const password = document.getElementById('pass')
const con_password = document.getElementById('confirm_password')
const message = document.getElementById('pass_message')

console.log('first stage')
function validatePassword(){
    if (con_password == ''){
        message.textContent = ''
    }else if(password.value === con_password.value){
        message.textContent = 'Password is a match!'
        message.style.color = 'lightgreen'
        console.log('second')
    }else if(password & con_password  === '' ){
        message.textContent = 'Password cannot be empty!'
    }
    else{
        message.textContent = 'Password do not match!'
        message.style.color = 'red'
        console.log('second')
    }
}

con_password.addEventListener('input', validatePassword)