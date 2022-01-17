//-Ф-ции для добавления, поиска html-элементов, ajax-запрос
//
function getDateTime(){
    let date1 = new Date
        d = String(date1.getDate())
        m = String(date1.getMonth() + 1)
        y = String(date1.getFullYear())
    let timeNow = new Date().toLocaleTimeString().slice(0,-3);

    return y+'-'+m+'-'+d+'_'+timeNow;
}
//
function addElement(child, parent = 'body', classChild = 'childBody', type = NaN, text = ''){
    /*Ф-ция создает элемент на странице:
        На вход подаются 1 обязятельный элемент и 3 не обязательных:
     Дочерний (div, p, li ...), класс для дочернего элемента , родительский элемент - ('.classname'), тип дочернего элемента.
     По умолчинию все элементы создаются в теле документа body.
     */
    let childElement = document.createElement(child)
        childElement.type = type
        childElement.className = classChild
        childElement.innerHTML = text
    document.querySelector(parent).appendChild(childElement)
};
//
function findElement(className){
    /*  Ф-ция находит эдементы на странице по классу и
        возвращает массив.
    */
    return document.querySelectorAll(className) //массив объектов
};
//
function findOneElement(className){
    /*
        Ф-ция находит эдементы на странице по классу и
        возвращает массив элементов.
    */
    return document.querySelector(className) //массив объектов
};
//
function ajaxRequest(url){
    /*
        1. ajax-запрос
        2. ф-ция возвращает промис
    */
    const promise = $.ajax(url);
    return promise
};
//
//let count = 1
//let interval1 = setInterval(() =>{
    /*
        Обновляем погодные данные на странице
        выполняется кажд. 30 мин
    */
//    ajaxRequest(url_add_db).then((weather) => {
//        let time = weather.date
//        // Размещаем обновленные данные на странице
//        findElement('.date')[0].innerHTML = `${weather.date}`
//        findElement('.name')[0].innerHTML = `${weather.name}`
//        findElement('.icon')[0].innerHTML = `<img src=${weather.icon} class="icon" alt="">`
//        findElement('.temp')[0].innerHTML = `${weather.temp}`
//        findElement('.description')[0].innerHTML = `${weather.description}`
//        findElement('.temp2')[0].innerHTML = `Ощущается как ${weather.feels_like}`
//        findElement('.wind')[0].innerHTML = `Ветер ${weather.wind} м/с`
//        findElement('.humidity')[0].innerHTML = `Влажность ${weather.humidity} %`
        //

//        console.log(`ok - Погодные данные обновлены ${time.split(' ').slice(1)}`, count++) /* Отделяем только время */
//    })
//}, 1800000)
//
