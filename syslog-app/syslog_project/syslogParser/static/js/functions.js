/* Ф-ции добавления, поиска элементов html, ajax-запросы*/
//
//urlGetData = 'http://127.0.0.1:8000/serchDataBatchOutput/'
//urlSerchData = 'http://127.0.0.1:8000/serchData/'
//urlZipFiles = 'http://127.0.0.1:8000/serchZipFiles/'
urlGetData = 'http://192.168.220.72:8000/serchDataAll/'
urlSerchData = 'http://192.168.220.72:8000/serchData/'
urlZipFiles = 'http://192.168.220.72:8000/serchZipFiles/'
urlExtractZipFiles = 'http://192.168.220.72:8000/extractZipFiles/'
//
function addElement(child, parent = 'body', classChild = 'no_class', type = NaN, text = '') {
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
    /*  Ф-ция находит эдементы на странице по классу и
        возвращает массив.
    */
    return document.querySelectorAll(className) //массив объектов
};
//
function findOneElement(className) {
    /*
        Ф-ция находит эдемент на странице по классу и
        возвращает.
    */
    return document.querySelector(className) //массив объектов
};
//
function ajaxGetData() {
    // ajax-запрос .. Получаем весь файл syslog.txt
    const promise = axios(urlGetData)
    return promise
};
//
function ajaxSerchData(serchString) {
    // ajax-запрос .. Получаем искомые данные из файла syslog.txt
    const promise = axios(`${urlSerchData}${serchString}`)
    return promise
};
//
function addZipFiles() {
    // ajax-запрос .. Получаем список файлов *.zip
    const promise = axios(urlZipFiles)
    return promise
}
//
function extractZipFiles() {
    // ajax-запрос .. Получаем данные распакованного zip-архива
    const promise = axios(urlExtractZipFiles)
    return promise
}
//