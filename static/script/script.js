
function FilePath2(input) {
  var vidpath = input.value;
}
const fileInput = document.getElementById("fileInput");
fileInput.addEventListener("change", function() {
const file = fileInput.files[0];
const fileName = file.name;
console.log("File name: " + fileName);
fileInput = document.getElementById("fileInput");
const preview = document.getElementById("preview");
file = fileInput.files[0];
fileName = file.name;
preview.src = "{{ url_for('static', filename='{}')}}".format(fileName);
preview.style.display = "block";
});
