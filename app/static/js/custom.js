document.addEventListener("DOMContentLoaded", function () {
  var form = document.getElementById("signupForm");

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    let check = true;
    var formData = new FormData(form);
    for (const [key, value] of formData) {
      console.log(`${key}: ${value}\n`);
      if (!value || value == " ") {
        check = false;
        let element = document.getElementById(`${key}`);
        element.classList.add("is-invalid");
      }
    }

    if (check) {
      fetch(form.action, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
          "X-CSRFToken": formData.csrfmiddlewaretoken, // Include the CSRF token in the headers
        },
        body: JSON.stringify(formData),
      })
        .then((res) => {
          if (res.ok) {
            return res.json();
          } else {
            throw new Error("Error: " + res.status);
          }
        })
        .then((data) => {
          console.log(data);
        })
        .catch(function (error) {
          console.log(error);
        });
    }
  });
});
