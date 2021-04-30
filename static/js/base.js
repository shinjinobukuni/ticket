const menuBtn = document.querySelector('#menu-btn');
const sideMenu = document.querySelector('#side-menu');
const menuList = document.querySelector('#menu-list');

const menuItemArray = document.getElementsByClassName('menu-item')
const menuTextArray = document.getElementsByClassName('menu-text')

// メニューボタンのクリックイベント
menuBtn.addEventListener('click', () => {

  // サイドメニュー領域の表示cssをopenとcloseで切替
  sideMenu.classList.toggle('side-menu-open');
  sideMenu.classList.toggle('side-menu-close');

    for (var i = 0; i < menuItemArray.length; i++) {
        // 各メニューのcssをopenとcloseで切替
        menuItemArray[i].classList.toggle('menu-item-close');
        menuTextArray[i].classList.toggle('menu-text-close');
    }
});