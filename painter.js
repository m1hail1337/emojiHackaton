let previousEyesItem;
let previousShapesItem;
let previousMouthesItem;


function changeEyes(item) {

    eyesContext.clearRect(0, 0, canvas.width, canvas.height);
    

    let img = document.getElementById(item.id);
    item.className = "Selected";
    img.crossOrigin = "anonymous";
    if (previousEyesItem != null)
        previousEyesItem.className = "";

    previousEyesItem = item;
    // Привязываем функцию к событию onload
    // Это указывает браузеру, что делать, когда изображение загружено
    eyesContext.drawImage(img, 0, 0);
}

function changeShapes(item) {

    shapesContext.clearRect(0, 0, canvas.width, canvas.height);
    
    let img = document.getElementById(item.id);
    item.className = "Selected";
    img.crossOrigin = "anonymous";
    if (previousShapesItem != null)
        previousShapesItem.className = "";

    previousShapesItem = item;
    // Привязываем функцию к событию onload
    // Это указывает браузеру, что делать, когда изображение загружено
    shapesContext.drawImage(img, 0, 0);
}

function changeMouthes(item) {
    mouthesContext.clearRect(0, 0, canvas.width, canvas.height);
    
    let img = document.getElementById(item.id);
    item.className = "Selected";
    img.crossOrigin = "anonymous";
    if (previousMouthesItem != null)
        previousMouthesItem.className = "";

    previousMouthesItem = item;
    // Привязываем функцию к событию onload
    // Это указывает браузеру, что делать, когда изображение загружено
    mouthesContext.drawImage(img, 0, 0);
}
