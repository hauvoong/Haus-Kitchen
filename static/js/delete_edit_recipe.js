/**
 * Initializes delete functionality for the provided delete recipe buttons.
 */

document.addEventListener('DOMContentLoaded', function() {
    
    const deleteButtons = document. querySelectorAll('.btn-delete-recipe');
    const confirmDeleteBtn = document.getElementById('confirmDeleteBtn');

    deleteButtons.forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            
            // ✅ Get the URL from 'data-recipe-url' NOT 'href'
            const recipeUrl = btn.getAttribute('data-recipe-url');
            
            // Set the URL on the confirm button
            confirmDeleteBtn.setAttribute('href', recipeUrl);
            
            // Show the modal
            const modal = new bootstrap.Modal(document. getElementById('deleteRecipeModal'));
            modal.show();
        });
    });
});