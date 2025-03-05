function openFullscreen() {
    if (document.documentElement.requestFullscreen) {
        document.documentElement.requestFullscreen();
    } else if (document.documentElement.mozRequestFullScreen) { // Firefox
        document.documentElement.mozRequestFullScreen();
    } else if (document.documentElement.webkitRequestFullscreen) { // Chrome, Safari, Opera
        document.documentElement.webkitRequestFullscreen();
    } else if (document.documentElement.msRequestFullscreen) { // IE/Edge
        document.documentElement.msRequestFullscreen();
    }
}

function closeFullscreen() {
    if (document.exitFullscreen) {
        document.exitFullscreen();
    } else if (document.mozCancelFullScreen) { // Firefox
        document.mozCancelFullScreen();
    } else if (document.webkitExitFullscreen) { // Chrome, Safari, Opera
        document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) { // IE/Edge
        document.msExitFullscreen();
    }
}



function toggleFullscreen() {
    if (document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement) {
        closeFullscreen();
    } else {
        openFullscreen();
    }
}

function handleFullscreenChange() {
    let fullscreenButton = document.getElementById("fullscreenbutton");
    console.log('screen size changed')
    if (document.fullscreenElement) {
        fullscreenButton.style.display = "none"; // Hide button in fullscreen
    } else {
        fullscreenButton.style.display = "block"; // Show button when exiting fullscreen
    }
}

document.addEventListener("DOMContentLoaded", function () {
    document.addEventListener("fullscreenchange",handleFullscreenChange)
    // let battery_code = prompt("Enter text to generate QR Code:","B3453");
    let userID = "D69009";
    let curTimestamp=new Date()-0;
    curTimestamp=Math.floor(curTimestamp/1000);
    if (userID) {
        new QRCode(document.getElementById('qrcode'), {
            text: `${userID}-${curTimestamp}`,
            width: 185,
            height: 178
        });
    }
});