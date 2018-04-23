$(document).ready(function () {

    $('.tree-toggler').click(function () {
        $(this).parent().children('ul.tree').toggle(300);
    });

});