//
url_summary = 'http://127.0.0.1:8000/summary/'
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
function addData(city, description, temperature, feels_like, wind, humidity, date){
    let element = findOneElement('.table')
        element.innerHTML += `
                            <div class = "content">
                                <div>${date.slice(0, -6)}</div>
                                <div class="tr">${date.slice(-5) }</div>
                                <div class="tr">${description }</div>
                                <div class="tr">${temperature}&deg;C </div>
                                <div class="tr">Ощущается как ${feels_like}&deg;C</div>
                                <div class="tr">Ветер ${wind} м/с</div>
                                <div class="tr">Влажность ${humidity}%</div>
                            </div> <hr>`
}

/* Событие мыши */
let header = document.querySelector('.header')
    header.addEventListener('click', ()=> { // событие клик по элементу header
        let modal = document.querySelector('.modal') // получаем модальное окно (div)
            modal.style.display = "block" // изменяем состояние на block(блочный элемент)
        //
        let modalContent = document.querySelector('.modal_content') //получаем контентную часть (окно div)
            //modalContent.innerHTML = "Получаем модальное окно" //
                // События, модальное окно, вывод погодных данных
                findOneElement('.table').innerHTML = '' // очищаем всю таблицу
                ajaxRequest(url_summary).then((summary) => {
                        //console.log(`ok -  ${summary}`)

                        for (let i in summary){
                            let element = summary[i].split(',') // преобразуем строки в массив
                            //
                            addData(element[0].replace(/\s/g, ''), element[2].replace(/'/g, ''), +element[3], +element[4], element[5], element[6], element[7].slice(0,-14).replace(/'/g, ''))
                        }
                });
        //
        window.onclick = function(event){ // клик, кроме контентного окна.
        //console.log(event)
        if (event.target == modal){ // если клик по модальному окну (div .modal)
            modal.style.display = "none" // убираем контентное окно и изменяем состояние модального окна на "none"
        }
    };
})
