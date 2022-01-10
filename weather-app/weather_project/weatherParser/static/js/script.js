/*Создание ajax-запросов GET/POST, промисы */
url_update = 'http://127.0.0.1:8000/json/' /* Обновление погодных данных */
url_add_db = 'http://127.0.0.1:8000/add/' /* Внесение погодных данных в БД MSSQL */
//
function findElement(className){
    /*  Ф-ция находит эдемент(ы) на странице по классу и
        возвращает массив.
    */
    return document.querySelectorAll(className) //массив объектов
};
//
function ajaxRequest(url){
    /*
        1. ajax-запрос
        2. ф-ция возвращает промис
    */
    const promise = $.ajax(url);
    return promise
}
//
setInterval(() =>{
    /*
        Обновляем погодные данные на странице
        выполняется кажд. 30 мин
    */
    ajaxRequest(url_update).then((weather) => {
        let time = weather.date
        // Размещаем обновленные данные на странице
        findElement('.date')[0].innerHTML = `${weather.date}`
        findElement('.name')[0].innerHTML = `${weather.name}`
        findElement('.icon')[0].innerHTML = `<img src=${weather.icon} class="icon" alt="">`
        findElement('.temp')[0].innerHTML = `${weather.temp}`
        findElement('.description')[0].innerHTML = `${weather.description}`
        findElement('.temp2')[0].innerHTML = `Ощущается как ${weather.feels_like}`
        findElement('.wind')[0].innerHTML = `Ветер ${weather.wind} м/с`
        findElement('.humidity')[0].innerHTML = `Влажность ${weather.humidity} %`
        //
        console.log(`ok - Погодные данные обновлены ${time.split(' ').slice(1)}`) /* Отделяем только время */

    })

}, 900000);
//
setInterval(() =>{
    /*
        Вносим обновления в БД
        выполняется кажд. 30 мин
    */
    ajaxRequest(url_add_db).then((weather) => {
        let time = weather.date
            console.log(`ok - Погодные данные внесены ${time.split(' ').slice(1)}`)
    })
}, 900000);