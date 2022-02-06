/* События на html-элементы */
//
function handleButtonClick(){
    /* Событие кнопки 'Найти' */
    let btn = findOneElement('.inp_btn')
        btn.addEventListener('click', ()=> {
            let modal = findOneElement('.modal') // получаем модальное окно (div)
                modal.style.display = "block" // изменяем состояние на block(блочный элемент)
            })
};
let btn = findOneElement('.inp_btn')
    btn.oncklick = handleButtonClick()
//
