$(document).ready(function() {
    var text_max = 140;
    $('#characterCount').html(text_max + ' characters remaining');

    $('#id_tweet_container').keyup(function() {
        var text_length = $('#id_tweet').val().length;
        var text_remaining = text_max - text_length;

        $('#characterCount').html(text_remaining + ' characters remaining');
    });
});
