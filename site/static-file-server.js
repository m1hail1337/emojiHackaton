const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const { exec } = require('child_process');

app.set('port', 8080);
app.use(express.static(__dirname));
app.use(bodyParser.json());
app.post('/site.html', function (req, res) {
    res.redirect('back');
});
app.listen(app.get('port'), function () {
    console.log('Server started: http://localhost:' + app.get('port') + '/site.html');
});