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
function addHtml(elem){
    //ф-ция добавляет в modal_content строки
    findOneElement('.modal_content').innerHTML +=`
                                                ${elem}<br>
                                                `
    };
//
// Обработка промиса
/*function dataProcessing(data, i = 0, count = 0){
    let len = data.length
    for (let i=0; i<10; i++){
        addHtml(data[count]) // выводим в modal_content
        count++
    }
    timer = setTimeout(()=> {
        if (count < len){
            // рекурсивно вызываем с вх. аргументами
            dataProcessing(data, i = 0, count)
        }
        else {
            btn.value = 'Найти' // возвращаем название кнопки
            clearTimeout(timer) // отменяем вызов ф-ции setTimeout
        }
    }, 150)
};*/
//
/* */
function showDataOutput(className, data){
    /*
        Ф-ция находит элемент по классу и 
        размещает в нем данные
    */
    return document.querySelector(className).innerHTML += `Output: ${data}`
};
/* */
function processingData(data){
    /* ф-ция обрабатывает промис */
    for(let i=0; i<10; i++){
        data.forEach(element => {
            // console.log(element)
            showDataOutput('.modal_content', element.name)
        })
    };
};
/* */
//
function dataProcessing(data){
    //let len = data.length
    let count = 0
    //
    for (let i=0; i<30; i++){
        if (data[count] != undefined){
            addHtml(data[count]) // выводим в modal_content
            count++    
        }
    }
    btn.value = 'Найти' // возвращаем название кнопки
    //
};    
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
                //
                console.log('пустое поле')
                btn.value = 'Найти'
                return
            }
            else{
                //ajax-запрос, после выполнения получаем промис
                ajaxSerchData(inp.value).then(response => {
                    let resp = response.data // берем данные
                    // передаем промис в обработку
                    dataProcessing(resp.split('\n'))
                    
                })
            }
        }
        else{
            clearTimeout(timer)
            btn.value = 'Найти'
        }
    });
//
// Обработчик события на скролл '.modal_content'
let mc = document.querySelector('.modal_content')
$(function(){
	$(mc).scroll(function(){
		if($(mc).scrollTop() > 100) {
			$('#scroll_top').show();
            $('#scroll_bottom').show();
		} else {
			$('#scroll_top').hide();
            $('#scroll_bottom').hide();
		}
	});
 
	$('#scroll_top').click(function(){
		$(mc).animate({scrollTop: 0}, 100);
		return false;
	});
    $('#scroll_bottom').click(function(){
		let modal = findOneElement('.modal_content')
        ajaxRequest().then(response =>{  // ajax-запрос   
            processingData(response.data)   // передаем промис в ф-цию processingData)
            //removeElement('.btn') // удаляем кнопку
            modal.scrollTo(0, modal.scrollHeight) // прокручиваем контент вниз до конца
    })                
        // $(mc).animate({scrollTop: $(mc).height() * $(mc).height()}, 100);
		// return false;
	});
});