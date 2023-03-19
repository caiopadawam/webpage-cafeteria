const navItems = document.querySelectorAll('.navbar-nav .nav-item');
navItems.forEach(item => {
    item.addEventListener('click', function() {
        navItems.forEach(i => {
            i.classList.remove('active');
        })
        this.classList.add('active');
    });
});