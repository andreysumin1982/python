//
//url_summary_date = 'http://127.0.0.1:8000/summary_date/'
//
//url_deleteIdSummary = 'http://127.0.0.1:8000/deleteIdSummary/'
//
url_summary_date = 'http://192.168.220.72:8000/summary_date/'
//
url_deleteIdSummary = 'http://192.168.220.72:8000/deleteIdSummary/'
//
let k = 1 // счетчик
function addData(
    /* Ф-ция создает html-дерево из входных аргументов*/
                id_summary,
                description,
                temperature,
                feels_like,
                wind,
                humidity,
                date)
        {
        String(k)
        addElement('div', '.table', `content cont${k}`)
            addElement('input', `.cont${k}`, 'check-box', 'checkbox')
            //
            addElement('p', `.cont${k}`, `id_summary${k}`)
                findOneElement(`.id_summary${k}`).innerHTML = `${id_summary}`
                findOneElement(`.id_summary${k}`).style.display = 'none'
            addElement('p', `.cont${k}`, `p_date${k}`)
                findOneElement(`.p_date${k}`).innerHTML = `${date.slice(0, -6)}`
            addElement('p', `.cont${k}`, `tr p_time${k}`)
                findOneElement(`.p_time${k}`).innerHTML = `${date.slice(-5)}`
            addElement('p', `.cont${k}`, `tr p_description${k}`)
                findOneElement(`.p_description${k}`).innerHTML = `${description}`
            addElement('p', `.cont${k}`, `tr p_temperature${k}`)
                findOneElement(`.p_temperature${k}`).innerHTML = `${temperature}&deg`
            addElement('p', `.cont${k}`, `tr p_feels_like${k}`)
                findOneElement(`.p_feels_like${k}`).innerHTML = `Ощущается как ${feels_like}&deg`
            addElement('p', `.cont${k}`, `tr p_wind${k}`)
                findOneElement(`.p_wind${k}`).innerHTML = `Ветер ${wind} м/с`
            addElement('p', `.cont${k}`, `tr p_humidity${k}`)
                findOneElement(`.p_humidity${k}`).innerHTML = `Влажность ${humidity}%`

            //findOneElement(`.cont${k}`).innerHTML += '<hr>'
        Number(k)
        k++
};
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
let listIdSimmary = []  // массив для id id_summary
let objIdCheckBox = {}  // словарь для соответствия id и обьектов checkbox
let delIdSummary =  {}  // словарь для элементов на удаление
function getAjax(url){
    /*Ф-ция обрабатывает промис, полученный из ф-ции ajaxRequest()*/

        // Обнуляем
        listIdSimmary = [] //
        objIdCheckBox = {} //
        delIdSummary = {} //
        //
    ajaxRequest(url).then((summary) => {
        for (let i in summary){
            let element = summary[i].split(',') // преобразуем строки в массив
            //
            //console.log(element)
            listIdSimmary.push(element[0]) // Добавляем id_summary в массив
            addData(element[0], element[3].replace(/'/g, ''), +element[4], +element[5], element[6], element[7], element[8].slice(0,-14).replace(/'/g, ''))
        }
            //
        for (let i=0; i < listIdSimmary.length; i++){ // Заполняем объект. {id_summary: checkbox}
            objIdCheckBox[listIdSimmary[i]] = findElement('.check-box')[i]
        }
            // Иде по массиву checkbox
        for (let j =0; j < findElement('.check-box').length; j++){
            let checkElements = findElement('.check-box') //
            checkElements[j].addEventListener('click', ()=> { // обработчик события клик на checkbox.
                if (checkElements[j].checked == true && (checkElements[j] == objIdCheckBox[listIdSimmary[j]])) { // проверяем, есть ли элемент в словаре(объекте)
                    //console.log(listIdSimmary[j], objIdCheckBox[listIdSimmary[j]]); // выводим ключ, значение.
                    delIdSummary[listIdSimmary[j]] = listIdSimmary[j];//добавляем id_summary в объект
                    console.log(delIdSummary);
                }
                else{
                    delete delIdSummary[listIdSimmary[j]]; // если checked = falce, убираем из объекта id_summary
                    //console.log(delIdSummary);
                }
            })
        }
    }); // end ajaxRequest
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
                addElement('input', '.inputDate', 'inputBtn', 'button');
                    findOneElement('.inputBtn').value = 'Удалить';
                    findOneElement('.inputBtn').checked = false;
                //console.log(getValuesDate('.date-input1'))
                /* ajax-запрос, выводим данные за текущий день*/
                getAjax(`${url_summary_date}${getValuesDate()}/${getValuesDate()}`);
                //console.log(listCheckBox)
            // Обработчик собыия кнопки 'Выполнить'
            $('.btn').on('click', ()=> {
                findOneElement('.table').innerHTML = '' // очищаем всю таблицу
                /* ajax-запрос, выводим данные в контент за определенные дни */
                getAjax(`${url_summary_date}${getValuesDate('.date-input1')}/${getValuesDate('.date-input2')}`);
                //
            });
            // Обработчик собыия кнопки 'Удалить'
            $('.inputBtn').on('click', ()=> {
                if (Object.keys(delIdSummary).length != 0){
                    for (let key in delIdSummary){
                        console.log(String(key))
                        getAjax(`${url_deleteIdSummary}${String(key)}`);
                    }
                }
                else{ alert('Необходимо выбрать элемент(ы)!')}
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