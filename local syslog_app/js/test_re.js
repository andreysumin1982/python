//
//let arr = ['sdfs','errrrr','we','34','f','2','df','ggg']
//
//let str = 'sdgdfhgdfghddf'
//
//console.log(arr.length)
//x = 8
//for (let i = 1; i < x+1; i++){
//    let s = i/x*100
//   console.log(i, s+'%')
//}
//---------------------------------------
// Обработчик события на скролл

// Размер страницы с учетом прокрутки
let scrollWidth = Math.max(
    document.body.scrollHeight, document.documentElement.scrollHeight,
    document.body.offsetHeight, document.documentElement.offsetHeight,
    document.body.clientHeight, document.documentElement.clientHeight,
    );
console.log(scrollWidth)
//
console.log(innerWidth, innerHeight) // ширина и высота экрана
//
// получение текущей прокрутки
console.log(window.pageYOffset) // прокрутка по y
console.log(window.pageXOffset) // прокрутка по x
//
// let modal = document.querySelector('.modal_content');
//     console.log(modal.offsetParent); // относительно родителя, (по умолчан. body)
//     console.log(modal.offsetWidth, modal.offsetHeight) // ширина и высота обьекта

//
//let sc = document.querySelector('.modal_content')
//  sc.addEventListener('scroll', function ()
//    { 
      //console.log(sc.pageYOffset || sc.scrollTop)
      
      //console.log(sc.scrollTop)
      //console.log(sc.scrollHeight)
      //console.log(sc.clientHeight)
//    });
    