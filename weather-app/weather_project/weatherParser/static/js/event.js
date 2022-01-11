//
url_summary = 'http://127.0.0.1:8000/summary/'
url_summary_date = 'http://127.0.0.1:8000/summary_date/'
//
//url_summary = 'http://192.168.220.72:8000/summary/'
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
function getAjax(url){
    ajaxRequest(url).then((summary) => {
    //
        for (let i in summary){
            let element = summary[i].split(',') // преобразуем строки в массив
            //
            addData(element[0].replace(/\s/g, ''), element[2].replace(/'/g, ''), +element[3], +element[4], element[5], element[6], element[7].slice(0,-14).replace(/'/g, ''))
        }
    });
}

//
function addData(city, description, temperature, feels_like, wind, humidity, date){
    let element = findOneElement('.table')
        element.innerHTML += `
                            <div class = "content">
                                <p>${date.slice(0, -6)}</p>
                                <p class="tr">${date.slice(-5) }</p>
                                <p class="tr">${description }</p>
                                <p class="tr">${temperature}&deg;C </p>
                                <p class="tr">Ощущается как ${feels_like}&deg;C</p>
                                <p class="tr">Ветер ${wind} м/с</p>
                                <p class="tr">Влажность ${humidity}%</p>
                            </div> <hr>`
}

/* Событие мыши */
let header = document.querySelector('.header')
    header.addEventListener('click', ()=> { // событие клик по элементу header
        let modal = document.querySelector('.modal') // получаем модальное окно (div)
            modal.style.display = "block" // изменяем состояние на block(блочный элемент)
            //
                addElement('input', '.inputDate', 'date-input1', 'date');
                addElement('input', '.inputDate', 'date-input2', 'date');
                addElement('input', '.inputDate', 'btn', 'button');
                findOneElement('.btn').value = 'Выполнить';
                // Узнаем текущ. дату
                let date = new Date
                let d = String(date.getDate())
                let m = String(date.getMonth()+1)
                let y = String(date.getFullYear())
                // Вносим в значение элемента date-input1
                //console.log(`${url_summary_date}${y+'-'+m+'-'+d}/${y+'-'+m+'-'+d}`);

            //
            getAjax(`${url_summary_date}${y+'-'+m+'-'+d}/${y+'-'+m+'-'+d}`);
            /*ajaxRequest(`${url_summary_date}${y+'-'+m+'-'+d}/${y+'-'+m+'-'+d}`).then((summary) => {
                //
                for (let i in summary){
                    let element = summary[i].split(',') // преобразуем строки в массив
                    //
                    addData(element[0].replace(/\s/g, ''), element[2].replace(/'/g, ''), +element[3], +element[4], element[5], element[6], element[7].slice(0,-14).replace(/'/g, ''))
                }
            });*/
            // Обработчик событий. Получить день, месяц и год от объекта date-input. 
            $('.btn').on('click', ()=> {
                let date1 = new Date($('.date-input1').val());
                    day1 = String(date1.getDate());
                    month1 = String(date1.getMonth() + 1);
                    year1 = String(date1.getFullYear());
                //console.log([day, month, year]);
                    //
                let date2 = new Date($('.date-input2').val());
                    day2 = String(date2.getDate());
                    month2 = String(date2.getMonth() + 1);
                    year2 = String(date2.getFullYear());
                //console.log([day, month, year]);
                findOneElement('.table').innerHTML = '' // очищаем всю таблицу
                //console.log(`${url_summary_date}${year1+'-'+month1+'-'+day1}/${year2+'-'+month2+'-'+day2}`)
                getAjax(`${url_summary_date}${year1+'-'+month1+'-'+day1}/${year2+'-'+month2+'-'+day2}`)
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
