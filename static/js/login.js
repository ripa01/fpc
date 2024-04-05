
document.addEventListener("DOMContentLoaded", function() {

  const pwShowHide = document.querySelectorAll(".eye-icon");

  pwShowHide.forEach(eyeIcon => {
      eyeIcon.addEventListener("click", () => {
        
          let pwFields = eyeIcon.parentElement.querySelectorAll(".password");

          pwFields.forEach(password => {
             
              if (password.type === "password") {
                  password.type = "text";
                  eyeIcon.classList.replace("bx-hide", "bx-show");
              } else {
                  password.type = "password";
                  eyeIcon.classList.replace("bx-show", "bx-hide");
              }
          });
      });
  });
});
