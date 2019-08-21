let nav = document.querySelector('nav');

function mudar() {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        nav.style.backgroundColor = '#1f0464';
        nav.style.height = '50px'
    } else {
        nav.style.backgroundColor = 'rgba(69,27,74,.088)';
        nav.style.height = '120px'
    }
}

window.onscroll = function () { mudar() }

function mudaCor() {
    let back = document.querySelector('body')
    back.classList.toggle('gray');
}

function mudaLogin() {
    let usuario = document.getElementById('usuario')
    let empresa = document.getElementById('empresa')
    let divUsuario = document.getElementById('divUsuario')
    let divEmpresa = document.getElementById('divEmpresa')

    usuario.classList.toggle('ativo')
    empresa.classList.toggle('ativo')

    if(usuario.classList.contains('ativo')){
        divUsuario.classList.remove('none')
        divEmpresa.classList.add('none')
    }else if(empresa.classList.contains('ativo')){
        divUsuario.classList.add('none')
        divEmpresa.classList.remove('none')
    }
    
}