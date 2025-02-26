document.getElementById("qrForm").addEventListener("submit", function(event) {
    event.preventDefault();
    generateQRCode();
});

function generateQRCode() {
    let inputText = document.getElementById("qrText").value.trim();
    let color = document.getElementById("colorPicker").value.substring(1); // Remove '#' from color hex
    let qrImage = document.getElementById("qrImage");
    let loading = document.getElementById("loading");

    // Validate input
    if (inputText === "") {
        alert("Please enter text or a URL!");
        return;
    }

    // Format input as URL if necessary
    let formattedText = isValidUrl(inputText) ? inputText : `https://${inputText}`;

    // Show loading state
    showLoading();

    // Generate QR Code using external API
    qrImage.src = `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=${encodeURIComponent(formattedText)}&color=${color}`;
    qrImage.style.display = "block";

    // Handle QR code load and error events
    qrImage.onload = function() {
        hideLoading();
    };

    qrImage.onerror = function() {
        hideLoading();
        alert("Failed to generate QR code. Please try again.");
        qrImage.style.display = "none";
    };
}

// URL validation function
function isValidUrl(string) {
    try {
        new URL(string);
        return true;
    } catch (_) {
        return false;
    }
}

// Loading state functions
function showLoading() {
    document.getElementById("loading").style.display = "block";
}

function hideLoading() {
    document.getElementById("loading").style.display = "none";
}