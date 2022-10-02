let isDrawing;
let canvas;
let context;
let layerShapes;
let layerMouthes;
let layerEyes;
let previousThicknessElement;
let previousColorElement;

window.onload = function() {
      canvas = document.getElementById("drawingCanvas");
      context = canvas.getContext("2d");
      shapesContext = document.getElementById("layerShapes").getContext("2d");
	  eyesContext = document.getElementById("layerEyes").getContext("2d");
	  mouthesContext = document.getElementById("layerMouthes").getContext("2d");
   }

function clearCanvas() {
	context.clearRect(0, 0, canvas.width, canvas.height);
	shapesContext.clearRect(0, 0, canvas.width, canvas.height);
	eyesContext.clearRect(0, 0, canvas.width, canvas.height);
	mouthesContext.clearRect(0, 0, canvas.width, canvas.height);
	previousEyesItem = null;
	previousShapesItem = null;
	previousMouthesItem = null;
}

function saveCanvas() {
    // Находим элемент <img>
	let imageCopy = document.getElementById("savedImageCopy");
	context.drawImage(document.getElementById(previousShapesItem.id),0,0);
	context.drawImage(document.getElementById(previousEyesItem.id),0,0);
	context.drawImage(document.getElementById(previousMouthesItem.id),0,0);
	context.drawImage(canvas,0,0);
	// Отображаем данные холста в элементе <img>
	imageCopy.src = canvas.toDataURL();
	
	// Показываем элемент <div>, делая изображение видимым
	// делая изображение видимым
	let imageContainer = document.getElementById("savedCopyContainer");
    imageContainer.style.display = "block";
	let video = document.getElementById("video");
	video.height = 0;
}

function cutPicture() {
	let video = document.getElementById("video");
	video.height = 175;
	let imageContainer = document.getElementById("savedCopyContainer");
	let imageCopy = document.getElementById("savedImageCopy");
    imageContainer.style.display = "none";
	imageCopy.src = "";
}