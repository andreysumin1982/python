// События, модальное окно, вывод погодных данных
url_summary = 'http://127.0.0.1:8000/summary/'
//
setInterval(() =>{
    /*
        выполняется кажд. 2 часа
    */
    ajaxRequest(url_summary).then((summary) => {
            //console.log(`ok -  ${summary}`)
            for (let i in summary){
                console.log(i, summary[i])
            }


    });
}, 5000000);