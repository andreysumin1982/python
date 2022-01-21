//
//url_summary_date = 'http://127.0.0.1:8000/summary_date/';
//
//url_deleteIdSummary = 'http://127.0.0.1:8000/deleteIdSummary/';
//
url_summary_date = 'http://192.168.220.72:8000/summary_date/'
//
url_deleteIdSummary = 'http://192.168.220.72:8000/deleteIdSummary/'
//
//
let listIdSummary = []  // массив для id id_summary
let objIdCheckBox = {}  // словарь для соответствия id и обьектов checkbox
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
                findOneElement(`.check-box`).id = 'box'
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
function getAjax(url){
    /*Ф-ция обрабатывает промис, полученный из ф-ции ajaxRequest()*/

        // Обнуляем
        listIdSummary = [] //
        objIdCheckBox = {}
        //
    ajaxRequest(url).then((summary) => {
        let l = 0
        for (let i in summary){
            let element = summary[i].split(',') // преобразуем строки в массив
            //
            //console.log(element)
            addData(element[0], element[3].replace(/'/g, ''), +element[4], +element[5], element[6], element[7], element[8].slice(0,-14).replace(/'/g, ''))
            //
            listIdSummary.push(element[0]) // Добавляем id_summary в массив
            objIdCheckBox[listIdSummary[l]] = findElement('.check-box')[l]
            l++
        }
        //console.log(listIdSummary)
    }); // end ajaxRequest
};
//
//function addId(){
//    // Обнуляем
//    //objIdCheckBox = {}
//    //console.log(listIdSummary)
//    for (let i=0; i < listIdSummary.length; i++){ // Заполняем объект. {id_summary: checkbox}
//            console.log(document.getElementById('#box'))
//            //objIdCheckBox[listIdSummary[i]] = findElement('#box')[i]
//        }
//};
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
                console.log(getValuesDate('.date-input1'))
                /* ajax-запрос, выводим данные за текущий день*/
                getAjax(`${url_summary_date}${getValuesDate()}/${getValuesDate()}`);

                //console.log(listCheckBox)

            // Обработчик собыия кнопки 'Выполнить'
            document.querySelector('.btn').addEventListener('click', ()=> {
                findOneElement('.table').innerHTML = '' // очищаем всю таблицу
                /* ajax-запрос, выводим данные в контент за выбранные дни */
                getAjax(`${url_summary_date}${getValuesDate('.date-input1')}/${getValuesDate('.date-input2')}`);
                //

            });
            // Обработчик собыия кнопки 'Удалить'
            document.querySelector('.inputBtn').addEventListener('click',()=> {
                    console.log(objIdCheckBox)
                    let objBox = objIdCheckBox
                    let lst = Object.keys(objBox)
                    //console.log(lst)
                    for (let elem of lst) {
                        //console.log(elem, objIdCheckBox[elem])
                        if (objBox[elem].checked == true){
                            console.log(elem, objBox[elem])
                            ajaxRequest(`${url_deleteIdSummary}${elem}`).then((summary) => {
                                console.log('Удален id: ', elem)
                            })
                        }
                    }

                           //alert('Необходимо выбрать элемент(ы)!')
                        findOneElement('.table').innerHTML = '' // очищаем всю таблицу
                          // если не выбран временной интервал, ввыводим данные за текущий день
                        if (getValuesDate('.date-input1') == 'NaN-NaN-NaN'){
                            getAjax(`${url_summary_date}${getValuesDate()}/${getValuesDate()}`);
                        }
                        else{
                            // иначе, выводим данные в контент за выбранные дни
                            getAjax(`${url_summary_date}${getValuesDate('.date-input1')}/${getValuesDate('.date-input2')}`)
                        }
            })

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