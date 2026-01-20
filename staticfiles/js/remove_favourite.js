document.addEventListener('DOMContentLoaded', function () {
  var removeModal = document.getElementById('removeFavouriteModal');
  removeModal.addEventListener('show.bs.modal', function (event) {
    var button = event.relatedTarget;
    var removeUrl = button.getAttribute('data-remove-url');
    var form = document.getElementById('removeFavouriteForm');
    form.action = removeUrl;
  });
});