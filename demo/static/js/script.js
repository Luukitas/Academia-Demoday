let nav = document.querySelector('nav');

function mudar() {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        nav.style.backgroundColor = 'rgba(69,27,74)';
        nav.style.height = '50px'
    } else {
        nav.style.backgroundColor = 'rgba(69,27,74,.088)';
        nav.style.height = '120px'
    }
}

window.onscroll = function() { mudar() }

function mudaCor() {
    let back = document.querySelector('body')
    back.classList.toggle('gray');
}