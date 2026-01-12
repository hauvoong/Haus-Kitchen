const editButtons = document.getElementsByClassName("btn-edit");
const recipeText = document.getElementById("id_content");
const recipeForm = document.getElementById("recipeForm");
const submitButton = document.getElementById("submitButton");

const deleteButtons = document.querySelectorAll('.btn-delete');
const confirmDeleteBtn = document.getElementById('confirmDeleteBtn');


/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated recipe's ID upon click.
* - Fetches the content of the corresponding recipe.
* - Populates the `recipeText` input/textarea with the recipe's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_recipe/{recipeId}` endpoint.
*/


/**
 * * Initializes delete functionality for the provided delete recipe buttons.
 */

document.addEventListener('DOMContentLoaded', function() {
    deleteButtons.forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const href = btn.getAttribute('href');
            confirmDeleteBtn.setAttribute('href', href);
            const modal = new bootstrap.Modal(document.getElementById('deleteRecipeModal'));
            modal.show();
        });
    });
});
