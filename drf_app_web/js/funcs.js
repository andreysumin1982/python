/* --------------------------------------------------------------------------------------------- */
/* */
const url = 'https://wttr.in/%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3';
/* */
function addElement(child, parent = 'body', classChild = 'childBody', type = NaN, text = '') {
    /*Ф-ция создает элемент на странице:
        На вход подаются 1 обязятельный элемент и 3 не обязательных:
     Дочерний (div, p, li ...), класс для дочернего элемента , родительский элемент - ('.classname'), тип дочернего элемента.
     По умолчинию все элементы создаются в теле документа body.
     */
    let childElement = document.createElement(child)
    childElement.type = type
    childElement.className = classChild
    childElement.innerHTML = text
    document.querySelector(parent).appendChild(childElement)
};
//
function findElement(className) {
    /*Ф-ция находит элементы на странице по классу. 
    */
    return document.querySelector(className)
};
//

/* --- */