// ajax-запрос получает json, создает дерево html-элементов и рисует погодный контент.
//url_json = 'http://127.0.0.1:8000/json/';
url_json = 'http://192.168.220.72:8000/json/';
//url_add_db = 'http://127.0.0.1:8000/add/';
url_add_db = 'http://192.168.220.72:8000/add/'
//
// Добавляем элементы на страницу
    addElement('div', '.header', 'weather none')
    addElement('div', '.header', 'weather date')
    addElement('div', '.header', 'weather name')
    addElement('div', '.header', 'weather icon')
    addElement('div', '.header', 'weather temp')
    addElement('div', '.header', 'weather block')
        addElement('div', '.block', 'weather description')
        addElement('div', '.block', 'weather temp2')
    addElement('div', '.header', 'weather wind')
    addElement('div', '.header', 'weather humidity')
    //Добавляем модальное окно
    addElement('div', 'body', 'modal')
        addElement('div', '.modal', 'modal_content')
            addElement('div', '.modal_content', 'inputDate')
            addElement('div', '.modal_content', 'table')
//
function getWeatherData(){
    ajaxRequest(url_json).then((weather) =>{
        //Добавляем даннае из jsonData
        findElement('.date')[0].innerHTML = `${weather.date}`
        findElement('.name')[0].innerHTML = `${weather.name}`
        findElement('.icon')[0].innerHTML = `<img src=${weather.icon} class="icon" alt="">`
        findElement('.temp')[0].innerHTML = `${weather.temp}&deg`
        findElement('.description')[0].innerHTML = `${weather.description}`
        findElement('.temp2')[0].innerHTML = `Ощущается как ${weather.feels_like}&deg`
        findElement('.wind')[0].innerHTML = `Ветер ${weather.wind} м/с`
        findElement('.humidity')[0].innerHTML = `Влажность ${weather.humidity} %`
        //console.log(`ok - Погодные данные обновлены ${time.split(' ').slice(1)}`, count++) /* Отделяем только время */
    })
};
// Вызываем ф-цию.
getWeatherData();
//
let count = 1;
//
setInterval(() =>{
    /*
        Обновляем погодные данные на странице
        Выполняется кажд. 30 мин
    */
    getWeatherData()
    //

},1800000);
//
setInterval(() =>{
    /*
        Добавляем в БД.
        Выполняется кажд. 30 мин
    */
    ajaxRequest(url_add_db).then((weather_add) => {
        console.log('ok - Погодные данные обновлены', count++)
    })
}, 1810000);