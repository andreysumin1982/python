///* События */
////
////
//function handleButtonClick(){
//    /* Событие кнопки 'Найти' */
//    let modal = findOneElement('.modal') // получаем модальное окно (div)
//        modal.style.display = "block" // изменяем состояние на block(блочный элемент)
//        // ajax-запрос, после выполнения получаем промис
//        ajaxGetData().then(response => {
//            let resp = response.data // берем данные
//            console.log(resp)
//            // проверяем аргументы, если 0
//            if (arguments == 0){
//                // Вызываем ф-цию processingData() и передаем только [массив данных]
//                processingData(resp.split('\n'))
//            }
//            else{ // // Вызываем ф-цию processingData() и передаем [массив данных] и аргумент
//                processingData(resp.split('\n'), arguments[0])
//            }
//        })
//    };
////
//function addHtml(elem){
//    //ф-ция добавляет в modal_content строки
//    findOneElement('.modal_content').innerHTML +=`
//                                                ${elem}<br>
//                                                `
//    };
////
//// Посчитать проценты (доделать)
////let x = 20
////for (let i = 1; i < x+1; i++){
////    let s = i/x*100
////    console.log(i, s+'%')
////}
////
//function loadSummary(loadCount, data){
//    // Ф-ция считат процентное соотношение
//    //let sum = loadCount/data*100
//    //console.log('sum :',  Math.round(sum))
//    return Math.round(loadCount/data*100)
//}
////
//function processingData(data, findSymbols = NaN, i = 0, count = 0){
//    // Порционный вывод, выводим только искомое
//    n = 1000
//    if (findSymbols){ // если есть искомый аргумент(findSymbols)
//        // шаблон поиска
//        let regexp = new RegExp(`(\\b${findSymbols})|(\\b${findSymbols}\\d)|(\\b${findSymbols}\\-\\d\\-\\d\\-\\d)`, "gi")
//        for (i; i < 10; i++){
//            // если шаблон есть в искомой строке
//            if (regexp.test(data[count])){
//                addHtml(data[count])  // выводим в modal_content
//                //console.log(regexp.test(data[count]), data[count])
//                count++
//            }
//            else{count++; continue} // иначе продолжаем бежать по циклу
//        }
//        //btn.value = 'Найти'
//        clear = setTimeout(()=> {
//            if (count < n){ //
//                //
//                load = loadSummary(count, n) // считаем проценты
//                    findOneElement('.p_loading').innerHTML = `Идет поиск ${load}%` // выводим
//                //
//                processingData(data, `${findSymbols}`, i = 0, count) // рекурсивно вызываем с вх. аргументами
//            }
//            else {
//                load = loadSummary(count, n)
//                    findOneElement('.p_loading').innerHTML = `Выполнено ${load}%` //выводим
//                //
//                clearTimeout(clear) // отменяем вызов ф-ции setTimeout
//                btn.value = 'Найти'
//                return}
//        }, 300)
//    }
//    //
//    else {
//        //Порционный вывод, выводим весь syslog
//        for (i; i < 10; i++){
//            addHtml(data[count]) // выводим по 10 строк.
//            count++
//        }
//        clear = setTimeout(()=> {
//            if (count < n){ //
//                //
//                //console.log(count)
//                load = loadSummary(count, n) // считаем проценты
//                    findOneElement('.p_loading').innerHTML = `Идет поиск ${load}%` // выводим
//                //
//                processingData(data, regexp = NaN, i = 0, count) // рекурсивно вызываем с вх. аргументами
//
//            }
//            else { // иначе, считаем проценты,
//                load = loadSummary(count, n)
//                    findOneElement('.p_loading').innerHTML = `Выполнено ${load}%` //выводим
//                //
//                clearTimeout(clear) // отменяем вызов ф-ции setTimeout
//                btn.value = 'Найти'
//                return}
//        }, 300)
//    }
//};
////
//
//// Обработчик события на кнопку 'Найти'
//let btn = findOneElement('.inp_btn')
//    btn.addEventListener('click', ()=> {
//    if (btn.value == 'Найти'){
//        btn.value = 'Остановить'
//        findOneElement('.modal_content').innerHTML = '' // Очищаем modal_content
//        // Проверяем поле ввода
//        let inp = findOneElement('.input')
//        if (inp.value == ''){ // если пустое поле
//           // Вызываем ф-цию handleButtonClick() без аргементов
//           handleButtonClick()
//        }
//        else{
//            // Вызываем ф-цию handleButtonClick() с аргументом
//            handleButtonClick(inp.value)
//        }
//    }
//    else {
//        clearTimeout(clear)
//            findOneElement('.p_loading').innerHTML = 'Остановлено на '+ load + '%' //выводим
//            btn.value = 'Найти'
//    }
//});
////

//
function addHtml(dataOutput) {
    //ф-ция добавляет в modal_content промис
    findOneElement('.modal_content').innerHTML = `<pre>${dataOutput}<br>`
};
//
//function dataProcessing(data){
//    //let len = data.length
//    let count = 0
//    //
//    for (let i=0; i<80; i++){
//        if (data[count] != undefined){
//            setTimeout(function () {
//                addHtml(data[count]) // выводим в modal_content
//                count++
//            }, 100);
//        }
//    }
//    btn.value = 'Найти' // возвращаем название кнопки
//};
//
// Обработчик события на кнопку 'Найти'
let btn = findOneElement('.inp_btn')
btn.addEventListener('click', () => {
    if (btn.value == 'Найти') {
        btn.value = 'Остановить'
        findOneElement('.modal_content').innerHTML = '' // Очищаем modal_content
        // Проверяем поле ввода
        let inp = findOneElement('.input')
        if (inp.value == '') { // если пустое поле ?!
            //ajax-запрос, после выполнения получаем промис
            ajaxGetData()
                .then(response => {
                    //console.log(response)
                    // передаем промис в обработку
                    response.text().then(data => {
                        addHtml(data)
                    })
                })
                .catch(error => {    //ошибки
                    console.log(error)
                    addHtml(error)
                });
            btn.value = 'Найти'; return
        }
        else {
            //ajax-запрос, после выполнения получаем промис
            ajaxSerchData(inp.value)
                .then(response => {
                    //console.log(response)
                    // передаем промис в обработку
                    response.text().then(data => {
                        if (data.length > 0) {
                            addHtml(data)
                        }
                        else { addHtml('Ничего не найдено.') }
                    })
                })
                .catch(error => {    //ошибки
                    console.log(error)
                    addHtml(error)
                });
            btn.value = 'Найти'; return
        }
    }
    else {
        clearTimeout(timer)
        btn.value = 'Найти'
    }
});
// Добавляем архивные файлы в элемент <select>..</select>
let selectBtn = document.querySelector('.archives')
addZipFiles().then(response => {
    /*
    * Ф -цая создает дочерние элементы в теге <select>
    * добавляем имя файла каждому элемету 
    */
    //console.log(response)
    response.text().then(data => {
        count = 0 // 
        for (let item of data.split('\n')) { // бежим по массиву с именами файлов
            if (item == '') { // Проверяем пробелы 
                continue
            }
            else {
                addElement('option', '.archives', 'opt select_' + count, NaN, item)
                count++
            }
        }
    })
});
// Обработчик события: выбираем архивный файл
let opt = findElements('.opt')
console.log(opt)

// Обработчик события на скролл '.modal_content'
let mc = document.querySelector('.modal_content')
$(function () {
    $(mc).scroll(function () {
        if ($(mc).scrollTop() > 500) {
            $('#scroll_top').show();
            $('#scroll_bottom').show();
        } else {
            $('#scroll_top').hide();
            $('#scroll_bottom').hide();
        }
    });
    //
    $('#scroll_top').click(function () {
        $(mc).animate({ scrollTop: 0 }, 100);
        return false;
    });
    $('#scroll_bottom').click(function () {
        $(mc).animate({ scrollTop: $(mc).height() * 9999 }, 100);
        return false;
    });
});
//


