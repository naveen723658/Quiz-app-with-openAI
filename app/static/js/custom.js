document.addEventListener("DOMContentLoaded", function () {
  var form = document.getElementById("signupForm");

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    let check = true;
    var formData = new FormData(form);
    var formDataObject = {};
    for (const [key, value] of formData) {
      if (!value || value == " ") {
        check = false;
        let element = document.getElementById(`${key}`);
        element.classList.add("is-invalid");
      }
    }
    for (var pair of formData.entries()) {
      formDataObject[pair[0]] = pair[1];
    }
    if (check) {
      fetch(form.action, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
          "X-CSRFToken": formDataObject["csrfmiddlewaretoken"], // Include the CSRF token in the headers
        },
        body: JSON.stringify(formDataObject),
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
