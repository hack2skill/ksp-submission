console.log("running");
const form = document.querySelector("form");
const imageContainer = document.querySelector("#image-container");
const progress = document.getElementById("lb");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  progress.innerHTML = "Searching...";

  const formData = new FormData(form);

  fetch("/", {
    method: "POST",
    body: formData,
  })
    .then((res) => res.json())
    .then((data) => {
      const image = new Image();
      image.src = data.imageURL;
      imageContainer.appendChild(image);
    });
});
