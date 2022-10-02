const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const shell = require('shelljs');

app.set('port', 8080);
app.use(express.static(__dirname));
app.use(bodyParser.json());
app.post('/site.html', function (req, res) {
    shell.exec('/static_video/static_video_creation.py')
    res.redirect('back');
});
app.listen(app.get('port'), function () {
    console.log('Server started: http://localhost:' + app.get('port') + '/site.html');
});