let previousEyesItem;

function setEyes(adress, element) {
    let img = document.getElementById("eyes"+adress);
    element.className = "Selected";
    img.crossOrigin = "anonymous";
    if (previousEyesItem != null)
        previousEyesItem.className = "";

    previousEyesItem = element;
    // Привязываем функцию к событию onload
    // Это указывает браузеру, что делать, когда изображение загружено
    context.drawImage(img, 10, 10);


    // Загружаем файл изображения

    console.log("heeeeeeeeeeeeee")
}