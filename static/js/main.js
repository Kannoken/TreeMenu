$(document).ready(function () {
    function hashHandler() {
        this.oldHash = window.location.hash;
        this.Check;
        var ex;
        var that = this;
        var detect = function () {
            if (that.oldHash != window.location.hash) {
                var allInputs = document.getElementsByTagName("a");
                for (var x = 0; x < allInputs.length; x++) {
                    if (allInputs[x].hash == window.location.hash)
                        ex = $(allInputs[x]).parent().children('ul.tree');
                    // else
                    //     allInputs[x].parent().children('ul.tree').hide()

                }
                that.oldHash = window.location.hash;
            }
        };
        // console.log(ex)
        // $(ex).parent().children('ul.tree').show();

        this.Check = setInterval(function () {
            detect()
        }, 100);
    }

    //
    // $('.tree-toggler').click(function () {
    //     $(this).parent().children('ul.tree').toggle(300);
    // });

    var hashDetection = new hashHandler();
});