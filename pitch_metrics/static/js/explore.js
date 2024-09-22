console.log("explore.js is loaded");

document.addEventListener('DOMContentLoaded', function() {
    console.log("Page ready, adding event listeners");

    // Sélectionner tous les éléments ayant la classe "label-button"
    let buttons = document.querySelectorAll('.label-button');

    buttons.forEach(function(button) {
        console.log("Attaching event listener to button");

        button.addEventListener('click', function(e) {
            e.preventDefault();  // Empêcher le comportement par défaut du lien

            // Récupérer l'ID du label depuis l'attribut "data-label-id"
            var labelId = this.getAttribute('data-label-id');
            console.log("Label ID: " + labelId);

            // Requête AJAX pour charger les détails du label
            fetch(`/explore/${labelId}/`, {
                method: 'GET',
            })
            .then(response => response.text())
            .then(data => {
                // Mettre à jour le contenu du conteneur des détails avec la réponse
                document.getElementById('label-details-container').innerHTML = data;
                console.log("Détails du label chargés avec succès");
            })
            .catch(error => console.error('Erreur lors du chargement des détails:', error));
        });
    });
});
