/* События */
//
//
function handleButtonClick(){
    /* Событие кнопки 'Найти' */
    let modal = findOneElement('.modal') // получаем модальное окно (div)
        modal.style.display = "block" // изменяем состояние на block(блочный элемент)
        // ajax-запрос, после выполнения получаем промис
        ajaxGetData().then(response => {
            let resp = response.data // берем данные
            // проверяем аргументы, если 0 
            if (arguments == 0){
                // Вызываем ф-цию processingData() и передаем только [массив данных]
                processingData(resp.split('\n'))
            }
            else{ // // Вызываем ф-цию processingData() и передаем [массив данных] и аргумент
                processingData(resp.split('\n'), arguments[0])
            }   
        })
    };
//
function addHtml(numberStr,elem){
    //ф-ция добавляет в modal_content строки
    findOneElement('.modal_content').innerHTML +=`
                                                <p>${numberStr}</p> ${elem}<br>
                                                `
    };
//
function processingData(data, findSymbols = NaN, i = 0, count = 0){
    // Порционный вывод, выводим только искомое
    if (findSymbols){
        //console.log(findSymbols)
        //поисковый шаблон
        let regexp = new RegExp(`(\\b${findSymbols})|(\\b${findSymbols}\\d)|(\\b${findSymbols}\\-\\d\\-\\d\\-\\d)`, "gi")
        //console.log(regexp, data[count])
        //console.log(data[count].match(regexp))
        //console.log(regexp)
        for (i; i < 10; i++){
            // если шаблон совподает 
            if (regexp.test(data[count])){            
                addHtml(count, data[count])  // выводим в modal_content
                //console.log(regexp.test(data[count]), data[count])
                count++               
            }
            else{count++; continue}
        }
        //btn.value = 'Найти'
        clear = setTimeout(()=> {
            if (count < 165){
                        
                processingData(data, `${findSymbols}`, i = 0, count)
            }
            else { 
                clearTimeout(clear)
                btn.value = 'Найти'
                return}
        }, 300)
    }    
    //
    else {    
        //Порционный вывод, выводим весь syslog
        console.log(data.length)
        for (i; i < 100; i++){
            addHtml(count, data[count])
            //console.log(count)
            //console.log(count, data[count])
            count++
        }
        clear = setTimeout(()=> {
            if (count < 2000){
                        
                processingData(data, regexp = NaN, i = 0, count)
            }
            else { 
                clearTimeout(clear)
                btn.value = 'Найти'
                return}
        }, 300)
    }
};
//
//
// Обработчик события на кнопку 'Найти'
let btn = findOneElement('.inp_btn')
    btn.addEventListener('click', ()=> {
    if (btn.value == 'Найти'){        
        btn.value = 'Остановить'
        findOneElement('.modal_content').innerHTML = '' // Очищаем modal_content
        // Проверяем поле ввода 
        let inp = findOneElement('.input')
        if (inp.value == ''){ // если пустое поле
           // Вызываем ф-цию handleButtonClick() без аргементов
           handleButtonClick()
        }
        else{
            // Вызываем ф-цию handleButtonClick() с аргументом
            handleButtonClick(inp.value)
        }        
    }
    else {
        btn.value = 'Найти'
        clearTimeout(clear)
    }
});
//

