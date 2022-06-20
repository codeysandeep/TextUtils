function copy() {
    let copyButton = document.getElementById('copy-button');
    if (document.selection) {
        var range = document.body.createTextRange();
        range.moveToElementText(document.getElementById("analyzed-text"));
        range.select().createTextRange();
        document.execCommand("copy");

    } else if (window.getSelection) {
        var range = document.createRange();
        range.selectNode(document.getElementById("analyzed-text"));
        window.getSelection().addRange(range);
        document.execCommand("copy");
        copyButton.innerHTML = "Text Copied"
    }
}