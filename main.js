const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const fetch = require('node-fetch');
const bodyParser = require('body-parser');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

app.use(express.static('public'));
app.use(bodyParser.json());

let meetingTranscript = '';

io.on('connection', (socket) => {
    console.log('New client connected');

    socket.on('startMeeting', () => {
        console.log('Meeting started');
        // Here you would start the audio acquisition and transcription
    });

    socket.on('transcriptUpdate', (transcript) => {
        console.log('Transcript updated');
        meetingTranscript = transcript;
        // Here you would update the transcript on the page
    });

    socket.on('askAdvice', async () => {
        console.log('Advice asked');
        const response = await fetch('https://api.openai.com/v1/engines/davinci-codex/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer YOUR_OPENAI_API_KEY'
            },
            body: JSON.stringify({
                'prompt': meetingTranscript,
                'max_tokens': 60
            })
        });
        const data = await response.json();
        const advice = data.choices[0].text;
        // Here you would output the advice as speech using text-to-speech AI technology
        socket.emit('advice', advice);
    });

    socket.on('disconnect', () => {
        console.log('Client disconnected');
    });
});

app.get('/', (req, res) => {
    res.send('Hello World!');
});

const port = process.env.PORT || 3000;
server.listen(port, () => console.log(`Listening on port ${port}`));
