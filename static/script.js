document.getElementById("uploadForm").addEventListener("submit", function (e) {
    e.preventDefault(); // 🚨 THIS STOPS PAGE REFRESH

    const fileInput = document.getElementById("resume");
    const result = document.getElementById("result");

    if (fileInput.files.length === 0) {
        alert("Please select a file");
        return;
    }

    const formData = new FormData();
    formData.append("resume", fileInput.files[0]);

    result.textContent = "Analyzing...";

    fetch("/analyze", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        result.textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        result.textContent = "Error analyzing resume";
        console.error(error);
    });
});
