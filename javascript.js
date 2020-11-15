// tooltips
(function() {
    window.addEventListener("load", function() {
    $('[data-toggle="tooltip"]').tooltip();
    });
})();


// icon

function saveHandler(editor){
    const a = document.createElement('a');
    a.href = 'data:text/plain,' + encodeURIComponent(mdContents);
    a.download = 'article.md';
    a.click();
};


console.log('test')

// markdown to html translation
var html_id = document.getElementById("markedPreview");
html_id.innerHTML = "test elements";

// marked('# Marked in the browserRendered by **marked**. test text');
