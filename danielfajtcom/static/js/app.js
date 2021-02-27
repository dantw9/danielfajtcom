function NavBurger() {
    const icon = document.querySelector('#burger-icon')
    const items = document.querySelector('#burger-items')
    const openIcon = document.querySelector('#burger-icon-open')
    const closeIcon = document.querySelector('#burger-icon-close')

    icon.addEventListener('click', function (){
        items.classList.toggle('hidden')
        openIcon.classList.toggle('hidden')
        closeIcon.classList.toggle('hidden')

    })
}

NavBurger()