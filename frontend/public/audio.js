// audio.js

let audioContext;
let mediaStream;
let mediaRecorder;
let chunks = [];

// Initialize audio context
window.onload = function () {
    audioContext = new (window.AudioContext || window.webkitAudioContext)();
};

// Start audio acquisition
document.getElementById('start-meeting').addEventListener('click', function () {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(function (stream) {
            mediaStream = audioContext.createMediaStreamSource(stream);
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();

            mediaRecorder.ondataavailable = function (e) {
                chunks.push(e.data);
                if (mediaRecorder.state == 'inactive') {
                    let blob = new Blob(chunks, { type: 'audio/wav' });
                    sendAudioToServer(blob);
                    chunks = [];
                }
            };
        })
        .catch(function (err) {
            console.log('The following error occurred: ' + err);
        });
});

// Send audio to server for transcription
function sendAudioToServer(blob) {
    let data = new FormData();
    data.append('audio', blob);

    fetch('/start', {
        method: 'POST',
        body: data
    })
        .then(response => response.json())
        .then(data => {
            socket.emit('transcriptUpdate', data.transcript);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

document.getElementById('ask-advice').addEventListener('click', function () {
    socket.emit('askAdvice');
});
