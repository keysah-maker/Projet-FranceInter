let int = 0;

async function play_audio() {
    if (int === 0) {
        let audio1 = document.getElementById('audio1').className;
        let audio = new Audio("/static/" + audio1);

        await audio.play();
        setTimeout(() => {
            let audio2 = document.getElementById('audio2').className;
            new Audio("/static/" + audio2).play();
        }, audio.duration * 1000);
    }
    int = 1
}

window.onclick = event => {
    play_audio()
};