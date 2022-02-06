/* Заполняем элементами */
addElement('div', '.body', 'header')
addElement('div', '.header', 'input_box')
addElement('div', '.input_box', 'div_text')
    addElement('p', '.div_text', 'p_text')
    findOneElement('.p_text').innerHTML = 'text'
addElement('div', '.input_box', 'div_input')
    addElement('input', '.div_input', 'input', 'input')
addElement('div', '.input_box', 'div_btn')
    addElement('input', '.div_btn', 'inp_btn', 'button')
    findOneElement('.inp_btn').value = 'Найти'
//Добавляем модальное окно
addElement('div', 'body', 'modal')
    addElement('div', '.modal', 'modal_content')
