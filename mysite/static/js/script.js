// Wait for the DOM content to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Find the form element by its ID
    const searchForm = document.getElementById('search-recipe');
    // Find the table element by its ID
    const recipeTable = document.getElementById('recipe-table');

    // Add an event listener to the form for the 'submit' event
    searchForm.addEventListener('submit', function(event) {
        // Prevent the form from submitting the traditional way
        event.preventDefault();
        // Scroll to the table element
        recipeTable.scrollIntoView({ behavior: 'smooth' });
    });
});