// script.js

document.addEventListener('DOMContentLoaded', function() {
    // Add event listeners to all toggle buttons
    document.querySelectorAll('.toggle-details').forEach(button => {
    button.addEventListener('click', function() {
        const details = this.parentElement.querySelector('.expanded-details');
        details.classList.toggle('expanded');
        if (details.classList.contains('expanded')) {
        this.innerText = 'See Less';
        } else {
        this.innerText = 'See More';
        }
    });
    });
});
