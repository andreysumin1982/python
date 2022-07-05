/* Добавляем картинку */
const img = document.createElement('img');
img.src = 'static/img/postgres.png';
img.width = 100;
img.classList.add('PostgreSQL');
img.alt = 'PostgreSQL'
const header_image = findElement('.header_image');
header_image.appendChild(img);
/* ------------------------------ */

/* Добавляем TextArea */
const text = document.createElement('textarea');
text.name = 'textarea';
text.classList.add('textarea');
const content_textarea = findElement('.content_textarea');
content_textarea.appendChild(text);
/*------------------------------- */

/* Добавляем кнопки */
const button_send = document.createElement('button');
button_send.classList.add('btn_send');
button_send.innerHTML = 'Send';
button_send.style.width = '6vw';
button_send.style.height = '6vh';
/**/
const button_clear = document.createElement('button');
button_clear.classList.add('btn_clear');
button_clear.innerHTML = 'Clear';
button_clear.style.width = '6vw';
button_clear.style.height = '6vh';
/**/
const content_button = findElement('.content_button');
content_button.appendChild(button_send);
content_button.appendChild(button_clear);
/*--------------------------------*/

/*--- События на кнопки ---*/
/* Очистить */
button_clear.addEventListener('click', function () {
    text.value = '';
    let output = findElement('.content_output');
    output.innerHTML = '';
});
/* Отправить*/
button_send.addEventListener('click', function () {
    /* fetch*/
    let output = findElement('.content_output');
    fetch(url)
        .then((response) => { // Возвр. промис
            response.text()   // содержимое
                .then(data => {
                    // console.log(data)
                    output.innerHTML = `${data}`
                })
                .catch(error => {
                    console.log(error)
                    output.innerHTML = `${error}`
                })
        }) //fetch
});
/* ------------------------------ */


