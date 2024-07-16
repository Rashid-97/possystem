document.addEventListener('DOMContentLoaded', function() {
    const currentPath = window.location.href;
    const navItem = document.querySelectorAll('.sidebar .nav-item');

    navItem.forEach(function(item) {
        let links = item.querySelectorAll('a:not(.nav-link)');
        let is_curr_page = false;
        if (links.length) { // eger children varsa
            for (let link of links) {
                if (link.href && currentPath == link.href) {
                    is_curr_page = true;
                    $(link).addClass('active');
                    break;
                }
            }
            if (is_curr_page) {
                $(item).find('.nav-link').eq(0).removeClass('collapsed');
                $(item).attr('aria-expanded', 'true');
                $(item).find('.nav-content').addClass('show')
                $(item).find('.nav-item').addClass('show')
                $(item).find('.nav-item').find('.nav-content').removeClass('show')
            }
        }
        else {
            if (currentPath == item.querySelector('.nav-link').href) {
                $(item).find('.nav-link').removeClass('collapsed');
            }
        }
    });
});
