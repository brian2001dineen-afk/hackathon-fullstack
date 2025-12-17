const editPostButton = document.getElementById("postEdit");

const deletePostButton = document.getElementById("postDelete");
const deletePostModal = new bootstrap.Modal(document.getElementById("deletePostModal"));
const confirmDeletePost = document.getElementById("confirmDeletePost");

/**
* Initializes post edit functionality for the provided edit button.
* 
* Retrieves the associated post's ID upon click.
* Sends the user to post_edit.html to update post content
*/

if (editPostButton) {
    editPostButton.addEventListener("click", function() {
        const postId = editPostButton.dataset.postId;
        window.location.href = `/${postId}/editpost/`;
    });
}

/**
* Initializes post deletion functionality for the provided delete button.
* 
* Retrieves the associated post ID upon click.
* Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific post.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/

if (deletePostButton) {
    deletePostButton.addEventListener("click", function() {
        const postId = deletePostButton.dataset.postId;
        confirmDeletePost.href = `/${postId}/deletepost/`;
        deletePostModal.show();
    });
}
