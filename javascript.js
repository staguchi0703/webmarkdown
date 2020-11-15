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

function reloadHtml() {
// idからHTMLelemntを取得する
var html_id = document.getElementById("markedPreview");
var mdElem = document.getElementById("markdown_editor_textarea");
// emElemから要素のテキストを抽出(.value)してmarked()に渡す
var md_article = marked(mdElem.value);
//html_idにmarkedで変換したhtmlを挿入する
html_id.innerHTML = md_article;
};
