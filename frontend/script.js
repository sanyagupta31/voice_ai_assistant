async function recordAudio() {
    let stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    let mediaRecorder = new MediaRecorder(stream);
    let audioChunks = [];

    mediaRecorder.ondataavailable = event => {
        audioChunks.push(event.data);
    };

    mediaRecorder.onstop = async () => {
        let audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        let formData = new FormData();
        formData.append("audio", audioBlob);

        let response = await fetch("http://127.0.0.1:5000/voice-input", {
            method: "POST",
            body: formData
        });

        let data = await response.json();
        document.getElementById("response-text").innerText = data.response;
        document.getElementById("response-audio").src = "http://127.0.0.1:5000/" + data.audio_file;
    };

    mediaRecorder.start();
    setTimeout(() => mediaRecorder.stop(), 3000);
}
