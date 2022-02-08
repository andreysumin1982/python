/* События на html-элементы */
//
function handleButtonClick(){
    /* Событие кнопки 'Найти' */
    let modal = findOneElement('.modal') // получаем модальное окно (div)
        modal.style.display = "block" // изменяем состояние на block(блочный элемент)
        // ajax-запрос
        ajaxGetData().then(response => {
           let count = 0
           console.log(response.split('\n'))
           //console.log(response)
           //response.split('\n').forEach(elem => {
           //     console.log(elem)
                //addElement('p', '.modal_content', `p${count}`)
                //document.querySelector(`.p${count}`).innerHTML = elem
                //addHtml(elem)
           //})
        })
    };
//
function addHtml(elem){
    findOneElement('.modal_content').innerHTML +=`
                                                ${elem}<br>
                                                `
    };

// Обработчик события на кнопку 'Найти'
let btn = findOneElement('.inp_btn')
    btn.addEventListener('click', ()=> {
        handleButtonClick() // Вызываем ф-цию handleButtonClick()
    });