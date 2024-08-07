$(document).ready(function() {
    $('INPUT#btn_translate').click(function() {
        const code = $('INPUT#language_code').val();
        const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${code}`;
        $.get(url, function(data) {
            $('DIV#hello').text(data.hello);
        });
    });
})