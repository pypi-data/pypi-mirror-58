$(document).ready( function () {
    $("dmc-datetime input").addClass("datepicker");
    $("[data-form-control='date']").addClass("datepicker");
    $("[data-form-control='time']").addClass("timepicker");

    // Initialize sidenav [MAT]
    $(".sidenav").sidenav();

    // Initialize datepicker [MAT]
    $('.datepicker').datepicker({
        format: 'dd.mm.yyyy',
        // Translate to German
        i18n: {
            months: ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'],
            monthsShort: ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez'],
            weekdays: ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'],
            weekdaysShort: ['So', 'Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa'],
            weekdaysAbbrev: ['S', 'M', 'D', 'M', 'D', 'F', 'S'],

            // Buttons
            today: 'Heute',
            cancel: 'Abbrechen',
            done: 'OK',
        },

        // Set monday as first day of week
        firstDay: 1,
        autoClose: true
    });

    // Initialize timepicker [MAT]
    $('.timepicker').timepicker({
        twelveHour: false,
        autoClose: true,
        i18n: {
            cancel: 'Abbrechen',
            clear: 'Löschen',
            done: 'OK'
        },
    });

    // Initialize tooltip [MAT]
    $('.tooltipped').tooltip();

    // Initialize select [MAT]
    $('select').formSelect();

    // Initalize print button
    $("#print").click(function () {
        window.print();
    });

    // Initialize Collapsible [MAT]
    $('.collapsible').collapsible();

    // Initialize FABs [MAT]
    $('.fixed-action-btn').floatingActionButton();

    // Initialize Modals [MAT]
    $('.modal').modal();

    $('table.datatable').each(function (index) {
        $(this).DataTable({
            "paging": false
        });
    });
});
