function NavBurger() {
    const icon = document.querySelector('#burger-icon')
    const items = document.querySelector('#burger-items')
    const openIcon = document.querySelector('#burger-icon-open')
    const closeIcon = document.querySelector('#burger-icon-close')

    icon.addEventListener('click', function () {
        items.classList.toggle('hidden')
        openIcon.classList.toggle('hidden')
        closeIcon.classList.toggle('hidden')

    })
}
NavBurger()

// Projects APP photo gallery - zoom image on click - TODO review
document.addEventListener("click", function (event) {
    // Check to see if the clicked element is a thumbnail
    if (event.target.classList.contains("project-thumb-img" )) {
        let clickedImage = event.target;  // Set main picture to match the thumbnail
        let imageContainer = clickedImage.parentElement // Set parent DIV

        // Disable scrolling
        document.body.style.overflow === '' ? document.body.style.overflow = 'hidden' : document.body.style.overflow = ''

        imageContainer.classList.toggle('project-big-picture')
    }
    else if (event.target.id === "project-image-container") {
        let imageContainer = event.target
        document.body.style.overflow === '' ? document.body.style.overflow = 'hidden' : document.body.style.overflow = ''
        imageContainer.classList.toggle('project-big-picture')
    }
});

