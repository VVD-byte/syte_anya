function like(id){
    if (getCookie('a') == undefined){document.cookie = 'a=;'}
    let el = document.getElementById(id);
    if (el.src.search('lova_no') != -1){
        el.src = '/static/lova_yes.JPG';
        if (getCookie('a').search(toString(id)) == -1){
        document.cookie = 'a = ' + getCookie('a') + id + ',';
        }
    }
    else {
        el.src = '/static/lova_no.JPG';
        let end = '';
        for (var i = 0;i < getCookie('a').split(',').length; i++){
            if (parseInt(getCookie('a').split(',')[i]) != id && getCookie('a').split(',')[i] != ''){
                end += getCookie('a').split(',')[i] + ',';
            }
        }
        document.cookie = 'a=' + end + ';';
    }
    document.getElementById('int').textContent = getCookie('a').split(',').length - 1;
}

function buy(id){
    if (getCookie('b') == undefined){document.cookie = 'b=;'}
    let el = document.getElementById(id + "_1");
    if (el.textContent == "В корзину"){
        el.textContent = 'Убрать из корзины';
        if (getCookie('b').search(toString(id)) == -1){
        document.cookie = 'b = ' + getCookie('b') + id + ',';
        }
    }
    else {
        el.textContent = 'В корзину';
        let end = '';
        console.log(id);
        for (var i = 0;i < getCookie('b').split(',').length; i++){
            if (parseInt(getCookie('b').split(',')[i]) != id && getCookie('b').split(',')[i] != ''){
                console.log(parseInt(getCookie('b').split(',')[i]));
                end += getCookie('b').split(',')[i] + ',';
            }
        }
        document.cookie = 'b=' + end + ';';
    }
    document.getElementById('int').textContent = getCookie('b').split(',').length - 1;
}

function redy(){
 for (var i = 0;i < getCookie('a').split(',').length; i++){
        try{
            document.getElementById(parseInt(getCookie('a').split(',')[i])).src = '/static/lova_yes.JPG';
            }
        catch (e){}
        }
  document.getElementById('int').textContent = getCookie('a').split(',').length - 1;
};

function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}