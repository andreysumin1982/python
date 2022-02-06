/* Ф-ции добавления, поиска элементов html, ajax-запросы*/
//
function addElement(child, parent = 'body', classChild = 'no_class', type = NaN, text = ''){
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
function findElement(className){
    /*  Ф-ция находит эдементы на странице по классу и
        возвращает массив.
    */
    return document.querySelectorAll(className) //массив объектов
};
//
function findOneElement(className){
    /*
        Ф-ция находит эдемент на странице по классу и
        возвращает.
    */
    return document.querySelector(className) //массив объектов
};
//

