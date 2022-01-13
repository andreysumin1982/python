//
url_summary_date = 'http://127.0.0.1:8000/summary_date/'
//
//url_summary_date = 'http://192.168.220.72:8000/summary_date/'
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
function findOneElement(className){
    /*
        Ф-ция находит эдементы на странице по классу и
        возвращает массив элементов.
    */
    return document.querySelector(className) //массив объектов
};
//
function addData(
    /* Ф-ция создает html-дерево из входных аргументов*/
                id_city,
                description,
                temperature,
                feels_like,
                wind,
                humidity,
                date){
    let element = findOneElement('.table')
        element.innerHTML += `
                            <div class = "content">
                                <p>${id_city}</p>
                                <p>${date.slice(0, -6)}</p>
                                <p class="tr">${date.slice(-5) }</p>
                                <p class="tr">${description }</p>
                                <p class="tr">${temperature}&deg;C </p>
                                <p class="tr">Ощущается как ${feels_like}&deg;C</p>
                                <p class="tr">Ветер ${wind} м/с</p>
                                <p class="tr">Влажность ${humidity}%</p>
                            </div> <hr>`
}
//
function getValuesDate(){
    /* Ф-ция возвращает строку:
        1: если нет аргументов - текущую дату
        2: иначе - дату, выбранную из элемента <input type="date">  */
    if (arguments.length != 0){
        let date1 = new Date($(arguments[0]).val())
            d = String(date1.getDate())
            m = String(date1.getMonth() + 1)
            y = String(date1.getFullYear())
        return y+'-'+m+'-'+d;
    }
    else{
        let date1 = new Date
            d = String(date1.getDate())
            m = String(date1.getMonth() + 1)
            y = String(date1.getFullYear())
        return y+'-'+m+'-'+d;
    }
}
//
function getAjax(url){
    /*Ф-ция обрабатывает промис, полученный из ф-ции ajaxRequest()*/
    ajaxRequest(url).then((summary) => {
    //
        for (let i in summary){
            let element = summary[i].split(',') // преобразуем строки в массив
            //
            console.log(element)
            addData(element[0], element[3].replace(/'/g, ''), +element[4], +element[5], element[6], element[7], element[8].slice(0,-14).replace(/'/g, ''))
        }
    });
}
//

/* Обработчик события мыши на погодный контент  */
let content = document.querySelector('.header')
    content.addEventListener('click', ()=> { // событие клик по элементу header
        let modal = document.querySelector('.modal') // получаем модальное окно (div)
            modal.style.display = "block" // изменяем состояние на block(блочный элемент)
            //
                addElement('input', '.inputDate', 'date-input1', 'date'); // добавляем input .date-input1
                addElement('input', '.inputDate', 'date-input2', 'date'); // добавляем input .date-input2
                addElement('input', '.inputDate', 'btn', 'button');       // добавляем button .btn
                findOneElement('.btn').value = 'Выполнить';
                //console.log(getValuesDate('.date-input1'))
                /* ajax-запрос, выводим данные за текущий день*/
                getAjax(`${url_summary_date}${getValuesDate()}/${getValuesDate()}`);
            // Обработчик собыия кнопки .
            $('.btn').on('click', ()=> {
                findOneElement('.table').innerHTML = '' // очищаем всю таблицу
                /* ajax-запрос, выводим данные за определенные дни */
                getAjax(`${url_summary_date}${getValuesDate('.date-input1')}/${getValuesDate('.date-input2')}`);
            });
        //
        window.onclick = function(event){ // клик, кроме контентного окна.
        //console.log(event)
        if (event.target == modal){ // если клик по модальному окну (div .modal)
            modal.style.display = "none" // убираем контентное окно и изменяем состояние модального окна на "none"
            findOneElement('.table').innerHTML = '' // очищаем всю таблицу
            findOneElement('.inputDate').innerHTML = '' // очищаем весь div
        }
    };
})
//