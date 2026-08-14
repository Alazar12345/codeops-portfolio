const form = document.getElementById("signupForm");
const error = document.getElementById("error");
const count = document.getElementById("count");

function updateCount() {
    const users = JSON.parse(localStorage.getItem("users")) || [];
    count.textContent = users.length;
}

updateCount();

form.addEventListener("submit", function (event) {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const phone = document.getElementById("phone").value.trim();

    error.textContent = "";

    // Validate name
    if (name.length < 2) {
        error.textContent = "Name must be at least 2 characters.";
        return;
    }

    // Validate Ethiopian phone number
    const phoneRegex = /^(09\d{8}|\+2519\d{8})$/;

    if (!phoneRegex.test(phone)) {
        error.textContent = "Enter a valid Ethiopian phone number.";
        return;
    }

    // Read existing users
    const users = JSON.parse(localStorage.getItem("users")) || [];

    // Save new user
    users.push({
        name: name,
        phone: phone
    });

    localStorage.setItem("users", JSON.stringify(users));

    // Clear form
    form.reset();

    // Update counter
    updateCount();
});