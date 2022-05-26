//* ------------------------------- */

function addHtml(dataOutput) {
    //ф-ция добавляет в modal_content данные
    findOneElement('.modal_content').innerHTML = `<pre>${dataOutput}<br>`
    findOneElement('.inp_btn').value = 'Найти'
};

// Обработчик события на кнопку 'Найти'
let btn = findOneElement('.inp_btn')
btn.addEventListener('click', () => {
    if (findOneElement('.div_info').innerHTML.length == 0) { // Если ничего не выбрано и поля пустые, подгружаем весь syslog
        btn.value = 'Идет поиск'
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
        }
        else { // если поле заполнено ?!
            //ajax-запрос, после выполнения получаем промис
            ajaxSerchData(inp.value)
                .then(response => {
                    //console.log(response)
                    // передаем промис в обработку
                    response.text().then(data => {
                        if (data.length > 0) {
                            addHtml(data)
                        }
                        else { addHtml('Ничего не найдено.'); return }
                    })
                })
                .catch(error => {    //ошибки
                    console.log(error)
                    addHtml(error)
                });
            btn.value = 'Найти'; return
        }
    }
    else if (findOneElement('.inp_btn').value == 'Распаковать и найти' && findOneElement('.div_info').innerHTML.length > 0) {
        if (findOneElement('.input').value == '') { // если поле пустое
            let zipFile = findOneElement('.div_info').innerHTML
            extractZipFiles(zipFile).then(response => {
                findOneElement('.modal_content').innerHTML = `Status:${response.status}<br>`
                response.text().then(data => {
                    findOneElement('.modal_content').innerHTML += `${data}<br>`
                })
            })
            findOneElement('.inp_btn').value = 'Найти'
        }
        else { // иначе 
            findOneElement('.modal_content').innerHTML = 'No'
        }
    }
    else if (findOneElement('.input').value.length > 0 && findOneElement('.inp_btn').value == 'Найти' && findOneElement('.div_info').innerHTML.length > 0) {
        findOneElement('.modal_content').innerHTML = findOneElement('.input').value
    }

});

// Добавляем архивные файлы в элемент <select>..</select>
let selectBtn = findOneElement('.archives')
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
        // Обработчик события: выбираем архивный файл
        let opt = findElements('.opt')
        opt.forEach(elem => {
            if (elem.innerText.includes('.zip')) { // отбрасываем, если не zip
                elem.addEventListener('click', () => {
                    findOneElement('.div_btnclear').style.display = 'block'
                    findOneElement('.div_info').innerHTML = elem.innerText
                    findOneElement('.select').style.display = 'none'
                    findOneElement('.inp_btn').value = 'Распаковать и найти'
                    findOneElement('.input').value = ''
                })
            }
        })
    })
}); //

//Обработчик события на кнопку 'Очистить'
let btnClear = findOneElement('.div_btnclear')
btnClear.addEventListener('click', () => {
    findOneElement('.div_btnclear').style.display = 'none'
    findOneElement('.div_info').innerHTML = ''
    findOneElement('.select').style.display = 'block'
    findOneElement('.select').selected = true // Пункт по умолчанию: 'Выберите архивные файлы'
    findOneElement('.inp_btn').value = 'Найти'
    findOneElement('.modal_content').innerHTML = ''
    findOneElement('.input').value = ''
});

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


