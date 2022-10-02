var express = require('express'),
    app = express();
var bodyParser = require('body-parser');
app.set('port', 8080);
app.use(express.static(__dirname));
app.use(bodyParser.json());
app.post('/site.html', function (req, res) {
    console.log(req.body);
    // res.redirect('site.html');
    res.redirect('back');
});
app.listen(app.get('port'), function () {
    console.log('Server started: http://localhost:' + app.get('port') + '/site.html');
});