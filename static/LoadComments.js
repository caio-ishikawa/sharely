const loadComments = () => {
    var div = document.getElementById('comments')
    if (div.classList.contains('d-none')){
        div.className = 'none'
        console.log('hey this works')
    }
    else {
        div.className = 'd-none'
    }
}



/// create DOM elements for comment form as well as show comment in a retractable div ///