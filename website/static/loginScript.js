const loginBtn = document.getElementById('login-button');
var key = "Stoney02";

function login() {
    const inputKey = document.getElementById('passkey').value;
    console.log(inputKey);
    if (inputKey == key) {
        window.location.href = "home.html";
    }
    else {
        var wrongPass = "<p>Incorrect Passkey. Try Again<p>";
        document.getElementById('passMsg').innerHTML = wrongPass;
    }
}
loginBtn.addEventListener('click', login);

const showPassword = document.querySelector("#show-passkey");

const passwordField = document.querySelector("#passkey");

showPassword.addEventListener("click", function(){
    this.classList.toggle("fa-eye-slash");
    this.classList.toggle("fa-eye", !this.classList.contains("fa-eye-slash")); 

    const type = passwordField.getAttribute("type") === "password" ? "text" : "password";
    passwordField.setAttribute("type", type);
})
