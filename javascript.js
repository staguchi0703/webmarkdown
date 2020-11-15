// tooltips
(function () {
    window.addEventListener("load", function () {
        $('[data-toggle="tooltip"]').tooltip();
    });
})();


// icon

function saveHandler(editor) {
    const a = document.createElement('a');
    a.href = 'data:text/plain,' + encodeURIComponent(mdContents);
    a.download = 'article.md';
    a.click();
};


// markdown to html translation

function reloadHtml(editor) {
var html_id = document.getElementById("markedPreview");
var md_article = $('#markdown_editor_textarea').val();
html_id.innerHTML = marked(md_article);
};
