let qr_changer = null;

function changeStaticQr(text){
    if (qr_changer != null){
        clearTimeout(qr_changer);
        qr_changer = null;
    }
    let qr = document.getElementById("qr_code");
    
    qr.innerHTML = "";
    new QRCode(qr, {
        text: text.value,
        width: 500,
        height: 500
    });
};



// Counter to mimic 'cnt' from Python
let cnt = 100;

// Function to pad numbers with leading zeros
function pad(num, size) {
    let s = "000" + num;
    return s.substr(s.length - size);
}

// Function to get UTC timestamp formatted as in Python
function getFormattedUTCTime() {
    const now = new Date();

    const year = now.getUTCFullYear();
    const month = pad(now.getUTCMonth() + 1, 2);
    const day = pad(now.getUTCDate(), 2);
    const hours = pad(now.getUTCHours(), 2);
    const minutes = pad(now.getUTCMinutes(), 2);
    
    const seconds = now.getUTCSeconds();
    const roundedSeconds = Math.floor(seconds / 15) * 15;
    const secondsStr = pad(roundedSeconds, 2);

    const cntStr = pad(cnt, 3);
    cnt += 1;
    if (cnt > 320) cnt = 100;

    return `${year}-${month}-${day}_${hours}:${minutes}:${secondsStr}.${cntStr}.UTC`;
}

// Main QR code generation function
function generateDynamicQRCodeImg() {
    uuid = "37b900f0-25c0-448b-825a-74d62c8ceb41"
    const timestamp = getFormattedUTCTime();
    const qrData = `${uuid}_${timestamp}`;

    // Clear previous QR code
    const qrContainer = document.getElementById("qr_code");
    qrContainer.innerHTML = "";

    // Generate new QR code
    new QRCode(qrContainer, {
        text: qrData,
        width: 500,  // similar to 21x21 box with 10 size
        height: 500,
        // colorDark: "#000000",
        // colorLight: "#ffffff",
        correctLevel: QRCode.CorrectLevel.L
    });

    qr_changer = setTimeout(generateDynamicQRCodeImg, 100);
}