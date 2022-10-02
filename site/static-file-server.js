const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const { exec } = require('child_process');

app.set('port', 8080);
app.use(express.static(__dirname));
app.use(bodyParser.json());
app.post('/site.html', function (req, res) {
    exec('static_video/static_video_creation.py',
        (error, stdout, stderr) => {
            console.log(stdout);
            console.log(stderr);
            if (error !== null) {
                console.log(`exec error: ${error}`);
            }
        });
    res.redirect('back');
});
app.listen(app.get('port'), function () {
    console.log('Server started: http://localhost:' + app.get('port') + '/site.html');
});