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
    btn.onclick = handleButtonClick()
/**/
let btn2 = findOneElement('.inp_btn')
    btn2.onclick = ajaxGetData()
    .then(response => {
        //console.log(response.split())
        let count = 0
        response.split().forEach(elem =>{
            console.log(elem)
            addElement('p', '.modal_content', `${count}`)
            findOneElement(`p${count}`).innerHTML = elem
            count++1
        })
    })