let mediaRecorder;
let audioChunks;
let timerInterval;
let secondsElapsed = 0;

function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];

        mediaRecorder.ondataavailable = event => {
            audioChunks.push(event.data);
        };

        mediaRecorder.onstop = () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
            const file = new File([audioBlob], 'recorded.wav', { type: 'audio/wav' });

            document.getElementById('audio_file').files = createFileList(file);
        };

        mediaRecorder.start();

        // UI Changes when recording starts
        document.getElementById('startBtn').disabled = true;
        document.getElementById('stopBtn').disabled = false;
        document.getElementById('recordingStatus').style.display = 'block';
        document.getElementById('recordingStatusStopped').style.display = 'none';

        // Start Timer
        secondsElapsed = 0;
        document.getElementById('timer').innerText = formatTime(secondsElapsed);
        timerInterval = setInterval(() => {
            secondsElapsed++;
            document.getElementById('timer').innerText = formatTime(secondsElapsed);
        }, 1000);
    });
}

function stopRecording() {
    mediaRecorder.stop();

    // UI Changes when recording stops
    document.getElementById('startBtn').disabled = false;
    document.getElementById('stopBtn').disabled = true;
    document.getElementById('recordingStatus').style.display = 'none';
    document.getElementById('recordingStatusStopped').style.display = 'block';

    // Update total time
    document.getElementById('timerStopped').innerText = formatTime(secondsElapsed);

    // Stop Timer
    clearInterval(timerInterval);
    document.getElementById('timer').innerText = '';
}

function createFileList(file) {
    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(file);
    return dataTransfer.files;
}

function formatTime(seconds) {
    const min = String(Math.floor(seconds / 60)).padStart(2, '0');
    const sec = String(seconds % 60).padStart(2, '0');
    return `${min}:${sec}`;
}